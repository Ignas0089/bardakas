# content_understanding.py

import re

def classify_text(normalized_text: str) -> list[dict]:
    """
    Simulates text classification. For now, returns a dummy list of categories with confidence scores.
    """
    # In a real scenario, this would involve an ML model prediction.
    # For now, we return dummy data based on the input text.
    if "verslas" in normalized_text.lower():
        return [
            {"category": "verslas", "score": 0.95},
            {"category": "ekonomika", "score": 0.70}
        ]
    elif "technologijos" in normalized_text.lower():
        return [
            {"category": "technologijos", "score": 0.92},
            {"category": "inovacijos", "score": 0.65}
        ]
    elif "asmeninis tobulėjimas" in normalized_text.lower():
        return [
            {"category": "asmeninis tobulėjimas", "score": 0.88},
            {"category": "psichologija", "score": 0.60}
        ]
    else:
        return [
            {"category": "bendrosios žinios", "score": 0.80},
            {"category": "kita", "score": 0.50}
        ]

def split_into_sentences(text: str) -> list[str]:
    """
    Helper function to split text into sentences.
    A simple rule-based approach for demonstration.
    """
    # This is a very basic sentence splitter.
    # More sophisticated methods would use NLP libraries.
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip()]

def extract_quotes(text: str, layout_regions: list[dict]) -> list[dict]:
    """
    Implements rule-based quote extraction (e.g., looking for text in quotes).
    """
    quotes = []
    # Rule-based detection: looking for text enclosed in double or single quotes
    # and also considering layout regions for potential blockquotes.
    
    # First, check for quotes within sentences
    for sentence in split_into_sentences(text):
        # Regex to find text within double quotes or single quotes
        # It handles cases where quotes might be at the beginning/end of a sentence
        # or within it.
        matches = re.findall(r'"([^"]*)"|\'([^\']*)\'', sentence)
        for match in matches:
            # One of the groups will be non-empty
            quote_content = match[0] if match[0] else match[1]
            if quote_content:
                quotes.append({"text": quote_content.strip(), "method": "rule_based_inline"})
    
    # Consider layout regions for blockquotes or distinct quoted paragraphs
    for region in layout_regions:
        if region.get("type") == "paragraph" or region.get("type") == "text_line":
            # A simple heuristic: if a paragraph starts and ends with quotes, or contains prominent quotes
            # This is a simplification; real layout analysis would be more complex.
            region_text = region.get("text", "").strip()
            if (region_text.startswith('"') and region_text.endswith('"')) or \
               (region_text.startswith("'") and region_text.endswith("'")):
                quotes.append({"text": region_text.strip('\'"'), "method": "rule_based_layout"})
            # Also check if the entire region is a quote, even if not perfectly enclosed
            elif re.search(r'^["\'].*["\']$', region_text):
                 quotes.append({"text": region_text.strip('\'"'), "method": "rule_based_layout_partial"})

    return quotes

def extract_topics(normalized_text: str, language: str) -> list[dict]:
    """
    Simulates topic extraction. For now, returns a dummy list of topics with scores.
    """
    # In a real scenario, this would involve an ML topic modeling algorithm.
    # For now, we return dummy data based on keywords and language.
    topics = []
    if language == "lt":
        if "lyderystė" in normalized_text.lower():
            topics.append({"topic": "lyderystė", "score": 0.85})
        if "inovacijos" in normalized_text.lower():
            topics.append({"topic": "inovacijos", "score": 0.75})
        if "verslas" in normalized_text.lower():
            topics.append({"topic": "verslas", "score": 0.70})
        if "technologijos" in normalized_text.lower():
            topics.append({"topic": "technologijos", "score": 0.65})
    elif language == "en":
        if "leadership" in normalized_text.lower():
            topics.append({"topic": "leadership", "score": 0.88})
        if "innovation" in normalized_text.lower():
            topics.append({"topic": "innovation", "score": 0.78})
        if "business" in normalized_text.lower():
            topics.append({"topic": "business", "score": 0.72})
        if "technology" in normalized_text.lower():
            topics.append({"topic": "technology", "score": 0.68})
    
    if not topics:
        topics.append({"topic": "bendrosios temos", "score": 0.60})
    
    return topics