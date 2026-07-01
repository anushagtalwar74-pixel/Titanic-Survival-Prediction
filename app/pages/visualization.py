import streamlit as st
import pandas as pd
import plotly.express as px


def app():

    df = pd.read_csv("data/raw/Titanic-Dataset.csv")

    st.markdown("""
    <div class="hero-section">

    <h1>📈 Visualizations</h1>

    <h3>Interactive Charts</h3>

    <p>
    Explore the Titanic dataset using beautiful
    interactive visualizations.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        fig = px.histogram(
            df,
            x="Age",
            template="plotly_dark",
            title="Age Distribution"
        )

        st.plotly_chart(fig, width="stretch")

    with col2:

        fig = px.pie(
            df,
            names="Sex",
            hole=.45,
            template="plotly_dark",
            title="Gender Distribution"
        )

        st.plotly_chart(fig, width="stretch")

    col3, col4 = st.columns(2)

    with col3:

        fig = px.bar(
            df,
            x="Pclass",
            color="Survived",
            template="plotly_dark",
            title="Passenger Class"
        )

        st.plotly_chart(fig, width="stretch")

    with col4:

        fig = px.box(
            df,
            x="Survived",
            y="Fare",
            template="plotly_dark",
            title="Fare Analysis"
        )

        st.plotly_chart(fig, width="stretch")