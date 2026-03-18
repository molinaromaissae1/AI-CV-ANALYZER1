import re

# -------------------------
# SKILLS
# -------------------------
def extract_skills(text):
    skills_list = [
        "python", "excel", "communication", "management",
        "recruitment", "hr", "powerpoint", "word"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


# -------------------------
# LANGUAGES
# -------------------------
def extract_languages(text):
    text = text.lower()
    languages = []

    if "anglais" in text or "english" in text:
        languages.append("English")

    if "français" in text or "french" in text:
        languages.append("French")

    if "arabe" in text or "arabic" in text:
        languages.append("Arabic")

    if "espagnol" in text or "spanish" in text:
        languages.append("Spanish")

    return languages


# -------------------------
# COMPANIES
# -------------------------
def extract_companies(text):
    words = text.split()
    companies = []

    for word in words:
        if word.istitle():
            companies.append(word)

    return list(set(companies))


# -------------------------
# SECTOR
# -------------------------
def extract_sector(text):
    text = text.lower()

    if "finance" in text:
        return "Finance"
    elif "hr" in text or "ressources humaines" in text:
        return "HR"
    elif "engineering" in text or "industrial" in text:
        return "Engineering"

    return "Unknown"
