import re

# -----------------------------
# EDUCATION
# -----------------------------

def extract_education(text):

    text = text.lower()

    if any(word in text for word in ["master", "bac+5", "ingenieur", "engineer"]):
        return "Bac+5"

    if any(word in text for word in [
        "licence",
        "bachelor",
        "3e annee",
        "3 eme annee",
        "3eme annee",
        "troisieme annee",
        "3rd year",
        "bac+3"
    ]):
        return "Bac+3"

    if any(word in text for word in ["bts", "dut", "bac+2"]):
        return "Bac+2"

    if "bac" in text or "baccalaureat" in text:
        return "Bac"

    return "Unknown"


# -----------------------------
# EXPERIENCE
# -----------------------------

months_map = {
    "janvier":1,"fevrier":2,"mars":3,"avril":4,"mai":5,"juin":6,
    "juillet":7,"aout":8,"septembre":9,"octobre":10,"novembre":11,"decembre":12,
    "january":1,"february":2,"march":3,"april":4,"may":5,"june":6,
    "july":7,"august":8,"september":9,"october":10,"november":11,"december":12
}


def extract_experience_months(text):

    text = text.lower()

    pattern = r"(janvier|fevrier|mars|avril|mai|juin|juillet|aout|septembre|octobre|novembre|decembre|january|february|march|april|may|june|july|august|september|october|november|december)\s*(\d{4}).*?(janvier|fevrier|mars|avril|mai|juin|juillet|aout|septembre|octobre|novembre|decembre|january|february|march|april|may|june|july|august|september|october|november|december)\s*(\d{4})"

    matches = re.findall(pattern, text)

    total_months = 0

    for match in matches:

        start_month = months_map[match[0]]
        start_year = int(match[1])

        end_month = months_map[match[2]]
        end_year = int(match[3])

        months = (end_year - start_year) * 12 + (end_month - start_month)

        if months > 0:
            total_months += months

    if total_months == 0 and "stage" in text:
        return 3

    return total_months


def extract_experience(text):

    months = extract_experience_months(text)

    return str(months) + " months"
