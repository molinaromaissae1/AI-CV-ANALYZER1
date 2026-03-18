import streamlit as st
import pandas as pd

# -------------------------
# IMPORTS
# -------------------------
from reader import extract_text_from_pdf
from preprocess import preprocess_text

from features import (
    extract_skills,
    extract_languages,
    extract_companies,
    extract_sector
)

from education_experience import extract_education, extract_experience_months
from ats_scoring import calculate_global_score


# -------------------------
# CONFIG
# -------------------------
st.set_page_config(
    page_title="AI CV Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI CV Analyzer for HR")
st.write("Upload CVs and match them with a job (fiche de poste)")

# -------------------------
# FICHE DE POSTE (SIDEBAR)
# -------------------------
st.sidebar.title("🎯 Fiche de poste")

job_skills = st.sidebar.text_input(
    "Required Skills",
    "recruitment, communication, HR"
)

job_education = st.sidebar.selectbox(
    "Required Education",
    ["Bac", "Bac+2", "Bac+3", "Bac+5"]
)

job_experience = st.sidebar.slider(
    "Minimum Experience (months)",
    0, 60, 12
)

# -------------------------
# UPLOAD
# -------------------------
uploaded_files = st.file_uploader(
    "📄 Upload CVs (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

# -------------------------
# PROCESS
# -------------------------
results = []

if uploaded_files:

    job_skills_list = [s.strip().lower() for s in job_skills.split(",")]

    for file in uploaded_files:

        # 1. Extract text
        text = extract_text_from_pdf(file)
        clean_text = preprocess_text(text)

        # 2. Extract features
        experience_months = extract_experience_months(clean_text)
        education = extract_education(clean_text)
        skills = extract_skills(clean_text)
        languages = extract_languages(clean_text)
        sector = extract_sector(clean_text)
        companies = extract_companies(clean_text)

        # 3. Global score
        data = {
            "skills": skills,
            "languages": languages,
            "education": education,
            "experience": experience_months
        }

        score = calculate_global_score(data)

        # -------------------------
        # MATCHING (fiche de poste)
        # -------------------------
        matching_score = 0

        # Skills matching
        matching_score += len(set(skills).intersection(job_skills_list)) * 5

        # Experience matching
        if experience_months >= job_experience:
            matching_score += 20

        # Education matching
        if education == job_education:
            matching_score += 20

        # -------------------------
        # STATUS
        # -------------------------
        if matching_score >= 60:
            status = "🟢 Good"
        elif matching_score >= 30:
            status = "🟡 Average"
        else:
            status = "🔴 Weak"

        # -------------------------
        # SAVE RESULT
        # -------------------------
        results.append({
            "CV": file.name,
            "Score": score,
            "Matching Score": matching_score,
            "Status": status,
            "Education": education,
            "Experience (months)": experience_months,
            "Skills": len(skills),
            "Languages": len(languages),
            "Companies": len(companies),
            "Sector": sector
        })

    # -------------------------
    # TABLE
    # -------------------------
    df = pd.DataFrame(results)
    df = df.sort_values(by="Matching Score", ascending=False)

    # Colors
    def color_status(val):
        if "Good" in val:
            return "background-color: lightgreen"
        elif "Average" in val:
            return "background-color: khaki"
        else:
            return "background-color: lightcoral"

    styled_df = df.style.applymap(color_status, subset=["Status"])

    st.subheader("📊 Candidates Ranking")
    st.dataframe(styled_df, use_container_width=True)

    # -------------------------
    # BEST CANDIDATE
    # -------------------------
    best = df.iloc[0]

    st.subheader("🏆 Best Candidate")

    if best["Matching Score"] >= 60:
        st.success(f"{best['CV']} - Excellent Match ({best['Matching Score']})")
    elif best["Matching Score"] >= 30:
        st.warning(f"{best['CV']} - Medium Match ({best['Matching Score']})")
    else:
        st.error(f"{best['CV']} - Weak Match ({best['Matching Score']})")

else:
    st.info("⬆️ Upload CVs to start analysis")
