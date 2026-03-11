def ats_score(features):

    score = 0

    if features["experience"] >= 5:
        score += 30

    elif features["experience"] >= 2:
        score += 20

    if features["education"] == "phd":
        score += 25

    elif features["education"] == "master":
        score += 20

    elif features["education"] == "bachelor":
        score += 10

    score += len(features["skills"]) * 10

    score += len(features["languages"]) * 5

    if features["companies"] >= 3:
        score += 10

    if score >= 70:
        decision = "Selected"

    elif score >= 40:
        decision = "Maybe"

    else:
        decision = "Rejected"

    return score, decision
