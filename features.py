import re

def extract_skills(text):
    skills_list = ["python", "excel", "communication", "management"]
    text = text.lower()
    return [s for s in skills_list if s in text]


def extract_languages(text):
    text = text.lower()

    languages = {
        "English": ["english", "anglais"],
        "French": ["french", "français"],
        "Arabic": ["arabic", "arabe"],
        "Spanish": ["spanish", "espagnol"]
    }

    levels = ["a1", "a2", "b1", "b2", "c1", "c2"]

    results = []

    for lang, keys in languages.items():
        for word in keys:
            if word in text:
                level = "Unknown"

                idx = text.find(word)
                context = text[max(0, idx-15): idx+15]

                for lvl in levels:
                    if lvl in context:
                        level = lvl.upper()

                if ("maternel" in context or "native" in context) and level == "Unknown":
                    level = "C2"

                results.append({"name": lang, "level": level})
                break

    return results


def extract_companies(text):
    companies = ["safran", "airbus", "deloitte"]
    text = text.lower()
    return [c.capitalize() for c in companies if c in text]


def extract_experience(text):
    matches = re.findall(r'(\d+)\s*(year|years|month|months)', text.lower())
    total = 0
    for num, unit in matches:
        if "year" in unit:
            total += int(num) * 12
        else:
            total += int(num)
    return total
