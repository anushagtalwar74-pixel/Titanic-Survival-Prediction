import streamlit as st
from datetime import datetime


def app():

    # =====================================================
    # HERO
    # =====================================================

    st.markdown("""
    <div class="hero-section">

    <h1>👩‍💻 About Titanic AI Platform</h1>

    <h3>Enterprise Machine Learning Project</h3>

    <p>
    Titanic AI Platform is an end-to-end Machine Learning web application
    developed using Python, Streamlit, Scikit-Learn and Plotly.
    It demonstrates data preprocessing, visualization,
    predictive analytics and interactive dashboards.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # STATUS CARDS
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("🤖 AI Powered")

    with c2:
        st.info("📊 Analytics")

    with c3:
        st.success("⚡ Real-Time")

    with c4:
        st.warning("🚀 Portfolio Project")

    st.markdown("---")

    # =====================================================
    # PROJECT OVERVIEW
    # =====================================================

    left, right = st.columns([2, 1])

    with left:

        st.subheader("🚢 Project Overview")

        st.write("""
The Titanic AI Platform predicts whether a passenger would survive
using a trained Machine Learning model.

The project includes:

• Data Cleaning

• Exploratory Data Analysis

• Feature Engineering

• Machine Learning Model Training

• Interactive Dashboard

• AI Prediction System

• Professional Enterprise UI

• Downloadable Reports
""")

    with right:

        st.markdown("""
<div class="glass-card">

<h3>🏆 Highlights</h3>

✔ Enterprise UI

<br><br>

✔ Dark Theme

<br><br>

✔ Plotly Charts

<br><br>

✔ Streamlit Dashboard

<br><br>

✔ Machine Learning

</div>
""", unsafe_allow_html=True)

    st.markdown("---")

    # =====================================================
    # TECHNOLOGY STACK
    # =====================================================

    st.subheader("🛠 Technology Stack")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
### Backend

• Python

• Pandas

• NumPy

• Joblib
""")

    with col2:
        st.success("""
### Machine Learning

• Scikit-Learn

• Classification

• Data Preprocessing

• Model Evaluation
""")

    with col3:
        st.warning("""
### Frontend

• Streamlit

• Plotly

• HTML

• CSS
""")

    st.markdown("---")

    # =====================================================
    # DEVELOPER
    # =====================================================

    st.subheader("👩‍💻 Developer")

    st.markdown("""
<div class="glass-card">

## Anusha Talawar

AI & Machine Learning Enthusiast

Python Developer

Machine Learning

Data Analytics

Streamlit Developer

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # PROJECT FEATURES
    # =====================================================

    st.subheader("🚀 Features")

    f1, f2 = st.columns(2)

    with f1:

        st.success("""
✔ AI Survival Prediction

✔ Interactive Dashboard

✔ Dataset Explorer

✔ Prediction History

✔ Download Reports
""")

    with f2:

        st.info("""
✔ Responsive UI

✔ Enterprise Design

✔ Plotly Charts

✔ Machine Learning

✔ Professional Portfolio
""")

    st.markdown("---")

    # =====================================================
    # PROJECT METRICS
    # =====================================================

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Pages", "5")
    m2.metric("Charts", "10+")
    m3.metric("ML Model", "1")
    m4.metric("Version", "2.0")

    st.markdown("---")

    # =====================================================
    # FOOTER
    # =====================================================

    left, center, right = st.columns([2, 2, 1])

    with left:
        st.caption("🚢 Titanic AI Platform")

    with center:
        st.caption("Built using Python • Streamlit • Plotly • Scikit-Learn")

    with right:
        st.caption(datetime.now().strftime("%d %b %Y"))
st.caption(
"🚀 Powered by Anusha Talawar | Titanic AI Platform | Version 2.0"
)