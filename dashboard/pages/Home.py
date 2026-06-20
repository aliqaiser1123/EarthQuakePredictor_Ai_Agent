import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown(
    """
<div style='
padding:40px;
border-radius:25px;
background:linear-gradient(
135deg,
#2563eb,
#7c3aed
);
text-align:center;
color:white;
'>

<h1>🌍 SeismoGuard AI</h1>

<h3>
Earthquake Magnitude Prediction &
Disaster Intelligence Platform
</h3>

</div>
""",
    unsafe_allow_html=True,
)
st.markdown("---")
df = pd.read_csv("../dataset/new_dataset.csv")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Earthquakes", len(df))

with col2:
    st.metric("Average Magnitude", round(df["magnitude"].mean(), 2))

with col3:
    st.metric("Maximum Magnitude", round(df["magnitude"].max(), 2))

with col4:
    st.metric("Tsunami Events", int(df["tsunami"].sum()))

st.markdown("---")

# charts

left, right = st.columns(2)

with left:
    fig = px.histogram(df, x="magnitude", nbins=30, title="Magnitude Distribution")
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.histogram(df, x="depth", nbins=30, title="Depth Distribution")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


st.subheader("Recent Earthquake Records")

display_cols = []

for col in ["title", "magnitude", "depth", "tsunami"]:
    if col in df.columns:
        display_cols.append(col)

st.dataframe(df[display_cols].head(15), use_container_width=True)
st.markdown("---")

st.subheader("Project Overview")

st.info("""
This system predicts earthquake magnitude using Machine Learning.

Main Components:

• Earthquake Magnitude Prediction

• Risk Assessment Engine

• Emergency Response Advisor

• Earthquake Hotspot Detection

• Data Analytics Dashboard

• Disaster Intelligence Support System
""")
