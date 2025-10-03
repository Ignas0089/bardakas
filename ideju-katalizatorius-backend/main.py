from fastapi import FastAPI, UploadFile, Form, status
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime

# Import pipeline components
from . import ocr_pipeline
from . import content_understanding
from . import tagging_service
from . import para_assignment_service
from . import action_relevance_service

app = FastAPI()

# In-memory storage for ideas (placeholder)
ideas_db = {}

class Source(str, Enum):
    share = "share"
    drag = "drag"

class PARAAssignmentType(str, Enum):
    Project = "Project"
    Area = "Area"
    Resource = "Resource"
    Archive = "Archive"
    Inbox = "Inbox"

class PARAAssignment(BaseModel):
    type: PARAAssignmentType
    name: str

class ActionType(str, Enum):
    create_task = "create_task"
    add_to_project = "add_to_project"
    just_save = "just_save"

class ActionSuggestionItem(BaseModel):
    action: ActionType
    score: float
    label: str

class ActionSuggestion(BaseModel):
    ideaId: UUID
    suggestions: list[ActionSuggestionItem]

class Idea(BaseModel):
    id: UUID
    originalContentUrl: Optional[str] = None
    ocrText: str
    tags: list[str]
    paraAssignment: PARAAssignment
    metadata: dict = Field(default_factory=dict)
    createdAt: datetime
    status: str = "processing" # Add status to the Idea model

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/ideas", status_code=status.HTTP_202_ACCEPTED)
async def upload_idea(
    file: UploadFile,
    source: Source = Form(...),
    url: Optional[str] = Form(None),
    device: Optional[str] = Form(None)
):
    idea_id = uuid4()
    
    # 1. OCR Pipeline
    file_content = await file.read()
    imported_data = ocr_pipeline.import_data(file_content)
    
    # For deduplication, we'd need a persistent store of hashes. For now, simulate.
    # existing_hashes = set()
    # deduplication_result = ocr_pipeline.deduplicate(imported_data, existing_hashes)
    # if deduplication_result["status"] == "duplicate":
    #     return {"id": idea_id, "status": "duplicate"} # Or handle as appropriate

    ocr_text, ocr_blocks = ocr_pipeline.perform_ocr(imported_data["content"])
    layout_regions = ocr_pipeline.detect_layout(ocr_blocks)
    detected_language = ocr_pipeline.detect_language(ocr_text)
    normalized_text = ocr_pipeline.normalize_text(ocr_text, detected_language)

    # 2. Content Understanding
    text_classifications = content_understanding.classify_text(normalized_text)
    extracted_quotes = content_understanding.extract_quotes(normalized_text, layout_regions)
    extracted_topics = content_understanding.extract_topics(normalized_text, detected_language)

    # 3. Tagging Service
    # Combine classifications and topics for tag generation, and check if quotes were detected
    quotes_detected_bool = bool(extracted_quotes)
    
    # For simulation, we'll pass a simplified structure to generate_auto_tags
    # In a real scenario, you might want to pass more detailed info or a combined score
    combined_classifications_for_tags = [{"name": c["category"], "score": c["score"]} for c in text_classifications]
    
    generated_tags = tagging_service.generate_auto_tags(
        combined_classifications_for_tags,
        extracted_topics,
        quotes_detected_bool,
        tagging_service.DEMO_ONTOLOGY
    )
    
    # For filter_tags_by_confidence, we need tags with scores.
    # Since generate_auto_tags returns just tags, we'll assign a dummy high score for now.
    # In a real system, generate_auto_tags would return tags with their confidence scores.
    generated_tags_with_scores = [(tag, 0.9) for tag in generated_tags] # Dummy scores
    auto_assigned_tags, _ = tagging_service.filter_tags_by_confidence(generated_tags_with_scores)

    # 4. PARA Assignment Service
    # For user_projects, user_areas, etc., we'll use dummy empty lists and settings for now.
    # In a real system, these would come from a user's profile/database.
    user_projects = []
    user_areas = []
    user_resources = []
    user_archives = []
    user_settings = para_assignment_service.UserSettings()

    para_assignment_result = para_assignment_service.assign_para(
        normalized_text,
        user_projects,
        user_areas,
        user_resources,
        user_archives,
        user_settings,
        auto_assigned_tags
    )
    final_para_assignment = para_assignment_service.handle_para_assignment_result(para_assignment_result)

    # 5. Action Relevance Service
    # For user_context, we'll use a dummy dictionary for now.
    user_context = {}
    action_scores = action_relevance_service.score_action_relevance(
        normalized_text,
        auto_assigned_tags,
        final_para_assignment,
        user_context
    )

    action_suggestions_list = []
    for action_type, score in action_scores.items():
        label = ""
        if action_type == "create_task":
            label = "[+] sukurti užduotį"
        elif action_type == "add_to_project":
            label = "[+] pridėti prie projekto"
        elif action_type == "just_save":
            label = "[+] tiesiog išsaugoti"
        action_suggestions_list.append(ActionSuggestionItem(action=ActionType(action_type), score=score, label=label))

    action_suggestions = ActionSuggestion(ideaId=idea_id, suggestions=action_suggestions_list)

    # Store the full processed idea
    idea = Idea(
        id=idea_id,
        originalContentUrl=url,
        ocrText=normalized_text,
        tags=auto_assigned_tags,
        paraAssignment=PARAAssignment(
            type=PARAAssignmentType(final_para_assignment["type"]),
            name=final_para_assignment["name"]
        ),
        metadata={
            "classifications": text_classifications,
            "quotes": extracted_quotes,
            "topics": extracted_topics,
            "language": detected_language,
            "layout_regions": layout_regions,
            "filename": file.filename,
            "source": source.value,
            "device": device,
            "action_suggestions": action_suggestions.dict() # Store action suggestions as part of metadata
        },
        createdAt=datetime.now(),
        status="processing"
    )
    ideas_db[str(idea_id)] = idea.dict()
    print(f"Processed and stored idea: {idea.dict()}")

    return {"id": idea_id, "status": "processing"}


@app.get("/ideas/{idea_id}", response_model=Idea)
async def get_idea_details(idea_id: UUID):
    from fastapi import HTTPException # Import HTTPException here
    idea = ideas_db.get(str(idea_id))
    if not idea:
        raise HTTPException(status_code=404, detail="Idea not found")
    return idea


@app.post("/actions/suggest", response_model=ActionSuggestion)
async def suggest_actions_for_idea(idea_request: dict):
    from fastapi import HTTPException # Import HTTPException here
    idea_id = idea_request.get("ideaId")
    if not idea_id:
        raise HTTPException(status_code=400, detail="ideaId is required")

    idea_data = ideas_db.get(str(idea_id))
    if not idea_data:
        raise HTTPException(status_code=404, detail="Idea not found")
    
    # Retrieve action suggestions from the stored idea's metadata
    action_suggestions_data = idea_data.get("metadata", {}).get("action_suggestions")
    if not action_suggestions_data:
        raise HTTPException(status_code=404, detail="Action suggestions not found for this idea")
    
    return ActionSuggestion(**action_suggestions_data)
