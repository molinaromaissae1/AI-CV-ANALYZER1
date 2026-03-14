import re

def extract_education(text):

    text = text.lower()

    if "master" in text or "bac+5" in text or "ingenieur" in text:
        return "Bac+5"

    if ("licence" in text 
        or "3e annee" in text
        or "3 eme annee" in text
        or "3eme annee" in text
        or "troisieme annee" in text
        or "bac+3" in text):
        return "Bac+3"

    if "bts" in text or "dut" in text or "bac+2" in text:
        return "Bac+2"

    if "bac" in text or "baccalaureat" in text:
        return "Bac"

    return "Unknown"


# ------------------------

months = {
    "janvier":1,"fevrier":2,"mars":3,"avril":4,"mai":5,"juin":6,
    "juillet":7,"aout":8,"septembre":9,"octobre":10,"novembre":11,"decembre":12
}

def extract_experience_months(text):

    text = text.lower()

    pattern = r"(janvier|fevrier|mars|avril|mai|juin|juillet|aout|septembre|octobre|novembre|decembre).*?(janvier|fevrier|mars|avril|mai|juin|juillet|aout|septembre|octobre|novembre|decembre)"

    match = re.search(pattern,text)

    if match:

        start = months[match.group(1)]
        end = months[match.group(2)]

        diff = end - start

        if diff <= 0:
            diff = 1

        return diff

    if "stage" in text:
        return 3

    return 0


def extract_experience(text):

    months = extract_experience_months(text)

    return str(months) + " months"
