import streamlit as st

st.title("📄 About Project")

st.markdown("---")

st.header("Project Title")

st.info("""
SeismoGuard AI:
Earthquake Magnitude Prediction
and Disaster Response Intelligence System
""")

st.markdown("---")

st.header("Objectives")

st.markdown("""
✔ Predict earthquake magnitude

✔ Analyze earthquake trends

✔ Detect earthquake hotspots

✔ Assess disaster risk

✔ Provide emergency recommendations

✔ Support disaster preparedness
""")

st.markdown("---")

st.header("Dataset")

st.markdown("""
Earthquake Dataset from Kaggle

Features Used:

• CDI

• MMI

• Tsunami

• SIG

• NST

• DMIN

• GAP

• Depth

• Latitude

• Longitude

Target Variable:

Magnitude
""")

st.markdown("---")

st.header("Algorithms")

st.markdown("""
### Regression Models

• Linear Regression

• Decision Tree Regressor

• Random Forest Regressor

### Clustering

• K-Means Clustering

### Visualization

• Plotly

• Folium

• Streamlit
""")

st.markdown("---")

st.header("Technologies")

st.markdown("""
Python

Pandas

NumPy

Scikit-Learn

Plotly

Folium

Streamlit

Joblib
""")

st.markdown("---")

st.header("Future Scope")

st.success("""
• Real-Time USGS Integration

• Government Dashboard

• SMS Alerts

• AI-Based Disaster Forecasting

• Mobile Application

• Rescue Resource Optimization
""")

st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.header("\tDEVELOPED BY")
    st.subheader("\tMuhammad Ali")
    st.write("\tClassics Matrix Lab")
with col2:
    st.image("utils/classics.png", width=400)
