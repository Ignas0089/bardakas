import re
import uuid
import string

def import_data(input_data):
    """
    Simulate data import. For now, it can just return the input data with a type.
    """
    if isinstance(input_data, bytes):  # Assuming bytes for image content
        return {"type": "image", "content": input_data}
    elif isinstance(input_data, str):
        return {"type": "text", "content": input_data}
    else:
        raise ValueError("Unsupported input data type")

def deduplicate(processed_data, existing_hashes):
    """
    Simulate deduplication. Use a simple in-memory set for existing_hashes.
    For images, a simple hash of content is used. For text, a hash of the normalized text.
    """
    content_to_hash = processed_data["content"]
    
    if processed_data["type"] == "image":
        # For simulation, we'll just use a simple hash of the image content (bytes)
        current_hash = str(uuid.uuid5(uuid.NAMESPACE_OID, content_to_hash.decode('latin-1')))
    elif processed_data["type"] == "text":
        # For text, normalize before hashing for better deduplication
        normalized_text = normalize_text(content_to_hash, "en") # Use a default language for hashing
        current_hash = str(uuid.uuid5(uuid.NAMESPACE_OID, normalized_text))
    else:
        raise ValueError("Unsupported data type for deduplication")

    if current_hash in existing_hashes:
        return {"status": "duplicate", "hash": current_hash}
    else:
        return {"status": "new", "hash": current_hash}

def perform_ocr(image_content):
    """
    Simulate OCR. For now, it can return a dummy text and empty blocks.
    """
    dummy_text = "Simulated OCR text from image content."
    empty_blocks = [] # In a real scenario, this would contain structured OCR output
    return dummy_text, empty_blocks

def detect_layout(ocr_blocks):
    """
    Simulate layout detection. Return an empty list for now.
    """
    return [] # In a real scenario, this would contain detected layout regions

def detect_language(text):
    """
    Simulate language detection. Return "lt" for now.
    """
    return "lt"

def normalize_text(text, language):
    """
    Implement basic text normalization (lowercase, remove punctuation, remove extra spaces).
    """
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()
    
    # No language-specific normalization for now, as per instructions
    return text