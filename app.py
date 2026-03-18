import streamlit as st

st.title("College Advisor")

gpa = st.number_input("Enter your GPA", min_value=0.0, max_value=4.0, step=0.1)
sat = st.number_input("Enter your SAT score", min_value=400, max_value=1600, step=10)

if st.button("Get Recommendation"):
    if gpa >= 3.8 and sat >= 1450:
        st.write("Reach: Top 20 schools")
    elif gpa >= 3.5:
        st.write("Match: Strong state schools")
    else:
        st.write("Safety: Build a balanced list")