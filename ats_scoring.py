def calculate_global_score(data):
    
    # Extract data
    experience = data.get("experience", 0)
    skills = data.get("skills", [])
    languages = data.get("languages", [])
    education = data.get("education", "")

    score = 0

    # -------------------------
    # EXPERIENCE (max 20)
    # -------------------------
    score += min(experience * 2, 20)

    # -------------------------
    # SKILLS (max ~30)
    # -------------------------
    score += len(skills) * 3

    # -------------------------
    # LANGUAGES (max ~30)
    # -------------------------
    score += len(languages) * 3

    # -------------------------
    # EDUCATION
    # -------------------------
    if education == "Bac+5":
        score += 20
    elif education == "Bac+3":
        score += 15
    elif education == "Bac+2":
        score += 10
    elif education == "Bac+1":
        score += 8
    elif education == "Bac":
        score += 5
    else:
        score += 3

    # -------------------------
    # LIMIT SCORE
    # -------------------------
    return min(score, 100)
