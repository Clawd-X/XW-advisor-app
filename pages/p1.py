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
name = st.text_input("What's your name? (optional)", key="name")

# Initialize state
if "confirmed" not in st.session_state:
    st.session_state.confirmed = False

# Button
if st.button("Confirm", key="confirm_name"):
    st.session_state.confirmed = True

# Step 2: Reveal section AFTER click
if st.session_state.confirmed:
    st.divider()

    name = st.session_state.name_input.strip()

    if name == "":
        name = "User"
    
    st.session_state["name"] = name

    st.header(f"Hello, {name}! 👋")

    st.write("Now let's find your perfect colleges...")

    st.subheader("Your Preferences")

    # Majors
    majors = st.multiselect(
        "Intended Major(s)",
        ["Computer Science", "Biology", "Business", "Engineering", "Psychology"],
        key="majors"
    )

    # Budget
    budget = st.selectbox(
        "Budget",
        ["< $20k", "$20k–$40k", "$40k–$70k", "$70k+"],
        key="budget"
    )

    # Interests
    interests = st.multiselect(
        "Interests",
        ["Research", "Sports", "Party Scene", "Internships", "Campus Life"],
        key="interests"
    )

    # School type
    school_size = st.radio(
        "Preferred School Size",
        ["Small / Close-knit", "Medium", "Large / Big campus"],
        key="school_size"
    )

    # Location
    location = st.selectbox(
        "Preferred Location",
        ["California", "West Coast", "Anywhere in US", "Urban", "Suburban", "Rural"],
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
