import streamlit as st
import pandas as pd

from reader import extract_text_from_pdf
from preprocess import preprocess_text

from features import extract_skills, extract_languages, extract_companies
from education_experience import extract_education, extract_experience_months
from ats_scoring import calculate_global_score


# -------------------------
# CONFIG
# -------------------------
st.set_page_config(page_title="AI CV Analyzer", page_icon="🤖", layout="wide")

st.title("🤖 AI CV Analyzer for HR")
st.write("Upload CVs and match them with a job (fiche de poste)")


# -------------------------
# JOB INPUT
# -------------------------
st.sidebar.title("🎯 Fiche de poste")

job_skills = st.sidebar.text_area("Required Skills", "recruitment, communication, HR")

job_education = st.sidebar.selectbox(
    "Required Education",
    ["Bac", "Bac+1", "Bac+2", "Bac+3", "Bac+5", "Doctorat"]
)

job_experience = st.sidebar.slider("Minimum Experience (months)", 0, 60, 12)

job_language = st.sidebar.selectbox("Language Level", ["A1","A2","B1","B2","C1","C2"])


# -------------------------
# UPLOAD
# -------------------------
uploaded_files = st.file_uploader("📄 Upload CVs (PDF)", type=["pdf"], accept_multiple_files=True)


# -------------------------
# PROCESS
# -------------------------
results = []

if uploaded_files:

    job_skills_list = [s.strip().lower() for s in job_skills.split(",")]

    for file in uploaded_files:

        text = extract_text_from_pdf(file)
        clean_text = preprocess_text(text)

        # Features
        experience_months = extract_experience_months(clean_text)
        education = extract_education(clean_text)
        skills = extract_skills(clean_text)
        languages = extract_languages(clean_text)
        
        companies = extract_companies(clean_text)

        # Global score
        data = {
            "skills": skills,
            "languages": languages,
            "education": education,
            "experience": experience_months
        }

        score = calculate_global_score(data)

        # -------------------------
        # MATCHING
        # -------------------------
        matching_score = 0

        matched_skills = set(skills).intersection(job_skills_list)
        matching_score += len(matched_skills) * 5

        # EDUCATION
        education_levels = {"Bac":1,"Bac+1":2,"Bac+2":3,"Bac+3":4,"Bac+5":5,"Doctorat":6}
        if education_levels.get(education,0) >= education_levels.get(job_education,0):
            matching_score += 20

        # EXPERIENCE
        if experience_months >= job_experience:
            matching_score += 20

        # LANGUAGE
        language_levels = {"A1":1,"A2":2,"B1":3,"B2":4,"C1":5,"C2":6}
        candidate_lang_level = 0

        for lang in languages:
            lvl = language_levels.get(lang["level"],0)
            if lvl > candidate_lang_level:
                candidate_lang_level = lvl

        if candidate_lang_level >= language_levels.get(job_language,0):
            matching_score += 20

        # STATUS
        status = "🟢 Good" if matching_score >= 60 else "🟡 Average" if matching_score >= 30 else "🔴 Weak"

        # SAVE
        results.append({
            "CV": file.name,
            "Matching Score": matching_score,
            "Education": education,
            "Experience (months)": experience_months,
            "Skills": ", ".join(skills),
            "Matched Skills": ", ".join(matched_skills),
            "Languages": ", ".join([f"{l['name']} ({l['level']})" for l in languages]),
            "Companies": len(companies),
            
            "Status": status
        })

    df = pd.DataFrame(results).sort_values(by="Matching Score", ascending=False)

    st.subheader("📊 Candidates Ranking")
    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Matching Score Chart")
    st.bar_chart(df.set_index("CV")["Matching Score"])

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Results (CSV)", csv, "candidates.csv", "text/csv")

    best = df.iloc[0]

    st.subheader("🏆 Best Candidate")
    st.success(f"{best['CV']} - Score: {best['Matching Score']}")

    st.write("### 🔍 Why selected?")
    st.write(f"""
    - Skills: {best['Skills']}
    - Experience: {best['Experience (months)']} months
    - Education: {best['Education']}
    - Languages: {best['Languages']}
    """)

else:
    st.info("⬆️ Upload CVs to start analysis")
