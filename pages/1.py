import streamlit as st

st.title("📊 Stats-Based College Advisor")

col1, col2 = st.columns(2)

with col1:
    gpa = st.slider("GPA", 0.0, 4.0, 3.5)

with col2:
    sat = st.slider("SAT", 400, 1600, 1200)

# gpa = st.slider("GPA", 0.0, 4.0, 3.5, 0.1)
# sat = st.slider("SAT Score", 400, 1600, 1200, 10)

rigor = st.toggle("Took rigorous courses (AP/IB)?")
ecs = st.selectbox("Extracurricular strength", ["Low", "Medium", "High"])

if st.button("Get Recommendations"):
    score = gpa * 100 + sat

    if rigor:
        score += 50
    if ecs == "High":
        score += 100

    if score > 1500:
        st.success("Reach: Top 20 schools")
    elif score > 1300:
        st.info("Match: Strong universities")
    else:
        st.warning("Safety: Build a balanced list")