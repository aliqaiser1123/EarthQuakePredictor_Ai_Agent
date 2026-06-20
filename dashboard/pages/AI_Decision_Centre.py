import streamlit as st
import pandas as pd
from streamlit_agraph import Node, Edge, Config, agraph

from knowledge_system.bfs_agent import MASTER_GRAPH
from knowledge_system.planner import SeismoGuardPlanner
# from knowledge_system.whatsapp_alert import build_alert, send_alert

import streamlit.components.v1 as components
import joblib

MODEL_PATH = "../models/magnitude_model.pkl"
model = joblib.load(MODEL_PATH)


def get_model():
    return model


def speak(text):
    components.html(
        f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{text}");
        window.speechSynthesis.speak(msg);
        </script>
        """,
        height=0,
    )


model = get_model()

st.set_page_config(page_title="AI State Space Search", layout="wide")

st.title("🤖 SeismoGuard AI Search Agent")

st.markdown("""
This module demonstrates:

- Knowledge-Based Reasoning
- Inference Engine
- State Space Representation
- BFS Search Agent
- Constraint Satisfaction Problem (CSP)
- Goal State Achievement
""")

# USER INPUTS
col1, col2, col3 = st.columns(3)

with col1:
    # magnitude = st.slider("Magnitude", 0.0, 10.0, 6.5)
    sig = st.number_input(
        "Significance (Estimated impact on public ranging from 0 to 1000)", value=500
    )
    cdi = st.number_input(
        "CDI (Did You Feel It? (DYFI) system from 1.0 to 10.0)", value=5.0
    )
with col2:
    tsunami = st.selectbox("Tsunami Risk", [0, 1])
    gap = st.number_input(
        "Gap (that is overdue for a major earthquake.)",
        value=50.0,
    )

with col3:
    depth = st.number_input(
        "Depth (exact vertical distance beneath the Earth's surface)", value=10.0
    )
    population = st.number_input(
        "Population (ammount to evacuate)", min_value=100, value=700
    )

col1, col2 = st.columns(2)

if st.button("▶ Start AI Agent"):
    speak("Initializing AI agent...")
    sample = pd.DataFrame(
        {
            "cdi": [cdi],
            "mmi": 10,
            "tsunami": [tsunami],
            "sig": [sig],
            "nst": 500,
            "dmin": 10,
            "gap": [gap],
            "depth": [depth],
            "latitude": 80,
            "longitude": 70,
        }
    )

    # sample_scaled = scaler.transform(sample)

    magnitude = model.predict(sample)[0]
    col1, col2 = st.columns(2)
    if magnitude < 4:
        st.success(f"🟢 Magnitude: {magnitude:.2f}")

    elif magnitude < 6:
        st.warning(f"🟡 Magnitude: {magnitude:.2f}")

    else:
        st.error(f"🔴 Magnitude: {magnitude:.2f}")
        st.metric("Magnitude", round(magnitude, 2))
    rounded_mag = round(magnitude, 2)
    speak(f"Magnitude Predicted; The Value is {rounded_mag}")

    # AI ENGINE
    planner = SeismoGuardPlanner()  # from planner.py

    result = planner.generate_plan(magnitude, tsunami, population)
    selected_path = result["path"]
    selected_shelter = result["shelter"]
    category = result["category"]
    rules = result["rules"]

    # alert_message = build_alert(category, magnitude, selected_shelter)

    path_edges = []

    for i in range(len(selected_path) - 1):
        path_edges.append((selected_path[i], selected_path[i + 1]))

    # # WHATSAPP ALERT

    # if st.button("📱 Send WhatsApp Alert"):
    #     success = send_alert("+923106643436", alert_message)

    #     if success:
    #         st.success("WhatsApp Alert Sent Successfully")
    # speak("Sending WhatsApp Alert, Successfull...")
    #     else:
    #         st.error("Failed to send WhatsApp Alert")

    # GRAPH NODES

    all_nodes = set()

    for source in MASTER_GRAPH:
        all_nodes.add(source)

        for target in MASTER_GRAPH[source]:
            all_nodes.add(target)

    nodes = []

    for node in all_nodes:
        if node in selected_path:
            nodes.append(Node(id=node, label=node, size=30, color="#00CC66"))

        else:
            nodes.append(Node(id=node, label=node, size=22, color="#D3D3D3"))

    # GRAPH EDGES
    edges = []

    for source in MASTER_GRAPH:
        for target in MASTER_GRAPH[source]:
            if (source, target) in path_edges:
                edges.append(
                    Edge(source=source, target=target, color="#00CC66", width=6)
                )

            else:
                edges.append(
                    Edge(source=source, target=target, color="#A0A0A0", width=2)
                )

    # GRAPH CONFIG
    config = Config(
        width=1200,
        height=700,
        directed=True,
        hierarchical=False,
        physics=True,
        nodeHighlightBehavior=True,
        highlightColor="#F7A7A6",
    )

    # GRAPH DISPLAY
    st.subheader("🌐 Complete State Space")

    agraph(nodes=nodes, edges=edges, config=config)
    speak("Graph Created, Retrieving Optimal Path...")

    # AI RESULTS
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🧠 Inference Engine")

        st.success(f"Selected Category: {category}")

        st.write("Triggered Rules:")

        for rule in rules:
            st.info(rule)

    with col2:
        st.subheader("🏢 CSP Shelter Allocation")

        if selected_shelter:
            st.success(selected_shelter["name"])

            st.write(f"Capacity: {selected_shelter['capacity']}")

            st.write(f"Road Status: {selected_shelter['road']}")

            st.write(f"Medical Support: {selected_shelter['medical']}")

        else:
            st.error("No valid shelter found.")

    # RESPONSE PATH
    st.subheader("🎯 Selected Emergency Response Path")

    st.success(" ➜ ".join(selected_path))
    speak("Sending WhatsApp Alert, Successfull...")
    speak(
        f"Moving people towards the {selected_shelter['name']} having {selected_shelter['capacity']} persons capacity"
    )
    # AI PIPELINE
    with st.expander("📚 AI Architecture Explanation"):
        st.markdown(
            """
    ### Step 1 — Magnitude Prediction

    Random Forest predicts earthquake magnitude.

    ---

    ### Step 2 — Knowledge Base

    Expert disaster-management rules are stored.

    Examples:

    - High Risk
    - Medium Risk
    - Low Risk
    - Tsunami Risk

    ---

    ### Step 3 — Inference Engine

    Rules are evaluated.

    A strategy is selected.

    ---

    ### Step 4 — State Space Representation

    All possible emergency actions are represented as nodes.

    ---

    ### Step 5 — BFS Search Agent

    The agent searches for a valid path toward:

    **Population Safe**

    ---

    ### Step 6 — CSP Shelter Allocation

    Constraints:

    - Shelter Capacity
    - Medical Support
    - Road Availability

    Best shelter is selected.

    ---

    ### Step 7 — Goal State

    Population Safe
            """
        )
