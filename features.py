import re

# -----------------------
# EXPERIENCE
# -----------------------

def extract_experience(text):

    years = re.findall(r'\b\d+\s*(ans|an)\b', text.lower())

    return len(years)


# -----------------------
# EDUCATION
# -----------------------

def extract_education(text):

    text = text.lower()

    if "bac+5" in text:
        return "Bac+5"

    if "bac+3" in text:
        return "Bac+3"

    if "bac+2" in text:
        return "Bac+2"

    if "bac" in text:
        return "Bac"

    return "Unknown"


# -----------------------
# LANGUAGES
# -----------------------

def extract_languages(text):

    text = text.lower()

    languages_list = [
        "français",
        "francais",
        "anglais",
        "english",
        "arabe",
        "arabic"
    ]

    found = []

    for lang in languages_list:
        if lang in text:
            found.append(lang)

    return found


# -----------------------
# SKILLS
# -----------------------

def extract_skills(text):

    text = text.lower()

    skills_list = [
        "python",
        "excel",
        "power bi",
        "sql",
        "gestion",
        "administrative",
        "communication",
        "analyse",
        "data"
    ]

    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found


# -----------------------
# SECTOR
# -----------------------

def extract_sector(text):

    text = text.lower()

    sectors = [
        "informatique",
        "data",
        "finance",
        "marketing",
        "administration",
        "industrie"
    ]

    found = []

    for s in sectors:
        if s in text:
            found.append(s)

    return found


# -----------------------
# COMPANIES
# -----------------------

def extract_companies(text):

    years = re.findall(r'20\d{2}', text)

    return max(0, len(years)//2)
