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
    total_months = 0
    
    months_map = {
        "janvier":1,"février":2,"mars":3,"avril":4,"mai":5,"juin":6,
        "juillet":7,"août":8,"septembre":9,"octobre":10,"novembre":11,"décembre":12
    }
    
    # السطاج الحالي
    if "stage" in text and ("actuellement" in text or "حاليا" in text):
        # لقا تاريخ البداية
        date_match = re.search(r'stage.*?([a-z]+)\s+(\d{4})', text)
        if date_match:
            month_name, year = date_match.groups()
            start_month = months_map.get(month_name, 1)
            start_date = datetime(int(year), start_month, 1)
            today = datetime.now()
            total_months = (today.year - start_date.year) * 12 + (today.month - start_date.month)
    
    # إذا ماعندوش تاريخ → 3 أشهر
    elif "stage" in text:
        total_months = 3
    
    return total_months

def extract_experience(text):
    months = extract_experience_months(text)
    return f"{months} mois"

# استخدام
cv_text = "3éme année de gestion. Stage actuellement depuis septembre 2024"

print("Formation:", extract_education(cv_text))  # Bac+3
print("Expérience:", extract_experience(cv_text))
