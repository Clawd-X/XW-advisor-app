import streamlit as st

st.set_page_config(page_title="College Advisor", layout="wide")

st.title("🎓 College Advisor")
st.subheader("Academic Stats")
st.divider()

st.write("Use the sidebar to navigate between tools.")

p2 = st.Page("pages/p1.py", title = "Stats-Based College Advisor", icon = "📊")
p3 = st.Page("pages/p2.py", title = "Short Answer Helper", icon = "✍️")
p4 = st.Page("pages/p3.py", title = "WebdriverTorso", icon = "⚙️")


pg = st.navigation([p2,p3,p4])
pg.run()

st.markdown("""
### Features:
- 📊 Stats-based college matching  
- ✍️ Short answer / essay help  
""")