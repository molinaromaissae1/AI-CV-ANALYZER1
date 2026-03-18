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
# FICHE DE POSTE
# -------------------------
st.sidebar.title("🎯 Fiche de poste")

job_skills = st.sidebar.text_area(
    "Required Skills",
    "recruitment, communication, HR"
)

job_education = st.sidebar.selectbox(
    "Required Education",
    ["Bac", "Bac+1", "Bac+2", "Bac+3", "Bac+5", "Doctorat"]
)

job_experience = st.sidebar.slider(
    "Minimum Experience (months)",
    0, 60, 12
)

job_language = st.sidebar.selectbox(
    "Language Level",
    ["A1", "A2", "B1", "B2", "C1", "C2"]
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
        if not isinstance(skills, list):
            skills = []

        languages = extract_languages(clean_text)
        if not isinstance(languages, list):
            languages = []

        sector = extract_sector(clean_text)

        companies = extract_companies(clean_text)
        if not isinstance(companies, list):
            companies = []

        # 3. Global score
        data = {
            "skills": skills,
            "languages": languages,
            "education": education,
            "experience": experience_months
        }

        score = calculate_global_score(data)

        # -------------------------
        # MATCHING SMART
        # -------------------------
        matching_score = 0

        # SKILLS
        matched_skills = set(skills).intersection(job_skills_list)
        matching_score += len(matched_skills) * 5

        if len(matched_skills) >= len(job_skills_list) / 2:
            matching_score += 10

        # EDUCATION
        education_levels = {
            "Bac": 1,
            "Bac+1": 2,
            "Bac+2": 3,
            "Bac+3": 4,
            "Bac+5": 5,
            "Doctorat": 6
        }

        candidate_level = education_levels.get(education, 0)
        required_level = education_levels.get(job_education, 0)

        if candidate_level >= required_level:
            matching_score += 20
        elif candidate_level == required_level - 1:
            matching_score += 10

        # EXPERIENCE
        if experience_months >= job_experience:
            matching_score += 20
        elif experience_months >= job_experience / 2:
            matching_score += 10

        # LANGUAGE
        language_levels = {
            "A1": 1, "A2": 2,
            "B1": 3, "B2": 4,
            "C1": 5, "C2": 6
        }

        candidate_lang_level = 0

        for lang in languages:
            if isinstance(lang, str):
                lvl = language_levels.get(lang.upper(), 0)
                if lvl > candidate_lang_level:
                    candidate_lang_level = lvl

        required_lang_level = language_levels.get(job_language, 0)

        if candidate_lang_level >= required_lang_level:
            matching_score += 20
        elif candidate_lang_level == required_lang_level - 1:
            matching_score += 10

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
            "Matched Skills": len(matched_skills),
            "Languages": len(languages),
            "Companies": len(companies),
            "Sector": sector
        })

    # -------------------------
    # TABLE
    # -------------------------
    df = pd.DataFrame(results)
    df = df.sort_values(by="Matching Score", ascending=False)

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
    # GRAPH 📈
    # -------------------------
    st.subheader("📈 Matching Score Chart")
    st.bar_chart(df.set_index("CV")["Matching Score"])

    # -------------------------
    # DOWNLOAD CSV 📥
    # -------------------------
    csv = df.to_csv(index=False).encode('utf-8')

    st.download_button(
        "📥 Download Results (CSV)",
        csv,
        "candidates.csv",
        "text/csv"
    )

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

    # -------------------------
    # WHY SELECTED 🔍
    # -------------------------
    st.write("### 🔍 Why selected?")

    st.write(f"""
    - Matched Skills: {best['Matched Skills']}
    - Experience: {best['Experience (months)']} months
    - Education: {best['Education']}
    - Languages: {best['Languages']}
    """)

else:
    st.info("⬆️ Upload CVs to start analysis")
