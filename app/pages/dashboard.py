from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_lottie import st_lottie
import requests

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def app():
    df = pd.read_csv("data/raw/Titanic-Dataset.csv")
        # ==========================
    # TITANIC HERO IMAGE
    # ==========================

    banner = Path("assets/images/titanic_banner.jpg")

    if banner.exists():
        st.image(str(banner), width="stretch")

    # ==========================
    # LOAD DATA
    # ==========================

    df = pd.read_csv("data/raw/Titanic-Dataset.csv")
    total = len(df) 
    
    with st.spinner("🚢 Loading Enterprise Dashboard..."):
        pass
    # ==========================
    # HERO
    # ==========================

    if "loaded_once" not in st.session_state:
        st.session_state.loaded_once = True
        st.toast(
            "🚢 Enterprise Dashboard Ready!",
            icon="🎉"
        )
    st.markdown("""
    <div class="hero-section">

    <h1>🚢 Titanic AI Platform</h1>

    <h3>Enterprise Machine Learning Dashboard</h3>

    <p>
    Analyze the Titanic dataset with interactive visualizations,
    machine learning insights and professional analytics.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.info("🚢 Enterprise Machine Learning Dashboard is connected successfully.")

    with st.container(border=True):

     st.subheader("✨ AI Highlights")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("✔ Machine Learning")

    with c2:
        st.info("📊 Interactive Analytics")

    with c3:
        st.success("⚡ Real-Time Dashboard")
        
    st.markdown("""
    <style>

    .hero-section h1{

    animation:titleGlow 3s infinite alternate;

    } 

    @keyframes titleGlow{

    from{

    text-shadow:
    0 0 10px #4F8EF7;

    }

    to{

    text-shadow:
    0 0 30px #7B61FF,
    0 0 60px #4F8EF7;

    }

    }

  </style>
  """, unsafe_allow_html=True)

    # ==========================
    # STATUS BADGES
    # ==========================

    c1, c2, c3, c4 = st.columns(4)

    c1.success("✔ AI Ready")
    c2.info("📊 Analytics")
    c3.warning("⚡ Real-Time")
    c4.success("🚀 Enterprise UI")

    st.markdown("<br>", unsafe_allow_html=True)
    if "dashboard_loaded" not in st.session_state:
        st.session_state.dashboard_loaded = True
        st.toast("🚢 Welcome to Titanic AI Platform", icon="🎉")

    # ==========================
    # KPI CARDS
    # ==========================

    total = len(df)
    survived = int(df["Survived"].sum())
    died = total - survived
    features = len(df.columns)

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric("👥 Passengers", total)

    with k2:
        st.metric("🟢 Survived", survived)

    with k3:
        st.metric("🔴 Died", died)

    with k4:
        st.metric("📁 Features", features)

    style_metric_cards(
        background_color="#101D2E",
        border_left_color="#4F8EF7",
        border_color="#1D3557",
        box_shadow=True
    )

    st.markdown("<hr>", unsafe_allow_html=True)
    
    st.markdown("### 📈 Live Dashboard Status")

    progress = survived / total

    st.progress(progress)

    st.caption(f"Survival Rate : {progress*100:.1f}%")
    
    st.markdown("<br>", unsafe_allow_html=True)

    ai1, ai2, ai3 = st.columns(3)

    with ai1:
        st.info("🧠 AI Model: Online")

    with ai2:
        st.success("📊 Dataset: Loaded")

    with ai3:
        st.warning("⚡ Prediction Engine Ready")

    # ==========================
    # TWO COLUMN LAYOUT
    # ==========================

    left, right = st.columns([2,1])

    # ==========================
    # CHART
    # ==========================

    with left:

        fig = px.histogram(

            df,

            x="Survived",

            color="Survived",

            title="Passenger Survival Distribution",

            template="plotly_dark"

        )

        fig.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)",

            title_x=0.5

        )

        st.plotly_chart(fig, width="stretch")
        st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head(10), width="stretch")

    # ==========================
    # AI INSIGHTS
    # ==========================

    with right:
        
        lottie_ai = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_zrqthn6o.json"
    )

    if lottie_ai:
      st_lottie(
        lottie_ai,
        height=260,
        key="ai_robot"
       )

    st.markdown("""

        <div class="glass-card">

        <h2>🤖 AI Insights</h2>

        ✅ Dataset Loaded

        <br><br>

        ✅ Machine Learning Ready

        <br><br>

        ✅ Interactive Dashboard

        <br><br>

        ✅ Plotly Visualization

        <br><br>

        ✅ Enterprise Design

        </div>

        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================
    # GENDER CHART
    # ==========================

    col1, col2 = st.columns(2)

    with col1:

        gender = px.pie(

            df,

            names="Sex",

            title="Gender Distribution",

            template="plotly_dark"

        )

        gender.update_layout(

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)"

        )

        st.plotly_chart(gender, width="stretch")

    with col2:

        pclass = px.bar(

            df["Pclass"].value_counts().sort_index(),

            title="Passenger Class",

            template="plotly_dark"

        )

        pclass.update_layout(

            xaxis_title="Class",

            yaxis_title="Passengers",

            paper_bgcolor="rgba(0,0,0,0)",

            plot_bgcolor="rgba(0,0,0,0)"

        )

        st.plotly_chart(pclass, width="stretch")
     
        # ==========================
    # ADVANCED ANALYTICS
    # ==========================

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📊 Advanced Analytics")

    col1, col2 = st.columns(2)

    with col1:

        age_chart = px.histogram(
            df,
            x="Age",
            nbins=30,
            color="Survived",
            template="plotly_dark",
            title="Age Distribution"
        )

        age_chart.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(age_chart, width="stretch")

    with col2:

        fare_chart = px.box(
            df,
            x="Survived",
            y="Fare",
            color="Survived",
            template="plotly_dark",
            title="Fare Distribution"
        )

        fare_chart.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(fare_chart, width="stretch")

    # ==========================
    # DATASET PREVIEW
    # ==========================

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📄 Dataset Preview")

    st.dataframe(df.head(10), width="stretch")

    # ==========================
    # DATASET STATISTICS
    # ==========================

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("📈 Dataset Statistics")

    st.dataframe(df.describe(), width="stretch")

    # ==========================
    # SEARCH PASSENGER
    # ==========================

    st.markdown("<br>", unsafe_allow_html=True)

    search = st.text_input("🔍 Search Passenger Name")

    if "Name" in df.columns:

        filtered = df[
            df["Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

        st.dataframe(filtered, width="stretch")

    # ==========================
    # DOWNLOAD DATASET
    # ==========================

    csv = df.to_csv(index=False)

    st.download_button(
        "📥 Download Dataset",
        csv,
        file_name="Titanic_Dataset.csv",
        mime="text/csv"
    )
       
        # ==========================
    # PROFESSIONAL FOOTER
    # ==========================

    from datetime import datetime

    st.markdown("---")

    left, center, right = st.columns([2,2,1])

    with left:
        st.caption("🚢 Titanic AI Platform")

    with center:
        st.caption(
            "Built using Python • Streamlit • Plotly • Scikit-Learn"
        )

    with right:
        st.caption(
            datetime.now().strftime("%d %b %Y")
        )
    
st.caption(
"🚀 Powered by Anusha Talawar | Titanic AI Platform | Version 2.0"
)