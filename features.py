import re


# EDUCATION
def extract_education(text):

    text = text.lower()

    if "master" in text or "bac+5" in text:
        return "Bac+5"

    if "licence" in text or "bac+3" in text:
        return "Bac+3"

    if "3e année" in text or "3eme annee" in text or "3ème année" in text:
        return "Bac+3"

    if "bts" in text or "dut" in text or "bac+2" in text:
        return "Bac+2"

    if "baccalauréat" in text or "bac" in text:
        return "Bac"

    return "Unknown"



# EXPERIENCE
def extract_experience(text):

    years = re.findall(r"20\d{2}", text)

    if len(years) < 2:
        return 0

    first = int(years[0])
    last = int(years[-1])

    exp = last - first

    if exp == 0:
        exp = 1

    return exp



# SKILLS
def extract_skills(text):

    text = text.lower()

    skills = [
        "ressources humaines",
        "gestion administrative",
        "saisie de données",
        "communication",
        "organisation",
        "excel",
        "word",
        "powerpoint"
    ]

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    return found



# LANGUAGES
def extract_languages(text):

    text = text.lower()

    languages = []

    if "français" in text or "francais" in text:
        languages.append("Français")

    if "anglais" in text:
        languages.append("Anglais")

    if "arabe" in text:
        languages.append("Arabe")

    return languages



# SECTOR
def extract_sector(text):

    text = text.lower()

    if "ressources humaines" in text or "rh" in text:
        return "Ressources Humaines"

    return "General"



# COMPANIES
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
