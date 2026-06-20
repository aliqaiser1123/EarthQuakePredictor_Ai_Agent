import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📉 Model Performance Dashboard")

st.markdown("""
Comparison of all machine learning models used
for earthquake magnitude prediction.
""")

st.markdown("---")

# MANUAL RESULTS
results = pd.DataFrame(
    {
        "Model": ["Linear Regression", "Decision Tree", "Random Forest"],
        "MAE": [0.2902, 0.0734, 0.0687],
        "RMSE": [0.4019, 0.1923, 0.1471],
        "R2": [0.1431, 0.8038, 0.8852],
    }
)

st.dataframe(results, use_container_width=True)

st.markdown("---")

# R2 SCORE
fig = px.bar(results, x="Model", y="R2", title="R² Score Comparison")

st.plotly_chart(fig, use_container_width=True)

# MAE
fig = px.bar(results, x="Model", y="MAE", title="Mean Absolute Error")

st.plotly_chart(fig, use_container_width=True)

# RMSE
fig = px.bar(results, x="Model", y="RMSE", title="Root Mean Squared Error")

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

st.success("""
Random Forest achieved the best performance
for earthquake magnitude prediction.
""")
