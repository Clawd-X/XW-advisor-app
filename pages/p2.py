import streamlit as st
import google.genai as genai

st.title("✍️ Short Answer Helper")

prompt = st.text_area("Paste your essay or short answer:")

if st.button("Improve / Get Feedback"):
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content(
        f"Give feedback on this college essay:\n\n{prompt}"
    )

    st.write(response.text)