import random
from datetime import datetime

def get_text_embedding(text: str) -> list[float]:
    """
    Placeholder function to simulate text embedding generation.
    In a real scenario, this would use an ML model (e.g., Sentence-BERT)
    to convert text into a numerical vector.
    """
    # Dummy embedding: a list of random floats
    return [random.uniform(-1, 1) for _ in range(768)]

def check_active_project_relevance(idea_content: str, user_context: dict) -> bool:
    """
    Placeholder function to simulate checking if an idea is related to active projects.
    In a real scenario, this would involve comparing idea_content with active project
    descriptions, tasks, or keywords using NLP techniques.
    """
    # Dummy logic: randomly return True or False
    return random.choice([True, False])

def get_user_action_history_features(user_context: dict) -> dict:
    """
    Placeholder function to simulate extracting features from user action history.
    In a real scenario, this would analyze past user interactions (e.g., how often
    they create tasks, add to projects, or just save similar ideas).
    """
    # Dummy features: random probabilities for past actions
    return {
        "avg_task_creation_prob": random.uniform(0.1, 0.9),
        "avg_add_to_project_prob": random.uniform(0.1, 0.9),
        "avg_just_save_prob": random.uniform(0.1, 0.9),
    }

def get_current_time_features() -> dict:
    """
    Placeholder function to simulate extracting time-based features.
    In a real scenario, this would provide features like hour of day, day of week,
    which might influence user productivity or action preferences.
    """
    now = datetime.now()
    return {
        "hour_of_day": now.hour,
        "day_of_week": now.weekday(), # Monday is 0, Sunday is 6
    }

def contains_action_verbs(idea_content: str) -> bool:
    """
    Placeholder function to simulate checking for action verbs in the idea content.
    In a real scenario, this would use NLP techniques (e.g., part-of-speech tagging)
    to identify verbs that suggest an actionable idea (e.g., "implement", "start", "create").
    """
    action_verbs = ["implement", "start", "create", "develop", "organize", "plan", "review"]
    # Dummy logic: check if any of the dummy action verbs are in the content (case-insensitive)
    return any(verb in idea_content.lower() for verb in action_verbs)

def score_action_relevance(idea_content: str, tags: list[str], para_assignment: dict, user_context: dict) -> dict:
    """
    Scores the relevance of three actions (create_task, add_to_project, just_save)
    for a given idea, based on its content, metadata, and user context.

    This function simulates an ML model with dummy probabilities.

    Args:
        idea_content (str): The normalized OCR text of the idea.
        tags (list[str]): A list of generated tags for the idea.
        para_assignment (dict): The PARA assignment for the idea (e.g., {"type": "Project", "name": "My Project"}).
        user_context (dict): A dictionary containing user-specific context (e.g., active projects, action history).

    Returns:
        dict: A dictionary with relevance scores for each action:
              {"create_task": float, "add_to_project": float, "just_save": float}
    """
    # Placeholder for ML model features
    features = {
        "text_embedding": get_text_embedding(idea_content),
        "tags": tags,
        "para_type": para_assignment.get("type"),
        "para_name": para_assignment.get("name"),
        "is_related_to_active_project": check_active_project_relevance(idea_content, user_context),
        "user_action_history_features": get_user_action_history_features(user_context),
        "time_of_day_features": get_current_time_features(),
        "contains_action_verbs": contains_action_verbs(idea_content),
        "is_quote": "citata" in tags, # Simplified check for quote tag
    }

    # Simulate ML model prediction with dummy probabilities
    # In a real scenario, an actual ML model would use the 'features' to predict probabilities.
    
    # Generate random probabilities that sum up to approximately 1.0
    p_task = random.uniform(0.1, 0.6)
    p_project = random.uniform(0.1, 0.6)
    p_save = random.uniform(0.1, 0.6)

    total = p_task + p_project + p_save
    
    # Normalize probabilities to sum to 1.0
    probabilities = {
        "create_task": p_task / total,
        "add_to_project": p_project / total,
        "just_save": p_save / total,
    }

    return probabilities
