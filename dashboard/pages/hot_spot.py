import streamlit as st
import pandas as pd
import folium

from streamlit_folium import st_folium
from sklearn.cluster import KMeans


st.set_page_config(page_title="Hotspot Detection", layout="wide")
st.title("🌍 Earthquake Hotspot Detection")

st.markdown("""
Identify earthquake-prone regions using
K-Means clustering on geographical coordinates.
""")

st.markdown("---")

try:
    df = pd.read_csv("../dataset/new_dataset.csv")

except:
    st.error("Dataset not found.")
    st.stop()

NUM_CLUSTERS = 10
kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(df[["latitude", "longitude"]])
cluster_centers = kmeans.cluster_centers_

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Earthquakes", len(df))

with col2:
    st.metric("Detected Hotspots", NUM_CLUSTERS)

with col3:
    st.metric("Average Magnitude", round(df["magnitude"].mean(), 2))

st.markdown("---")

center_lat = df["latitude"].mean()
center_lon = df["longitude"].mean()

m = folium.Map(
    location=[center_lat, center_lon], zoom_start=2, tiles="CartoDB positron"
)

cluster_colors = {
    0: "red",
    1: "blue",
    2: "green",
    3: "purple",
    4: "orange",
    5: "yellow",
    6: "pink",
    7: "cyan",
    8: "black",
    9: "brown",
}


for _, row in df.iterrows():
    magnitude = float(row["magnitude"])

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=max(4, magnitude * 1.5),
        color=cluster_colors[row["Cluster"]],
        fill=True,
        fill_color=cluster_colors[row["Cluster"]],
        fill_opacity=0.7,
        popup=f"""
        <b>Magnitude:</b> {magnitude}<br>
        <b>Depth:</b> {row["depth"]} km<br>
        <b>Cluster:</b> {row["Cluster"]}
        """,
    ).add_to(m)

for i, center in enumerate(cluster_centers):
    folium.Marker(
        location=[center[0], center[1]],
        popup=f"Hotspot Center {i}",
        tooltip=f"Cluster {i}",
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m)


st.subheader("🌎 Earthquake Hotspot Map")
st_folium(m, width=1400, height=700)
st.markdown("---")


st.subheader("📊 Cluster Summary")
cluster_summary = df.groupby("Cluster").agg(
    {"magnitude": ["count", "mean", "max"], "depth": "mean"}
)
cluster_summary.columns = ["Events", "Avg Magnitude", "Max Magnitude", "Avg Depth"]
cluster_summary = cluster_summary.round(2)
st.dataframe(cluster_summary, use_container_width=True)
st.markdown("---")

largest_cluster = df["Cluster"].value_counts().idxmax()
largest_count = df["Cluster"].value_counts().max()
highest_mag = round(df["magnitude"].max(), 2)
st.subheader("🧠 AI Insights")

st.info(f"""
Largest Hotspot Cluster: {largest_cluster}

Earthquakes in Cluster: {largest_count}

Maximum Recorded Magnitude: {highest_mag}

Cluster centers indicate regions with concentrated seismic activity.
These areas may require enhanced monitoring and disaster preparedness.
""")
