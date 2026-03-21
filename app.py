import streamlit as st
from google import genai

st.set_page_config(page_title="College Advisor", layout="wide")

st.title("College Advisor App")
st.header("Enter information below to get started!")
st.divider()

st.header("Lets get to know you! ")

name_input = st.text_input("What's your name? (optional)", key="name_input")
name = name_input.strip()

# Initialize state
if "step" not in st.session_state:
    st.session_state.step = 0

if st.button("Confirm", key="confirm_name"):
    st.session_state.step = 1


# Reveal section AFTER click
if st.session_state.step >= 1:
    st.divider()

    display_name = name_input.strip() or "User"
    st.session_state["name"] = display_name

    st.header(f"Hello, {display_name}! 👋")
    st.write("Now let's find your perfect colleges...")
    st.subheader("Your Preferences")

    col1, col2 = st.columns(2)
    with col1:
        gpa = st.slider(
        "Current Unweighted GPA", 
        min_value=0.0, 
        max_value=4.0, 
        value=3.5, 
        step=0.1,
        help="Slide to your current GPA"
    )
        sat_score = st.slider(
        "SAT Score 📝",
        min_value=0,
        max_value=1600,
        value=1200,
        step=10,
        help="Slide to 0 if unapplicable"
    )
    with col2:
        rigor = st.select_slider("Coursework Rigor", options=["Standard", "Honors", "AP/IB Heavy", "Most Rigorous Available"])
        
    extracurriculars = st.text_area("Extracurriculars, Leadership, & Awards", placeholder="e.g., Varsity Soccer Captain, Robotics State Champ, 100+ Volunteer Hours")

    # 2. Majors
    majors = st.multiselect(
        "Intended Major(s)",
        [
            "Computer Science", "Data Science", "Cybersecurity", 
            "Mechanical Engineering", "Electrical Engineering", "Biomedical Engineering",
            "Biology", "Pre-Med", "Nursing", "Psychology", "Neuroscience",
            "Business Administration", "Finance", "Marketing", "Economics",
            "Political Science", "International Relations", "Pre-Law",
            "Architecture", "Graphic Design", "Film & Media",
            "English Literature", "History", "Philosophy", "Education"
        ],
        key="majors"
    )

    # 3. Budget & Financial Aid
    budget = st.selectbox(
        "Budget & Financial Needs",
        [
            "Full Financial Aid Required", 
            "Seeking Merit Scholarships", 
            "$20k–$40k per year", 
            "$40k–$60k per year", 
            "$60k–$80k per year", 
            "No Budget Preference"
        ],
        key="budget"
    )

    # 4. Interests & Hobbies
    interests = st.multiselect(
        "Personal Interests & Hobbies",
        [
            "Undergraduate Research", "Study Abroad Programs", "Greek Life (Frats/Sororities)",
            "D1 Sports / School Spirit", "Intramural Sports", "Performing Arts / Theater",
            "Social Justice & Activism", "Religious Life", "Entrepreneurship / Startups",
            "Internships & Co-ops", "Outdoor Adventures / Hiking", "Gaming & eSports",
            "Quiet/Academic Focus", "Diverse/Multicultural Community", "LGBTQ+ Friendly"
        ],
        key="interests"
    )

    # 5. School Size
    school_size = st.radio(
        "Preferred School Size",
        [
            "Small (< 5,000 students)", 
            "Medium (5,000 – 15,000 students)", 
            "Large (15,000+ students)",
            "No Preference"
        ],
        key="school_size"
    )

    # 6. Location
    location = st.multiselect(
        "Preferred Location & Setting",
        [
            "Northeast (NYC, Boston, Philly)", "West Coast (CA, WA, OR)", 
            "The South (TX, FL, GA)", "Midwest (Chicago, OH, MI)",
            "International / Outside US", "Urban (Big City)", 
            "Suburban (College Town)", "Rural (Secluded Campus)",
            "Warm Weather", "Cold/Snowy Weather"
        ],
        key="location"
    )

    # 7. Learning Style
    learning_style = st.multiselect(
        "Learning Style Preferences",
        [
            "Discussion-based / Seminar Classes", 
            "Large Lectures", 
            "Hands-on / Lab Research", 
            "Project-based Learning", 
            "Independent Study Opportunities"
        ],
        key="learning_style"
    )

    st.divider()

    if st.button("Find Colleges", key="find_colleges"):
        st.success("Profile saved.")
        st.toast("Profile saved")

        # st.session_state["gpa"] = gpa
        # st.session_state["sat_score"] = sat_score
        # st.session_state["rigor"] = rigor
        # st.session_state["extracurriculars"] = extracurriculars
        # st.session_state["majors"] = majors
        # st.session_state["interests"] = interests
        # st.session_state["location"] = location
        # st.session_state["learning_style"] = learning_style
        # st.session_state["budget"] = budget
        # st.session_state["school_size"] = school_size

        majors_str = ", ".join(majors) if majors else "Undecided"
        interests_str = ", ".join(interests) if interests else "General"
        location_str = ", ".join(location) if location else "Anywhere"
        learning_str = ", ".join(learning_style) if learning_style else "Standard"
        sat_display = "unapplicable" if sat_score == 0 else str(sat_score)

        st.divider()
        col_a, col_b = st.columns(2)
        with col_a:
            st.write(f"**Name:** {display_name}")
            st.write(f"**GPA:** {gpa}")
            st.write(f"**SAT Scores:** {sat_display}")
            st.write(f"**Rigor:** {rigor}")
            st.write(f"**Majors:** {majors_str}")
            st.write(f"**Learning Style:** {learning_str}")
        with col_b:
            st.write(f"**Budget:** {budget}")
            st.write(f"**Size:** {school_size}")
            st.write(f"**Location:** {location_str}")
            st.write(f"**Interests:** {interests_str}")
            st.write(f"**Activities:** {extracurriculars if extracurriculars else 'None listed'}")

        st.session_state.step = 2
        st.rerun()

if st.session_state.step >= 2:
    if st.button("Edit Preferences"):
        st.session_state.step = 1
        st.session_state.generated = False
        st.rerun()

    if "generated" not in st.session_state:
        st.session_state.generated = False

    gpa = st.session_state.get("gpa")
    sat_score = st.session_state.get("sat_score")
    rigor = st.session_state.get("rigor")
    extracurriculars = st.session_state.get("extracurriculars")
    majors = st.session_state.get("majors", [])
    interests = st.session_state.get("interests", [])
    location = st.session_state.get("location", [])
    learning_style = st.session_state.get("learning_style", [])
    school_size = st.session_state.get("school_size")
    budget = st.session_state.get("budget")

    majors_str = ", ".join(majors) if majors else "Undecided"
    interests_str = ", ".join(interests) if interests else "General"
    location_str = ", ".join(location) if location else "Anywhere"
    learning_str = ", ".join(learning_style) if learning_style else "Standard"
    sat_display = "unapplicable" if sat_score == 0 else str(sat_score)

    if "client" not in st.session_state:
        st.session_state.client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    client = st.session_state.client

    if not st.session_state.generated:
        with st.spinner("Generating recommendations..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"""
                You are a professional college admissions advisor.

                Student Academic Profile:
                - GPA: {gpa}
                - Test Scores: {sat_display}
                - Rigor: {rigor}
                - Activities/Awards: {extracurriculars}

                Preferences:
                - Intended majors: {majors_str}
                - Budget/Aid: {budget}
                - Interests/Hobbies: {interests_str}
                - School size: {school_size}
                - Location: {location_str}
                - Learning Style: {learning_str}

                Task:
                1. Recommend 5 colleges.
                2. Categorize each as Reach, Match, or Safety (based on the GPA/Scores provided).
                3. Explain WHY each fits their learning style and hobbies.
                4. If any critical info is missing to make a good match, list it first.
                """
            )
        st.session_state["response"] = response.text
        st.session_state.generated = True
    if "response" in st.session_state:
        st.write(st.session_state["response"])
        # st.divider()
        # st.subheader("Ask a follow-up question?")
        # user_chat = st.chat_input("")

        # if user_chat:
        #     # Use the same 'client' to send the user_chat + the previous context
        #     follow_up = client.models.generate_content(
        #         model="gemini-2.5-flash",
        #         contents=f"The user previously got these results: {response.text}. Now they ask: {user_chat}"
        #     )
        #     st.info(follow_up.text)




st.markdown("""
### Features:
- 📊 Stats-based college matching  
- ✍️ AI advice
""")