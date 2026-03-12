def calculate_ats_score(experience, skills, languages, education):

    score = 0

    # experience
    score += experience * 20

    # skills
    score += len(skills) * 5

    # languages
    score += len(languages) * 5

    # education
    if education == "Bac+5":
        score += 20
    elif education == "Bac+3":
        score += 15
    elif education == "Bac+2":
        score += 10
    else:
        score += 5

    if score > 100:
        score = 100

    return score
