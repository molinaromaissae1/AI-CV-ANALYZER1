import streamlit as st
from reader import extract_text_from_pdf
from preprocess import preprocess_text

from features import (
    extract_skills,
    extract_languages,
    extract_companies,
    extract_sector
)

from education_experience import extract_education, extract_experience_months
st.set_page_config(
    page_title="AI CV Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI CV Analyzer for HR")
st.write("Upload a CV and the system will analyze it automatically.")

uploaded_file = st.file_uploader(
    "📄 Upload CV (PDF)",
    type=["pdf"]
)



if uploaded_file is not None:

    text = extract_text_from_pdf(uploaded_file)

    clean_text = preprocess_text(text)
    st.subheader("DEBUG TEXT")
    st.write(clean_text[:1500])
    
    experience_months = extract_experience_months(clean_text)

    education = extract_education(clean_text)
    skills = extract_skills(clean_text)
    languages = extract_languages(clean_text)
    sector = extract_sector(clean_text)
    companies = extract_companies(clean_text)

    st.subheader("📊 Extracted Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Experience Duration", experience_months)
        st.metric("Education Level", education)

    with col2:
        st.metric("Sector", sector)
        st.metric("Companies", companies)

    st.subheader("💼 Skills")

    for skill in skills:
        st.success(skill)

    st.subheader("🌍 Languages")

    for lang in languages:
        st.info(lang)

    # -----------------
    # ATS SCORE
    # -----------------

    score = 0

    score += min(experience_months * 5, 20)
    score += len(skills) * 5
    score += len(languages) * 5

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

    st.subheader("📈 ATS Score")

    st.progress(score)

    st.write("Score:", score)

    if score > 70:
        st.success("🟢 Good Candidate")
# update
    elif score >= 40:
        st.warning("🟡 Average Candidate")

    else:
        st.error("🔴 Weak Candidate")
