import streamlit as st
from reader import read_cv
from ats_scoring import score_cv

st.title("AI CV Screening Agent")

uploaded_file = st.file_uploader("Upload CV", type=["pdf", "docx"])

if uploaded_file is not None:

    text = read_cv(uploaded_file)
st.subheader("Text detected in CV")
st.write(text)
    st.subheader("Extracted Information")

    experience, education, skills, languages = score_cv(text)

    st.write("Experience:", experience)
    st.write("Education:", education)
    st.write("Skills:", skills)
    st.write("Languages:", languages)

    score = experience*2 + education*2 + skills*3 + languages

    st.subheader("ATS Score")
    st.write(score)

    if score > 10:
        st.success("Candidate Selected")
    else:
        st.error("Candidate Rejected")
