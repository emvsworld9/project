import streamlit as st


st.set_page_config(page_title="Weqaya", layout="wide")
# Navigation
PAGES = {
    "Home": r"C:\Users\VICTUS\Desktop\DEPI team\FINAL PROJECT\hype\source\home_page.py",
    "Hypertension Prediction": r"C:\Users\VICTUS\Desktop\DEPI team\FINAL PROJECT\hype\source\first.py",
   """ "Diabetes":r"C:\Users\VICTUS\Desktop\DEPI team\FINAL PROJECT\diab\source\second.py","""
    "Storke":r"C:\Users\VICTUS\Desktop\DEPI team\FINAL PROJECT\stroke\main_page.py"
}

st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page", list(PAGES.keys()))

# Display the selected page
if page == "Home":
    exec(open(PAGES["Home"], encoding="utf-8").read())
elif page == "Hypertension Prediction":
    exec(open(PAGES["Hypertension Prediction"], encoding="utf-8").read())
elif page == "Diabetes":
    exec(open(PAGES["Diabetes"], encoding="utf-8").read())
else:
    exec(open(PAGES["Storke"], encoding="utf-8").read())
