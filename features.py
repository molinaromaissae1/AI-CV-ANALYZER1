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

    results = []

    # نحيد الlabels
    text = text.replace("langues :", "").replace("languages :", "")

    # نقسم حسب الفواصل
    parts = text.split(",")

    for part in parts:
        part = part.strip()

        # Arabic
        if "arabe" in part or "arabic" in part:
            if "maternelle" in part:
                level = "C2"
            else:
                level = "Unknown"
            results.append({"name": "Arabic", "level": level})

        # French
        elif "français" in part or "french" in part:
            if "c1" in part:
                level = "C1"
            else:
                level = "Unknown"
            results.append({"name": "French", "level": level})

        # English
        elif "anglais" in part or "english" in part:
            if "c1" in part:
                level = "C1"
            else:
                level = "Unknown"
            results.append({"name": "English", "level": level})

        # Spanish
        elif "espagnole" in part or "spanish" in part:
            if "a2" in part:
                level = "A2"
            else:
                level = "Unknown"
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
