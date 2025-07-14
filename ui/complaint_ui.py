import streamlit as st
import pandas as pd
import plotly.express as px
from logic.complaint_classifier import classify_complaint
from logic.geo_clustering import cluster_complaints

def complaint_ui():
    st.markdown("### 📩 Smart Complaint Prioritizer")
    st.write("Upload your complaint CSV or paste complaints manually to see classification & routing.")

    # Upload CSV section
    uploaded_file = st.file_uploader("Upload CSV (with 'Complaint' column)", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        if "Complaint" not in df.columns:
            st.error("CSV must contain a 'Complaint' column.")
            return
        st.success(f"✅ Loaded {len(df)} complaints.")
    else:
        st.markdown("Or manually enter a few complaints (one per line):")
        manual_input = st.text_area("Enter complaints:", height=150)
        if manual_input.strip():
            complaints = manual_input.strip().split("\n")
            df = pd.DataFrame({"Complaint": complaints})
        else:
            st.info("Awaiting input or upload...")
            return

    # Classify
    classified = df["Complaint"].apply(classify_complaint)
    df["Urgency"] = classified.apply(lambda x: x["urgency"])
    df["Category"] = classified.apply(lambda x: x["issue_type"])
    df["Location"] = classified.apply(lambda x: x["location"])

    # Cluster
    df["Cluster"] = cluster_complaints(df["Complaint"])

    # Display
    st.markdown("#### 🧠 Classified Complaints")
    st.dataframe(df)

    # Charts
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🔥 Urgency Distribution")
        fig = px.histogram(df, x="Urgency", color="Urgency", barmode="group")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("#### 📂 Category Distribution")
        fig = px.histogram(df, x="Category", color="Category", barmode="group")
        st.plotly_chart(fig, use_container_width=True)

    # Optional: Cluster map
    st.markdown("#### 🗺️ Geo-cluster (simulated)")
    st.dataframe(df.groupby("Cluster")["Complaint"].count().reset_index().rename(columns={"Complaint": "No. of Complaints"}))
