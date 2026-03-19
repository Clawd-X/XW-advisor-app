import streamlit as st

st.set_page_config(
    page_title="debug world",
    layout="wide"
)

st.title("Main Title")
st.header("Header")
st.subheader("Subheader")
st.text("Plain text")
st.markdown("**bold** _italic_")
st.write("Anything (text, variables, etc.)")
gpa = st.slider("GPA", 0.0, 4.0, 3.5, 0.1)
sat = st.number_input("SAT", 400, 1600, 1200)
name = st.text_input("Your name")
essay = st.text_area("Paste your essay")
if st.button("Submit"):
    st.write("Clicked!")
rigor = st.toggle("Took AP classes?")
ecs = st.selectbox("Extracurricular level", ["Low", "Medium", "High"])
choice = st.radio("Pick one", ["A", "B", "C"])
majors = st.multiselect("Intended majors", ["CS", "Bio", "Business"])
col1, col2 = st.columns(2)

with col1:
    st.slider("GPA", 0.0, 4.0)

with col2:
    st.slider("SAT", 400, 1600)
with st.container():
    st.write("Grouped content")
st.divider()
st.success("Good result")
st.warning("Be careful")
st.error("Something broke")
st.info("FYI")
st.json({"gpa": 3.9, "sat": 1450})
data = {
    "School": ["UCLA", "Stanford", "UC Davis"],
    "Category": ["Match", "Reach", "Safety"],
    "Acceptance Rate": ["8%", "4%", "49%"]
}
st.table(data)
st.dataframe(data)
if st.button("Run"):
    st.write("Processing...")
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(st.session_state.count)

def play_sound():
    st.markdown("""
        <audio autoplay>
        <source src="https://www.soundjay.com/buttons/sounds/button-16.mp3" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

if st.button("Submit"):
    play_sound()
    st.success("Submitted!")