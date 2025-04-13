import streamlit as st
import pandas as pd
from datetime import datetime

# CONFIG
st.set_page_config(page_title="Tech Career Insights", layout="centered")

# TITLE
st.title("What Drives Tech Salaries?")

# SECTION: Action Buttons
st.subheader("🔗 Access Resources")

col1, col2, col3 = st.columns(3)

with col1:
    st.link_button("2019 Kaggle Machine Learning & Data Science Survey", "https://www.kaggle.com/c/kaggle-survey-2019", use_container_width=True)  # Replace with actual URL

with col2:
    with open("tech_career.csv", "rb") as f:  # Replace with your CSV file path
        st.download_button(
            label="Download Our Pre-processed Data",
            data=f,
            file_name="tech_career.csv",
            mime="text/csv",
            use_container_width=True
        )

with col3:
    st.button("Our analysis and report", disabled=True, use_container_width=True)
    st.caption("Report is currently under grading and will be available soon.")

# SECTION: Dataset Preview
st.markdown("---")
st.subheader("📑 Preview of Our Dataset")

try:
    df = pd.read_csv("tech_career.csv")  # Replace with your actual dataset
    st.dataframe(df.head(10))
except FileNotFoundError:
    st.error("⚠️ Dataset not found. Please upload or place 'our_data.csv' in the same directory.")

# SECTION: Metadata
st.markdown("---")
st.markdown(f"**Publish Date:** {datetime.now().strftime('%B %d, %Y')}")
st.markdown("""
✍️ **Credit:**  
This dataset was created by a group of students from **Nanyang Technological University (NTU)**, as part of the course project for **MH3511**, Semester 2, AY2024/25.  

**Group Members:**  
- Nguyen Hoang Minh Ngoc 
- Tan Ying Shan  
- Tan Jing Sheng
- Yashver Shori 
- Yu Fengyuan  
""")


