with st.sidebar:

    st.image("assets/images/logo.png", width=120)

    st.markdown("<h2 style='text-align:center;'>Titanic AI</h2>", unsafe_allow_html=True)

    st.markdown("---")

    page = st.radio(
        "",
        [
            "🏠 Dashboard",
            "📄 Dataset",
            "📊 Analytics",
            "🤖 Prediction",
            "🧠 Machine Learning",
            "📈 Model Performance",
            "📚 About Project"
        ]
    )

    st.markdown("---")

    st.markdown("### 👨‍💻 Developed By")
    st.write("Anusha Talawar")

    st.markdown("### 🎓 Project")
    st.write("Titanic Survival Prediction")

    st.markdown("### ⚙ Version")
    st.write("v2.0 Professional")