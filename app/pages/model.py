import streamlit as st
import pandas as pd
import plotly.express as px


def app():

    st.markdown("""
    <div class="hero-section">

    <h1>🧠 AI Model</h1>

    <h3>Machine Learning Information</h3>

    <p>
    Explore the trained Random Forest model,
    its features and prediction process.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.success("✅ Model Loaded Successfully")

    st.subheader("📋 Model Summary")

    st.write("""
    **Algorithm:** Random Forest Classifier

    **Problem Type:** Binary Classification

    **Target:** Passenger Survival

    **Training Dataset:** Titanic Dataset

    **Library:** Scikit-Learn
    """)

    st.markdown("---")

    st.subheader("📊 Features Used")

    features = pd.DataFrame({

        "Feature":[
            "Pclass",
            "Sex",
            "Age",
            "SibSp",
            "Parch",
            "Fare",
            "Embarked"
        ]

    })

    st.dataframe(features, width="stretch")

    st.markdown("---")

    st.subheader("⚙ AI Workflow")

    st.info("""

1️⃣ Dataset Loaded

⬇

2️⃣ Data Cleaning

⬇

3️⃣ Feature Encoding

⬇

4️⃣ Model Training

⬇

5️⃣ Prediction

⬇

6️⃣ Confidence Score

""")

    st.success("🚀 Enterprise AI Model Ready")