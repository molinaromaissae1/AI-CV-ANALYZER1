import re

# =========================
# SKILLS
# =========================
def extract_skills(text):
    skills_list = [
        "python", "excel", "communication", "management",
        "recruitment", "hr", "powerpoint", "word",
        "organisation", "gestion", "analysis"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


# =========================
# LANGUAGES (SMART VERSION)
# =========================
def extract_languages(text):
    text = text.lower()

    languages_list = {
        "English": ["english", "anglais"],
        "French": ["french", "français"],
        "Arabic": ["arabic", "arabe"],
        "Spanish": ["spanish", "espagnol", "espagnole"]
    }

    levels = ["a1", "a2", "b1", "b2", "c1", "c2"]

    results = []

    for lang, keywords in languages_list.items():
        for word in keywords:
            if word in text:

                level = "Unknown"

                index = text.find(word)

                # 🎯 context صغير باش مايتخلطوش اللغات
                context = text[max(0, index-15): index+15]

                # 🔍 detect level
                for lvl in levels:
                    if lvl in context:
                        level = lvl.upper()

                # 🔥 maternel فقط إذا ماكان حتى level
                if ("maternel" in context or "native" in context) and level == "Unknown":
                    level = "C2"

                results.append({
                    "name": lang,
                    "level": level
                })

                break

    return results


# =========================
# COMPANIES
# =========================
def extract_companies(text):
    companies = [
        "safran", "airbus", "deloitte", "pwc", "ey",
        "capgemini", "accenture", "atos"
    ]

    text = text.lower()
    found = []

    for company in companies:
        if company in text:
            found.append(company.capitalize())

    return found


# =========================
# EXPERIENCE (months)
# =========================
def extract_experience(text):
    matches = re.findall(r'(\d+)\s*(year|years|month|months)', text.lower())

    total_months = 0

    for num, unit in matches:
        num = int(num)

        if "year" in unit:
            total_months += num * 12
        else:
            total_months += num

    return total_months
