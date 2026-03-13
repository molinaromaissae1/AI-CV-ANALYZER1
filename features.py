import re

# ==========================
# EDUCATION LEVEL
# ==========================

def extract_education(text):

    text = text.lower()

    if "phd" in text or "doctorat" in text:
        return "Bac+8"

    if "master" in text or "bac+5" in text:
        return "Bac+5"

    if "5eme" in text or "5ème" in text:
        return "Bac+5"

    if "4eme" in text or "4ème" in text:
        return "Bac+4"

    if "licence" in text or "bac+3" in text or "3eme" in text or "3ème" in text:
        return "Bac+3"

    if "bac+2" in text or "dut" in text or "bts" in text:
        return "Bac+2"

    if "bac" in text:
        return "Bac"

    return "Unknown"

# ==========================
# EXPERIENCE
# ==========================

def extract_experience(text):

    text = text.lower()

    if "stage" in text or "expérience" in text or "experience" in text:
        return 1

    return 0


# ==========================
# SKILLS
# ==========================

def extract_skills(text):

    text = text.lower()

    skills_list = [
        "ressources humaines",
        "gestion administrative",
        "gestion des dossiers",
        "saisie de données",
        "communication",
        "organisation",
        "travail d'équipe",
        "excel",
        "word",
        "powerpoint"
    ]

    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found


# ==========================
# LANGUAGES
# ==========================

def extract_languages(text):

    text = text.lower()

    languages = []

    if "français" in text or "francais" in text:
        languages.append("Français")

    if "anglais" in text or "english" in text:
        languages.append("Anglais")

    if "arabe" in text or "arabic" in text:
        languages.append("Arabe")

    return languages


# ==========================
# SECTOR
# ==========================

def extract_sector(text):

    text = text.lower()

    if "ressources humaines" in text or "rh" in text:
        return "Ressources Humaines"

    return "General"


# ==========================
# COMPANIES
# ==========================

def extract_companies(text):

    text = text.lower()

    keywords = [
        "stage",
        "intern",
        "secrétaire",
        "assistant",
        "responsable",
        "manager",
        "syndicat",
        "entreprise",
        "company"
    ]

    count = 0

    for word in keywords:
        if word in text:
            count += 1

    if count > 1:
        count = 1

    return count
# -------------------------
# SECTOR
# -------------------------

def extract_sector(text):

    text = text.lower()

    if "ressources humaines" in text or "rh" in text:
        return "Ressources Humaines"

    if "finance" in text:
        return "Finance"

    if "marketing" in text:
        return "Marketing"

    if "data" in text or "analyse" in text:
        return "Data"
    
    return "General"
