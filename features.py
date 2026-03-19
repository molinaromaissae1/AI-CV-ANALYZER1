import re

def extract_skills(text):
    skills_list = ["python", "excel", "communication", "management"]
    text = text.lower()
    found = []
    for s in skills_list:
        if s in text:
            found.append(s)
    return found


def extract_languages(text):
    text = text.lower()

    languages = {
        "English": ["english", "anglais"],
        "French": ["french", "français"],
        "Arabic": ["arabic", "arabe"],
        "Spanish": ["spanish", "espagnol", "espagnole"]
    }

    results = []

    for lang, keys in languages.items():
        for word in keys:
            if word in text:

                level = "Unknown"

                # 🧠 خدي سطر كامل فيه اللغة
                lines = text.split("\n")
                for line in lines:
                    if word in line:

                        if "c2" in line or "maternel" in line:
                            level = "C2"
                        elif "c1" in line:
                            level = "C1"
                        elif "b2" in line:
                            level = "B2"
                        elif "b1" in line:
                            level = "B1"
                        elif "a2" in line:
                            level = "A2"
                        elif "a1" in line:
                            level = "A1"

                results.append({
                    "name": lang,
                    "level": level
                })

                break

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
