import streamlit as st

def play_sound():
    st.markdown("""
        <audio autoplay>
        <source src="https://www.soundjay.com/buttons/sounds/button-09.mp3" type="audio/mp3">
        </audio>
    """, unsafe_allow_html=True)

st.title("📊 Stats-Based College Advisor")
st.header("Enter information below to get started!")
st.divider()

st.header("Lets get to know you! ")

name_input = st.text_input("What's your name? (optional)", key="name_input")
name = name_input.strip()

# Initialize state
if "confirmed" not in st.session_state:
    st.session_state.confirmed = False

# Button
if st.button("Confirm", key="confirm_name"):
    st.session_state.confirmed = True

# Step 2: Reveal section AFTER click
if st.session_state.confirmed:
    st.divider()

    if name == "":
        name = "User"
    
    st.session_state["name"] = name

    st.header(f"Hello, {name}! 👋")

    st.write("Now let's find your perfect colleges...")

    st.subheader("Your Preferences")

# 1. Majors
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

    # 2. Budget
    budget = st.selectbox(
        "Budget (Total Cost per Year)",
        [
            "<$20k", 
            "$20k–$40k", 
            "$40k–$60k", 
            "$60k–$80k", 
            ">$80k+", 
            "No Budget Preference"
        ],
        key="budget"
    )

    # 3. Interests
    interests = st.multiselect(
        "Interests & Priorities",
        [
            "Undergraduate Research", "Study Abroad Programs", "Greek Life (Frats/Sororities)",
            "D1 Sports / School Spirit", "Intramural Sports", "Performing Arts / Theater",
            "Social Justice & Activism", "Religious Life", "Entrepreneurship / Startups",
            "Internships & Co-ops", "Outdoor Adventures / Hiking", "Gaming & eSports",
            "Quiet/Academic Focus", "Diverse/Multicultural Community", "LGBTQ+ Friendly"
        ],
        key="interests"
    )

    # 4. School Size
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

    # 5. Location
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

    st.divider()

    if st.button("Find Colleges", key="find_colleges"):
        play_sound()
        st.session_state["submitted"] = True
        st.success("Profile saved! Go to the Short Answer page 👉")

        # st.session_state["majors"] = majors
        # st.session_state["budget"] = budget
        # st.session_state["interests"] = interests
        # st.session_state["school_size"] = school_size
        # st.session_state["location"] = location

        st.subheader("🎯 Your Profile")
        st.write("Majors:", majors)
        st.write("Budget:", budget)
        st.write("Interests:", interests)
        st.write("Size:", school_size)
        st.write("Location:", location)

        st.success("Generating recommendations...")
