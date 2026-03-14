import re
from datetime import datetime
def extract_education(text):

    text = text.lower()

    # Bac+5
    if re.search(r'master|ingenieur|bac\s*\+\s*5', text):
        return "Bac+5"

    # Bac+3
    if re.search(r'3e|3eme|3ème|troisième|licence|bachelor|année de gestion|l3', text):
        return "Bac+3"

    # Bac+2
    if re.search(r'bts|dut|bac\s*\+\s*2', text):
        return "Bac+2"

    # Bac
    if re.search(r'\bbaccalauréat\b', text):
        return "Bac"

    return "Unknown"

   

def extract_experience_months(text):

    text = text.lower()

    months = {
        "janvier":1,"février":2,"mars":3,"avril":4,"mai":5,"juin":6,
        "juillet":7,"août":8,"septembre":9,"octobre":10,"novembre":11,"décembre":12
    }

   pattern = r"(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s*(\d{4}).*?(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s*(\d{4})"

    match = re.search(pattern, text)

    if match:

        start_month = months[match.group(1)]
        start_year = int(match.group(2))

        end_month = months[match.group(3)]
        end_year = int(match.group(4))

        total_months = (end_year - start_year) * 12 + (end_month - start_month)

        if total_months <= 0:
            total_months = 1

        return total_months

    if "stage" in text:
        return 3

    return 0
   


print("Formation:", extract_education(cv_text))  # Bac+3
print("Expérience:", extract_experience(cv_text))
