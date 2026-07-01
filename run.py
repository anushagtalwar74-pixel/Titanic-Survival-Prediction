import time
from pathlib import Path

import streamlit as st

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Titanic AI Platform",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
[data-testid="collapsedControl"]{
    display:block !important;
    visibility:visible !important;
    opacity:1 !important;
}

section[data-testid="stSidebar"]{
    min-width:320px !important;
    max-width:320px !important;
}
</style>
""", unsafe_allow_html=True)

# ==============================
# LOADING SCREEN
# ==============================
st.markdown("""
<div class="loading-screen">

<div class="ship">
🚢
</div>

<h1>Titanic AI Platform</h1>

<p>Loading Enterprise Dashboard...</p>

<div class="loader"></div>

</div>
""", unsafe_allow_html=True)

time.sleep(2)

st.empty()

# ==============================
# LOAD CSS
# ==============================

css_path = Path("assets/css/style.css")

if css_path.exists():
    with open(css_path, encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
        
st.markdown("""
<div class="background-grid"></div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="cursor-glow"></div>

<script>

const glow=document.querySelector(".cursor-glow");

document.addEventListener("mousemove",(e)=>{

glow.style.left=e.clientX+"px";
glow.style.top=e.clientY+"px";

});

</script>
""", unsafe_allow_html=True)
# ==============================
# WELCOME TOAST
# ==============================

if "welcome" not in st.session_state:
    st.session_state.welcome = True
    st.toast(
        "🚢 Welcome to Titanic AI Platform",
        icon="🎉"
    )

# ==============================
# SIDEBAR
# ==============================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center">

        <h1>🚢 Titanic AI</h1>

        <p style="color:#9db4d3;">
        Enterprise ML Platform
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    page = st.radio(
        "Navigation",
       [
     "🏠 Dashboard",
     "📊 Analytics",
     "📂 Dataset",
     "🤖 Prediction",
     "🧠 Model",
     "📈 Visualization",
     "ℹ About"
        ]
    )

    st.divider()

    st.success("🤖 AI Model Loaded")

    st.write("Model Accuracy")

    st.progress(0.96)

    st.divider()

    st.info(
        """
### 👩‍💻 Developer

**Anusha Talawar**

AI & ML Enthusiast

Python | Machine Learning | Streamlit
"""
    )

    st.divider()

    st.caption("Version 2.0")

    st.caption("© 2026 Titanic AI Platform")

# ==============================
# LOAD PAGES
# ==============================

if page == "🏠 Dashboard":

    from app.pages.dashboard import app

    app()

elif page == "📊 Analytics":

    from app.pages.analytics import app

    app()

elif page == "📂 Dataset":

    from app.pages.dataset import app

    app()

elif page == "🤖 Prediction":

    from app.pages.prediction import app

    app()

elif page == "🧠 Model":

    from app.pages.model import app

    app()

elif page == "📈 Visualization":

    from app.pages.visualization import app

    app()

elif page == "ℹ About":

    from app.pages.about import app

    app()

# ==============================
# FOOTER
# ==============================
st.markdown(
    """
<div class="enterprise-footer">

<h3>🚢 Titanic AI Platform</h3>

<p>
Enterprise Machine Learning Dashboard
</p>

<p>
Python • Streamlit • Plotly • Scikit-Learn
</p>

</div>
""",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
<hr>

<div style="text-align:center;color:#9db4d3">

🚢 Titanic AI Platform

Built using

Python • Streamlit • Plotly • Scikit-Learn

Version 2.0

</div>
""",
    unsafe_allow_html=True
)
st.markdown(
"""
<div class="loading-overlay">

🚢

</div>
""",
unsafe_allow_html=True)