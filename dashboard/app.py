import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="SeismoGuard AI", page_icon="🌍", layout="wide")
st.title("🌍 SeismoGuard AI")

st.set_page_config(page_title="SeismoGuard AI", page_icon="🌍", layout="wide")

page = option_menu(
    menu_title=None,
    options=[
        "Home",
        "AI Decision Centre",
        "Hotspots",
        "Model Performance",
        "About",
    ],
    icons=[
        "house",
        "activity",
        "geo-alt",
        "shield-check",
        "graph-up",
        "info-circle",
    ],
    orientation="horizontal",
)

# PAGE ROUTING
if page == "Home":
    exec(open("pages/Home.py", encoding="utf-8").read())

elif page == "Dataset Explorer":
    exec(open("pages/Dataset_Explorer.py", encoding="utf-8").read())

elif page == "AI Decision Centre":
    exec(open("pages/AI_Decision_Centre.py", encoding="utf-8").read())

elif page == "Hotspots":
    exec(open("pages/hot_spot.py", encoding="utf-8").read())

elif page == "Model Performance":
    exec(open("pages/Model_Performance.py", encoding="utf-8").read())

elif page == "About":
    exec(open("pages/About_Project.py", encoding="utf-8").read())
