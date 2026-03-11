import re

def extract_features(text):

    features = {}

    exp = re.findall(r"\d+ years", text)

    if exp:
        features["experience"] = int(exp[0].split()[0])
    else:
        features["experience"] = 0

    if "phd" in text:
        features["education"] = "phd"

    elif "master" in text or "bac+5" in text:
        features["education"] = "master"

    elif "bachelor" in text or "bac+3" in text:
        features["education"] = "bachelor"

    else:
        features["education"] = "unknown"

    skills = [
        "python",
        "machine learning",
        "data analysis",
        "excel",
        "sql",
        "project management"
    ]

    found = []

    for s in skills:

        if s in text:
            found.append(s)

    features["skills"] = found

    languages = []

    if "english" in text:
        languages.append("English")

    if "french" in text:
        languages.append("French")

    if "arabic" in text:
        languages.append("Arabic")

    features["languages"] = languages

    features["companies"] = text.count("company")

    return features
