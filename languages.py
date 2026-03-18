import re

# 🌍 List of known languages
LANGUAGES = [
    "français", "anglais", "arabe", "espagnol", "allemand",
    "italien", "portugais", "chinois", "japonais",
    "coréen", "russe", "turc", "néerlandais"
]

# 🎯 Levels mapping
LEVEL_SCORES = {
    "A1": 2, "A2": 4,
    "B1": 6, "B2": 8,
    "C1": 10, "C2": 12,
    "courant": 10,
    "avancé": 9,
    "intermédiaire": 6,
    "débutant": 3,
    "bilingue": 14,
    "natif": 14,
    "langue maternelle": 14
}


def extract_languages(text):
    text = text.lower()
    results = []

    for lang in LANGUAGES:
        if lang in text:
            level = None

            # search CEFR levels (A1, B2...)
            match = re.search(rf"{lang}[^a-zA-Z0-9]*(a1|a2|b1|b2|c1|c2)", text)
            if match:
                level = match.group(1).upper()
            else:
                # search other keywords
                for lvl in LEVEL_SCORES.keys():
                    if lvl in text:
                        level = lvl
                        break

            results.append({
                "language": lang.capitalize(),
                "level": level if level else "Unknown",
                "score": LEVEL_SCORES.get(level, 5)
            })

    return results
