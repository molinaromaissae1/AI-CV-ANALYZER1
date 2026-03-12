import re

# -----------------------------
# EDUCATION LEVEL
# -----------------------------
def extract_education(text):

    text = text.lower()

    if "bac+5" in text or "master" in text:
        return "Bac+5"

    if "bac+3" in text or "licence" in text or "3e année" in text or "3eme annee" in text:
        return "Bac+3"

    if "bac+2" in text or "dut" in text or "bts" in text:
        return "Bac+2"

    if "bac" in text or "baccalauréat" in text or "baccalaureat" in text:
        return "Bac"

    return "Unknown"


# -----------------------------
# EXPERIENCE (years)
# -----------------------------
def extract_experience(text):

    years = re.findall(r"20\d{2}", text)

    if len(years) >= 2:
        first = int(years[0])
        last = int(years[-1])

        exp = last - first

        if exp < 0:
            exp = 0

        return exp

    return 0


# -----------------------------
# SKILLS
# -----------------------------
def extract_skills(text):

    text = text.lower()

    skills_list = [

        # RH
        "ressources humaines",
        "gestion administrative",
        "recrutement",
        "gestion des dossiers",
        "saisie de données",
        "communication",
        "travail d'équipe",

        # bureautique
        "excel",
        "word",
        "powerpoint",

        # soft skills
        "organisation",
        "analyse",
        "gestion",
        "leadership"

    ]

    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found


# -----------------------------
# LANGUAGES
# -----------------------------
def extract_languages(text):

    text = text.lower()

    languages = []

    if "français" in text or "francais" in text:
        languages.append("français")

    if "anglais" in text or "english" in text:
        languages.append("anglais")

    if "arabe" in text or "arabic" in text:
        languages.append("arabe")

    return languages


# -----------------------------
# SECTOR
# -----------------------------
def extract_sector(text):

    text = text.lower()

    if "ressources humaines" in text or "rh" in text:
        return "Ressources Humaines"

    if "marketing" in text:
        return "Marketing"

    if "finance" in text:
        return "Finance"

    return "General"


# -----------------------------
# NUMBER OF COMPANIES
# -----------------------------
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

    return count
