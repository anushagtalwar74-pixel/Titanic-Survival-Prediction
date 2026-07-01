import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path


def app():

    # =====================================================
    # LOAD DATA
    # =====================================================

    data_path = Path("data/raw/Titanic-Dataset.csv")

    if not data_path.exists():
        st.error("Dataset not found.")
        return

    df = pd.read_csv(data_path)

    # =====================================================
    # HERO
    # =====================================================

    st.markdown("""
    <div class="hero-section">

    <h1>📂 Titanic Dataset</h1>

    <h3>Enterprise Dataset Explorer</h3>

    <p>
    Explore, search, analyze and download the Titanic dataset
    used for training the Machine Learning model.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # STATUS CARDS
    # =====================================================

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.success("📂 Dataset Loaded")

    with c2:
        st.info("📊 891 Records")

    with c3:
        st.success("🤖 ML Ready")

    with c4:
        st.warning("⚡ Interactive")

    st.markdown("---")

    # =====================================================
    # DATASET OVERVIEW
    # =====================================================

    m1, m2, m3, m4 = st.columns(4)

    m1.metric("Passengers", len(df))
    m2.metric("Columns", len(df.columns))
    m3.metric("Missing Values", int(df.isna().sum().sum()))
    m4.metric("Memory Usage", f"{df.memory_usage().sum()/1024:.1f} KB")

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # SEARCH
    # =====================================================

    st.subheader("🔍 Search Passenger")

    search = st.text_input(
        "Enter passenger name",
        placeholder="Example : Allen"
    )

    if "Name" in df.columns:

        filtered = df[
            df["Name"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    else:
        filtered = df

    # =====================================================
    # DATAFRAME
    # =====================================================

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        filtered,
        width="stretch",
        height=450
    )

    # =====================================================
    # DOWNLOAD
    # =====================================================

    csv = df.to_csv(index=False)

    st.download_button(
        "📥 Download Dataset",
        csv,
        file_name="Titanic_Dataset.csv",
        mime="text/csv",
        width="stretch"
    )

    st.markdown("---")

    # =====================================================
    # DATA TYPES
    # =====================================================

    left, right = st.columns(2)

    with left:

        st.subheader("📑 Data Types")

        st.dataframe(
            pd.DataFrame(df.dtypes, columns=["Type"]),
            width="stretch"
        )

    with right:

        st.subheader("📊 Missing Values")

        missing = pd.DataFrame({
            "Column": df.columns,
            "Missing": df.isna().sum()
        })

        st.dataframe(
            missing,
            width="stretch"
        )

    st.markdown("---")

    # =====================================================
    # FEATURE DISTRIBUTION
    # =====================================================

    st.subheader("📈 Passenger Class Distribution")

    fig = px.histogram(
        df,
        x="Pclass",
        color="Pclass",
        template="plotly_dark",
        title="Passenger Class"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        title_x=0.5
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    st.markdown("---")

    # =====================================================
    # QUICK STATISTICS
    # =====================================================

    st.subheader("📈 Dataset Statistics")

    st.dataframe(
        df.describe(),
        width="stretch"
    )

    st.markdown("---")

    # =====================================================
    # INFORMATION
    # =====================================================

    st.markdown("""
    <div class="glass-card">

    <h2>🤖 Dataset Information</h2>

    ✅ Original Titanic Dataset

    <br><br>

    ✅ Used for Machine Learning

    <br><br>

    ✅ Cleaned and Preprocessed

    <br><br>

    ✅ Interactive Search Available

    <br><br>

    ✅ Download Supported

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.success("✅ Dataset loaded successfully.")
    
st.caption(
"🚀 Powered by Anusha Talawar | Titanic AI Platform | Version 2.0"
)