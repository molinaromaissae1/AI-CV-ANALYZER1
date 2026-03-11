def score_cv(text):

    experience = text.lower().count("experience")
    education = text.lower().count("university") + text.lower().count("master") + text.lower().count("bachelor")
    skills = text.lower().count("python") + text.lower().count("excel") + text.lower().count("data")
    languages = text.lower().count("english") + text.lower().count("french")

    return experience, education, skills, languages
