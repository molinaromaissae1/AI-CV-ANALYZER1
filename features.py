import re


# -----------------------
# EXPERIENCE
# -----------------------

def extract_experience(text):

    text = text.lower()

    experience = 0

    # stage
    if "stage" in text or "stagiaire" in text:
        experience += 1

    # chercher années
    years = re.findall(r'20\d{2}', text)

    if len(years) >= 2:
        experience += 1

    return experience


# -----------------------
# EDUCATION
# -----------------------

def extract_education(text):

    text = text.lower()

    if "bac+5" in text or "master" in text:
        return "Bac+5"

    if "bac+3" in text or "licence" in text or "3e année" in text:
        return "Bac+3"

    if "bac+2" in text or "bts" in text or "dut" in text or "2e année" in text:
        return "Bac+2"

    if "bac" in text or "baccalauréat" in text:
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
# SKILLS (RH)
# -----------------------

def extract_skills(text):

    text = text.lower()

    skills_list = [

    # RH
    "ressources humaines",
    "recrutement",
    "gestion du personnel",
    "administration du personnel",
    "gestion des talents",

    # administratif
    "gestion administrative",
    "gestion des dossiers",
    "saisie de données",

    # soft skills
    "communication",
    "travail d'équipe",
    "leadership",
    "organisation",

    # bureautique
    "excel",
    "word",
    "powerpoint",
    "power point",
    "outlook"
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

    if "ressources humaines" in text or "rh" in text:
        return "Ressources Humaines"

    if "gestion" in text:
        return "Gestion / Administration"

    return "Unknown"


# -----------------------
# COMPANIES
# -----------------------

def extract_companies(text):

    years = re.findall(r'20\d{2}', text)

    return max(0, len(years)//2)
