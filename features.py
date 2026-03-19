import re

# =========================
# SKILLS
# =========================
def extract_skills(text):
    skills_list = [
        "python", "excel", "communication", "management",
        "recruitment", "hr", "powerpoint", "word",
        "organisation", "gestion", "teamwork"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# =========================
# LANGUAGES
# =========================
def extract_languages(text):
    text = text.lower()

    languages_list = {
        "english": ["english", "anglais"],
        "french": ["french", "français"],
        "arabic": ["arabic", "arabe"],
        "spanish": ["spanish", "espagnol", "espagnole"]
    }

    level_mapping = {
        "a1": "A1", "a2": "A2",
        "b1": "B1", "b2": "B2",
        "c1": "C1", "c2": "C2",
        "intermediate": "B1",
        "fluent": "C1",
        "courant": "C1"
    }

    results = []

    for lang, keywords in languages_list.items():
        for word in keywords:
            if word in text:

                level = "Unknown"

                # 🔍 نبحث على المستوى قريب من الكلمة
                for lvl in level_mapping:
                    if word + " " + lvl in text or lvl + " " + word in text:
                        level = level_mapping[lvl]

                # 🔥 maternel
                if "maternel" in text or "native" in text:
                    if word in text:
                        level = "C2"

                results.append({
                    "name": lang.capitalize(),
                    "level": level
                })
                break

    return results
   

          


# =========================
# COMPANIES
# =========================
def extract_companies(text):
    companies = [
        "safran", "deloitte", "capgemini", "google",
        "amazon", "microsoft", "apple"
    ]

    text = text.lower()
    found = []

    for c in companies:
        if c in text:
            found.append(c)

    return found


# =========================
# SECTOR
# =========================
def extract_sector(text):
    text = text.lower()

    if "hr" in text or "ressources humaines" in text:
        return "HR"
    elif "finance" in text:
        return "Finance"
    elif "engineering" in text:
        return "Engineering"
    else:
        return "Other"
