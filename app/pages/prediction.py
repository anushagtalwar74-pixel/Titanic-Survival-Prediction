import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
from pathlib import Path

# =====================================================
# PREDICTION PAGE
# =====================================================

def app():

    # -----------------------------
    # Load Model
    # -----------------------------
    model_path = Path("models/titanic_model.pkl")

    if not model_path.exists():
        model_path = Path("outputs/models/titanic_model.pkl")

    if not model_path.exists():
        st.error("❌ Trained model not found.")
        st.info("Train the model first or place titanic_model.pkl inside models/")
        st.stop()

    model = joblib.load(model_path)

    # -----------------------------
    # Session State
    # -----------------------------
    if "history" not in st.session_state:
        st.session_state.history = []

    # -----------------------------
    # Hero
    # -----------------------------
    st.markdown("""
    <div class="hero-section">

    <h1>🤖 AI Survival Prediction</h1>

    <h3>Machine Learning Prediction System</h3>

    <p>
    Predict whether a passenger would survive using a trained Machine Learning model.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # ==========================
 # AI STATUS CARDS
 # ==========================

    a1, a2, a3, a4 = st.columns(4)

    with a1:
      st.success("🧠 AI Model Online")

    with a2:
     st.info("⚡ Real-Time Prediction")

    with a3:
     st.success("📊 Confidence Analysis")

    with a4:
     st.warning("🚢 Titanic Dataset")
     
    with st.expander("💡 Prediction Tips"):

     st.write("""
     - First-class passengers generally had higher survival chances.
     - Female passengers survived more frequently.
     - Younger passengers often had better survival rates.
     - Ticket fare and passenger class influence predictions.
     - The AI analyzes all features together before predicting.
      """)

      # -----------------------------
      # Top Cards
      # -----------------------------
     c1, c2, c3 = st.columns(3)

     with c1:
        st.success("🤖 AI Model Ready")

     with c2:
        st.info("📊 Prediction Engine")

     with c3:
        st.success("⚡ Real-Time")

     st.markdown("---")


     st.markdown("""
     <div class="glass-card">

     <h2>📝 Passenger Information</h2>

     <p>
     Fill in the passenger details below.
     The AI model will instantly predict the survival probability.
     </p>

     </div>
     """, unsafe_allow_html=True)

     st.markdown("<br>", unsafe_allow_html=True)
     # -----------------------------
     # Layout
     # -----------------------------
     left, right = st.columns([1.3, 1])

     with left:

        st.subheader("Passenger Information")

        pclass = st.selectbox(
            "Passenger Class",
            [1, 2, 3]
        )

        sex = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        age = st.slider(
            "Age",
            1,
            80,
            30
        )

        sibsp = st.slider(
            "Siblings / Spouse",
            0,
            8,
            0
        )

        parch = st.slider(
            "Parents / Children",
            0,
            6,
            0
        )

        fare = st.slider(
            "Fare",
            0.0,
            550.0,
            50.0
        )

        embarked = st.selectbox(
            "Embarked",
            ["S", "C", "Q"]
        )

     with right:

        st.markdown("""
        <div class="glass-card">

        <h3>📘 AI Guide</h3>

        ✔ Fill passenger details

        ✔ Click Predict

        ✔ AI calculates survival probability

        ✔ Confidence score displayed

        ✔ Prediction stored in history

        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>")

        st.metric("Model Status", "Ready")

        st.metric("Prediction Mode", "Binary Classification")

        st.metric("Output", "Survived / Not Survived")
        
        st.markdown("""
        <div class="glass-card">

        <h2>🧠 AI Model Information</h2>

        <b>Algorithm:</b> Random Forest Classifier

        <br><br>

        <b>Input Features:</b> 10

        <br><br>

        <b>Output:</b> Survival Prediction

        <br><br>

        <b>Status:</b> 🟢 Online

        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        predict = st.button(
        "🚀 Predict Survival",
        width="stretch"
       )

     if predict:
        
        with st.spinner("🤖 AI is analyzing passenger data..."):
           import time
        time.sleep(1.5)

        # Match preprocessing encoding
        sex_value = 0 if sex == "Male" else 1

        embarked_map = {
            "S": 0,
            "C": 1,
            "Q": 2
        }

        embarked_value = embarked_map[embarked]
        # -----------------------------
       # Additional engineered features
     # -----------------------------

        family_size = sibsp + parch + 1

        is_alone = 1 if family_size == 1 else 0

        # Title encoding

        title_map = {
        "Male": 0,     # Mr
        "Female": 2    # Mrs (simple mapping)
        }

        title = title_map[sex]

        X = np.array([[
        pclass,
        sex_value,
        age,
        sibsp,
        parch,
        fare,
        embarked_value,
        family_size,
        is_alone,
        title
       ]])

        prediction = model.predict(X)[0]

        probability = model.predict_proba(X)[0]

        confidence = float(max(probability))

        st.markdown("## 🎯 Prediction Result")
                # -----------------------------
        # Prediction Result
        # -----------------------------

        if prediction == 1:

            st.success("🎉 Passenger is likely to SURVIVE")
            st.balloons()

            st.toast(
              "Prediction Completed Successfully!",
               icon="🤖"
              )

            st.balloons()

            result = "Survived"

        else:

            st.error("⚠ Passenger is unlikely to SURVIVE")
            st.toast(
            "Prediction Completed Successfully!",
              icon="🤖"
             )

            result = "Not Survived"
            
            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(f"""
            <div class="glass-card">

            <h2>🤖 AI Decision</h2>

            <b>Prediction:</b> {result}

            <br><br>

            <b>Confidence:</b> {confidence*100:.2f}%
  
            </div>
             """, unsafe_allow_html=True)

            st.metric(
            "Prediction Confidence",
            f"{confidence*100:.2f}%"
           )

            st.progress(confidence)

        # -----------------------------
         # Gauge Chart
         # -----------------------------

            gauge = go.Figure(go.Indicator(

             mode="gauge+number",

             value=confidence*100,

             title={"text":"AI Confidence"},

             gauge={

                "axis":{"range":[0,100]},

                "bar":{"color":"royalblue"},

                "steps":[

                    {"range":[0,40],"color":"#ffb3b3"},

                    {"range":[40,70],"color":"#ffe699"},

                    {"range":[70,100],"color":"#b6fcb6"}

                ]

            }

        ))

        gauge.update_layout(
            height=350,
            margin=dict(l=20,r=20,t=60,b=20)
        )

        st.plotly_chart(gauge, width="stretch")

        # -----------------------------
        # Probability Chart
        # -----------------------------

        fig = go.Figure()

        fig.add_bar(
            x=["Not Survived","Survived"],
            y=probability,
            text=[f"{i*100:.1f}%" for i in probability],
            textposition="outside"
        )

        fig.update_layout(

            title="Prediction Probability",

            template="plotly_dark",

            height=400

        )

        st.plotly_chart(fig, width="stretch")

        # -----------------------------
        # Save History
        # -----------------------------

        st.session_state.history.append({

            "Class": pclass,

            "Gender": sex,

            "Age": age,

            "Fare": fare,

            "Prediction": result,

            "Confidence": f"{confidence*100:.2f}%"

        })

        # -----------------------------
        # AI Explanation
        # -----------------------------

        st.markdown("""
        <div class="glass-card">

        <h3>🤖 AI Decision</h3>

        The Machine Learning model analyzed all passenger
        attributes and predicted survival based on patterns
        learned from the Titanic dataset.

        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
         <hr style="
           border:1px solid rgba(255,255,255,.12);
           margin-top:40px;
         margin-bottom:25px;
           ">
           """, unsafe_allow_html=True)
        
     # =====================================================
      # Prediction History
     # =====================================================

     if st.session_state.history:

      st.markdown("---")

      st.subheader("📜 Prediction History")

      history = pd.DataFrame(st.session_state.history)

      st.dataframe(history, width="stretch")

      csv = history.to_csv(index=False)

      st.download_button(

        "📥 Download Prediction History",

        csv,

        file_name="prediction_history.csv",

        mime="text/csv"

     )

     # =====================================================
     # Help
      # =====================================================

     with st.expander("ℹ How does the AI model work?"):

      st.write("""

        The model uses these features:

         • Passenger Class

         • Gender

         • Age

         • Fare

         • Siblings / Spouse

          • Parents / Children

          • Embarked Port

          It predicts survival using a trained Machine Learning classification model.

          """)
from datetime import datetime

st.markdown("---")

c1, c2 = st.columns([3,1])

with c1:
    st.caption("🤖 Titanic AI • Enterprise Prediction System")

with c2:
    st.caption(datetime.now().strftime("%d %b %Y"))
    
st.caption(
"🚀 Powered by Anusha Talawar | Titanic AI Platform | Version 2.0"
)