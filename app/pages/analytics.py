
import pandas as pd
import plotly.express as px
import streamlit as st

def app():
    st.title("analytics")

    # Your dashboard code goes here
    # -------------------------
    # Load Dataset
    # -------------------------

    df = pd.read_csv("data/raw/Titanic-Dataset.csv")

    # -------------------------
    # Hero
    # -------------------------

    st.markdown("""
    <div class="hero-section">
    <h1>📊 Analytics Dashboard</h1>
    <h3>Interactive Business Intelligence</h3>
    <p>
    Explore passenger demographics, survival statistics,
    fare distribution and AI insights.
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    a1, a2, a3, a4 = st.columns(4)

    with a1:
     st.success("📈 Live Analytics")

    with a2:
     st.info("📊 Interactive Charts")

    with a3:
     st.success("🤖 AI Insights")

    with a4:
     st.warning("📂 Dataset Ready")

    st.markdown("---")
    
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Passengers", len(df))
    c2.metric("Columns", len(df.columns))
    c3.metric("Survived", int(df["Survived"].sum()))
    c4.metric(
    "Death Rate",
    f"{(1-df['Survived'].mean())*100:.1f}%"
 )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==========================
    # Filters
    # ==========================

    st.subheader("🎛 Analytics Filters")

    f1, f2 = st.columns(2)

    with f1:

      selected_class = st.multiselect(
        "Passenger Class",
        options=sorted(df["Pclass"].unique()),
        default=sorted(df["Pclass"].unique())
    )
 
    with f2:

      selected_gender = st.multiselect(
        "Gender",
        options=df["Sex"].unique(),
        default=df["Sex"].unique()
    )

    filtered_df = df[
    (df["Pclass"].isin(selected_class)) &
    (df["Sex"].isin(selected_gender))
]

    st.success(f"Showing {len(filtered_df)} passengers")

    # -------------------------
    # Row 1
    # -------------------------

    c1, c2 = st.columns(2)

    with c1:
     fig = px.pie(
         filtered_df,
        names="Survived",
        title="Survival Distribution",
        color="Survived",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, width="stretch")

    with c2:

     fig = px.histogram(
        filtered_df,
        x="Age",
        nbins=30,
        title="Age Distribution",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, width="stretch")

   # -------------------------
   # Row 2
   # -------------------------

    c1, c2 = st.columns(2)

    with c1:

     fig = px.bar(
        filtered_df,
        x="Pclass",
        color="Survived",
        title="Passenger Class vs Survival",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, width="stretch")

    with c2:

     fig = px.box(
        filtered_df,
        x="Survived",
        y="Fare",
        color="Survived",
        title="Fare Analysis",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(fig, width="stretch")

   # -------------------------
   # Row 3
   # -------------------------

    st.markdown("""
    <div class="glass-card">

    ## 🤖 AI Insights

    ✅ Female passengers had the highest survival rate.

    ✅ First-class passengers survived more frequently.

    ✅ Younger passengers generally had better survival chances.

    ✅ Higher ticket fares correlated with higher survival.

    ✅ Passenger class was one of the strongest indicators.

    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

    st.subheader("🔥 Correlation Heatmap")

    numeric_df = filtered_df.select_dtypes(include="number")

    corr = numeric_df.corr(numeric_only=True)

    fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="Blues",
    template="plotly_dark",
    aspect="auto",
    title="Feature Correlation"
  )

    fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
  )
 
    st.plotly_chart(fig, width="stretch")
    
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="glass-card">

    <h2>🤖 AI Analytics Summary</h2>

    ✔ Total Passengers : {len(filtered_df)}

    <br><br>

    ✔ Survival Rate : {(filtered_df['Survived'].mean()*100):.1f}%

    <br><br>

    ✔ Average Fare : ${filtered_df['Fare'].mean():.2f}

    <br><br>

    ✔ Average Age : {filtered_df['Age'].mean():.1f} years

    </div>
    """, unsafe_allow_html=True)
    
st.caption(
"🚀 Powered by Anusha Talawar | Titanic AI Platform | Version 2.0"
)