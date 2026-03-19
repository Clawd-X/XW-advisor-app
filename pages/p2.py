import streamlit as st
import google.generativeai as genai

st.title("✍️ Short Answer Helper")

if not st.session_state.get("submitted"):
    st.warning("Please complete the form first.")
    st.stop()

name = st.session_state.get("name", "Not stated")
majors = st.session_state.get("majors", "Not stated")
budget = st.session_state.get("budget", "Not stated")
interests = st.session_state.get("interests", "Not stated")
school_size = st.session_state.get("school_size", "Not stated")
location = st.session_state.get("location", "Not stated")

if st.button("Improve / Get Feedback"):
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-pro")

response = model.generate_content(
    f"""
    You are a college admissions advisor.

    Student profile:
    - Name: {name}
    - Intended majors: {majors}
    - Budget: {budget}
    - Interests: {interests}
    - Preferred school size: {school_size}
    - Location preference: {location}

    Task:
    - Recommend 5 colleges
    - For each, explain WHY it fits
    - Categorize as Reach, Match, or Safety

    If key information is missing, briefly say what’s missing before answering.
    """
    )

st.write(response.text)