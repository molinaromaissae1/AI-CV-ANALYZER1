import re
from datetime import datetime


def extract_education(text):

    text = text.lower()

    if "phd" in text or "doctorat" in text:
        return "Bac+8"

    if "master" in text or "bac+5" in text:
        return "Bac+5"

    if "bac+4" in text:
        return "Bac+4"

    if "bac+3" in text or "licence" in text or "3ème année" in text:
        return "Bac+3"

    if "bac+2" in text or "bts" in text or "dut" in text:
        return "Bac+2"

    if "bac" in text:
        return "Bac"

    return "Unknown"



def extract_experience(text):

    text = text.lower()

    months = {
        "janvier":1,"février":2,"mars":3,"avril":4,"mai":5,"juin":6,
        "juillet":7,"août":8,"septembre":9,"octobre":10,"novembre":11,"décembre":12
    }

    pattern = r"(janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre)\s(\d{4})"

    matches = re.findall(pattern,text)

    if len(matches) >= 2:

        start_month,start_year = matches[0]
        end_month,end_year = matches[1]

        start_date = datetime(int(start_year),months[start_month],1)
        end_date = datetime(int(end_year),months[end_month],1)

        diff = (end_date.year-start_date.year)*12+(end_date.month-start_date.month)

        return f"{diff} months"

    return "0 months"
