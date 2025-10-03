import random
from typing import List, Dict, Any

# Define simple structures for PARA entities
class UserProject:
    def __init__(self, name: str, keywords: List[str]):
        self.name = name
        self.keywords = keywords

class UserArea:
    def __init__(self, name: str, keywords: List[str]):
        self.name = name
        self.keywords = keywords

class UserResource:
    def __init__(self, name: str, keywords: List[str]):
        self.name = name
        self.keywords = keywords

class UserArchive:
    def __init__(self, name: str, keywords: List[str]):
        self.name = name
        self.keywords = keywords

class UserSettings:
    def __init__(self, default_para_settings: Dict[str, Any] = None):
        self.default_para_settings = default_para_settings if default_para_settings is not None else {}

    def has_default_para_for_tags(self, current_tags: List[str]) -> bool:
        # Simulate checking if default settings exist for any of the current tags
        return any(tag in self.default_para_settings for tag in current_tags)

    def get_default_para(self, current_tags: List[str]) -> Dict[str, Any]:
        # Simulate getting the default PARA based on tags
        for tag in current_tags:
            if tag in self.default_para_settings:
                return self.default_para_settings[tag]
        return {"type": "Inbox", "name": "Idėjų Pašto dėžutė", "method": "default_fallback"}


def assign_para(
    normalized_text: str,
    user_projects: List[UserProject],
    user_areas: List[UserArea],
    user_resources: List[UserResource],
    user_archives: List[UserArchive],
    user_settings: UserSettings,
    current_tags: List[str]
) -> Dict[str, Any]:
    """
    Assigns a PARA category (Project, Area, Resource, Archive) to a normalized text
    using a hybrid rule-based and ML-model-based approach.
    """
    # 1. Rule-based assignment (priority)
    for project in user_projects:
        if any(keyword.lower() in normalized_text.lower() for keyword in project.keywords):
            return {"type": "Project", "name": project.name, "method": "rule_based", "confidence": 1.0}

    for area in user_areas:
        if any(keyword.lower() in normalized_text.lower() for keyword in area.keywords):
            return {"type": "Area", "name": area.name, "method": "rule_based", "confidence": 1.0}
    
    for resource in user_resources:
        if any(keyword.lower() in normalized_text.lower() for keyword in resource.keywords):
            return {"type": "Resource", "name": resource.name, "method": "rule_based", "confidence": 1.0}

    for archive in user_archives:
        if any(keyword.lower() in normalized_text.lower() for keyword in archive.keywords):
            return {"type": "Archive", "name": archive.name, "method": "rule_based", "confidence": 1.0}

    # Check user-defined default settings
    if user_settings.has_default_para_for_tags(current_tags):
        default_para = user_settings.get_default_para(current_tags)
        if default_para:
            default_para["confidence"] = 0.95 # High confidence for user settings
            return default_para

    # 2. ML Model-based assignment (fallback) - Simulate with dummy probabilities
    # In a real scenario, a trained ML model would predict probabilities.
    para_options = ["Project", "Area", "Resource", "Archive", "Inbox"]
    
    # Simulate probabilities for each PARA type
    simulated_probabilities = {
        "Project": random.uniform(0.1, 0.9),
        "Area": random.uniform(0.1, 0.9),
        "Resource": random.uniform(0.1, 0.9),
        "Archive": random.uniform(0.1, 0.9),
        "Inbox": random.uniform(0.1, 0.9) # Inbox as a potential ML output too
    }

    # Simulate specific names for each PARA type
    simulated_names = {
        "Project": "Simulated Project X",
        "Area": "Simulated Area Y",
        "Resource": "Simulated Resource Z",
        "Archive": "Simulated Archive A",
        "Inbox": "Idėjų Pašto dėžutė"
    }

    # Select the PARA with the highest confidence
    best_para_type = max(simulated_probabilities, key=simulated_probabilities.get)
    best_confidence = simulated_probabilities[best_para_type]
    best_name = simulated_names[best_para_type]

    return {
        "type": best_para_type,
        "name": best_name,
        "method": "ml_based",
        "confidence": best_confidence
    }

def handle_para_assignment_result(para_assignment_result: Dict[str, Any], min_confidence_threshold: float = 0.6) -> Dict[str, Any]:
    """
    Handles the result of PARA assignment, falling back to "Inbox" if confidence is too low.
    """
    if para_assignment_result.get("confidence", 0.0) >= min_confidence_threshold:
        return para_assignment_result
    else:
        return {"type": "Inbox", "name": "Idėjų Pašto dėžutė", "method": "fallback", "confidence": 1.0} # Fallback has high confidence in itself