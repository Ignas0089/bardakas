import collections

def generate_auto_tags(text_classifications, topics, quotes_detected, ontology):
    """
    Simulates automatic tag generation based on text classifications, topics,
    quotes detected, and a predefined ontology.

    Args:
        text_classifications (list): A list of dictionaries, each with 'name' (category)
                                     and 'score' (confidence).
        topics (list): A list of dictionaries, each with 'topic' and 'score'.
        quotes_detected (bool): True if quotes were detected, False otherwise.
        ontology (dict): A dictionary representing the hierarchical knowledge structure.

    Returns:
        list: A list of generated tags.
    """
    tags = set()

    # Add tags based on classifications
    for classification in text_classifications:
        category_name = classification["name"]
        if category_name in ontology.get("categories", {}):
            tags.add(ontology["categories"][category_name])

    # Add tags based on topics
    for topic_item in topics:
        topic_name = topic_item["topic"]
        if topic_name in ontology.get("topics", {}):
            tags.add(ontology["topics"][topic_name])

    # Add #citata if quotes are detected
    if quotes_detected:
        tags.add("#citata")

    return sorted(list(tags))

def filter_tags_by_confidence(generated_tags_with_scores, high_threshold=0.8, low_threshold=0.5):
    """
    Filters generated tags based on their confidence scores.

    Args:
        generated_tags_with_scores (list): A list of tuples, where each tuple contains
                                           (tag, score).
        high_threshold (float): The threshold for automatically assigned tags.
        low_threshold (float): The threshold for suggested tags.

    Returns:
        tuple: A tuple containing two lists: (auto_assigned_tags, suggested_tags).
    """
    auto_assigned_tags = []
    suggested_tags = []
    for tag, score in generated_tags_with_scores:
        if score >= high_threshold:
            auto_assigned_tags.append(tag)
        elif score >= low_threshold:
            suggested_tags.append(tag)
    return auto_assigned_tags, suggested_tags

def edit_tags(current_tags, new_tags):
    """
    Simulates tag editing by replacing the current tags with new ones.

    Args:
        current_tags (list): The current list of tags.
        new_tags (list): The new list of tags to replace the current ones.

    Returns:
        list: The updated list of tags.
    """
    # In a real scenario, this might involve more complex logic like
    # adding, removing, or modifying individual tags.
    # For simulation, we simply replace the list.
    return list(set(new_tags)) # Ensure uniqueness and convert to list

# Simple ontology for demonstration
DEMO_ONTOLOGY = {
    "categories": {
        "Asmeninis Augimas": "#asmeninisaugimas",
        "Profesinis Tobulėjimas": "#profesinistobulejimas",
        "Kūryba": "#kuryba",
        "Verslas": "#verslas",
        "Technologijos": "#technologijos"
    },
    "topics": {
        "lyderystė": "#lyderyste",
        "motyvacija": "#motyvacija",
        "inovacijos": "#inovacijos",
        "AI": "#AI",
        "etika": "#etika",
        "produktyvumas": "#produktyvumas"
    }
}