import re

def extract_skills(text):
    skills_list = ["python", "excel", "communication", "management"]
    text = text.lower()
    found = []
    for s in skills_list:
        if s in text:
            found.append(s)
    return found


import re
from typing import List, Dict, Any

import re

def extract_languages(text):
    text = text.lower()
    words = text.split()

    results = []

    for i, word in enumerate(words):

        # Arabic
        if word in ["arabe", "arabic"]:
            level = "Unknown"
            if i+1 < len(words) and words[i+1] in ["maternelle"]:
                level = "C2"
            results.append({"name": "Arabic", "level": level})

        # French
        if word in ["français", "french"]:
            level = "Unknown"
            if i+1 < len(words) and words[i+1] in ["c1", "c2"]:
                level = words[i+1].upper()
            results.append({"name": "French", "level": level})

        # English
        if word in ["anglais", "english"]:
            level = "Unknown"
            if i+1 < len(words) and words[i+1] in ["c1", "c2"]:
                level = words[i+1].upper()
            results.append({"name": "English", "level": level})

        # Spanish
        if word in ["espagnole", "spanish"]:
            level = "Unknown"
            if i+1 < len(words) and words[i+1] in ["a2"]:
                level = "A2"
            results.append({"name": "Spanish", "level": level})

    return results
    

def extract_companies(text):
    companies = ["safran", "airbus", "deloitte"]
    text = text.lower()
    found = []
    for c in companies:
        if c in text:
            found.append(c.capitalize())
    return found


def extract_experience(text):
    matches = re.findall(r'(\d+)\s*(year|years|month|months)', text.lower())
    total = 0
    for num, unit in matches:
        if "year" in unit:
            total += int(num) * 12
        else:
            total += int(num)
    return total
