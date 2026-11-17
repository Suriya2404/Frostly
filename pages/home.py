
import streamlit as st
from pathlib import Path
import textwrap

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# HTML RENDERING HELPER
# ==========================================

def render_html(content):
    clean_html = "\n".join(
        line.lstrip()
        for line in content.strip().splitlines()
    )

    st.markdown(
        clean_html,
        unsafe_allow_html=True
    )


# ==========================================
# HOME PAGE DESIGN
# ==========================================

st.markdown("""
<style>

/* GLOBAL */

.stApp {
    background: #F5F9FC;
}

.block-container {
    padding-top: 2rem;
    max-width: 1250px;
}

/* HERO SECTION */

.hero {
    position: relative;
    overflow: hidden;
    background: linear-gradient(120deg, #061626, #103B59, #071C30);
    background-size: 200% 200%;
    animation: gradientMove 9s ease infinite;
    padding: 65px 45px;
    border-radius: 24px;
    min-height: 410px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 15px 45px rgba(4, 28, 48, 0.18);
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero h1 {
    font-size: 53px;
    line-height: 1.15;
    font-weight: 850;
    color: #FFFFFF !important;
    margin-bottom: 18px;
}

.hero h1 span {
    color: #42C5F5;
}

.hero p {
    color: #D2E5F2 !important;
    font-size: 18px;
    line-height: 1.7;
}

/* GLOW EFFECT */

.hero::after {
    content: "";
    position: absolute;
    width: 280px;
    height: 280px;
    border-radius: 50%;
    background: rgba(44, 174, 245, 0.12);
    filter: blur(70px);
    right: -50px;
    bottom: -80px;
    animation: glowMove 5s ease-in-out infinite alternate;
    pointer-events: none;
}

@keyframes glowMove {
    from { transform: translateY(0px); }
    to { transform: translateY(-45px); }
}

/* SECTION HEADINGS */

.section-heading {
    color: #12344B;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 10px;
}

.section-subtitle {
    color: #61798B;
    font-size: 17px;
    margin-bottom: 30px;
}

/* FEATURE CARDS */

.feature-card {
    background: #FFFFFF;
    border: 1px solid #E0EAF1;
    border-radius: 18px;
    padding: 28px 23px;
    min-height: 205px;
    transition: all 0.3s ease;
    box-shadow: 0 5px 18px rgba(18, 52, 75, 0.04);
}

.feature-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 30px rgba(18, 52, 75, 0.12);
    border-color: #65C8F0;
}

.feature-icon {
    font-size: 35px;
    margin-bottom: 15px;
}

.feature-card h3 {
    color: #12344B !important;
    font-size: 21px;
    font-weight: 750;
}

.feature-card p {
    color: #647C8D !important;
    font-size: 15px;
    line-height: 1.6;
}

/* IMAGE */

.hero-image {
    border-radius: 22px;
    overflow: hidden;
}

/* BUTTON */

div[data-testid="stButton"] button {
    background: #168BD2;
    color: white !important;
    border: none;
    border-radius: 11px;
    padding: 13px 25px;
    font-weight: 700;
    transition: all 0.25s ease;
}

div[data-testid="stButton"] button:hover {
    background: #0875B8;
    transform: translateY(-3px);
    box-shadow: 0 8px 20px rgba(22, 139, 210, 0.25);
}

/* FOOTER */

.footer {
    background: #071C30;
    border-radius: 18px;
    padding: 35px;
    text-align: center;
}

.footer h2 {
    color: white !important;
}

.footer p {
    color: #B9D0E0 !important;
}

/* DIVIDERS */

hr {
    border-color: #DCE8F0;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HERO SECTION
# ==========================================

left, right = st.columns([1.2, 1], gap="large")

with left:

    render_html("""
    <div class="hero">

        <p style="color:#42C5F5 !important;
        font-weight:700; letter-spacing:2px;">
        WELCOME TO Frostly
        </p>

        <h1>
        Find Your Cool.<br>
        <span>Upgrade Your Comfort.</span>
        </h1>

        <p>
        Quality Second-Hand Refrigerators.<br>
        Reliable Repairs. Smart Exchanges.
        </p>

        <p>
        Discover affordable refrigerators and
        dependable cooling solutions, all in one place.
        </p>

    </div>
    """)

    st.write("")

    if st.button("Explore Refrigerators →"):
        st.switch_page("pages/refrigerators.py")


with right:

    hero_image = (
        BASE_DIR / "assets" / "refrigerators" / "fridge_01.png"
    )

    if hero_image.is_file():

        st.image(
            str(hero_image),
            width="stretch"
        )

    else:
        st.warning("Hero image unavailable.")


# ==========================================
# INTRODUCTION
# ==========================================

st.write("")
st.write("")

render_html("""
<div style="text-align:center; padding:25px 10px;">

    <div style="
        color:#168BD2;
        font-size:14px;
        font-weight:800;
        letter-spacing:2px;">
        ABOUT US
    </div>

    <h2 class="section-heading">
        Welcome to Frostly
    </h2>

    <p style="
        color:#61798B;
        font-size:17px;
        max-width:750px;
        margin:auto;
        line-height:1.8;">
        We believe quality refrigerators should be accessible
        and affordable. From second-hand appliances to
        dependable repair services and smart exchanges,
        we're here to make your cooling experience better.
    </p>

</div>
""")


st.write("")
st.divider()


# ==========================================
# WHAT WE OFFER
# ==========================================

render_html("""
<h2 class="section-heading">What We Offer</h2>

<p class="section-subtitle">
Everything you need for a better cooling experience.
</p>
""")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:

    render_html("""
    <div class="feature-card">

        <div class="feature-icon">❄️</div>

        <h3>Refrigerators</h3>

        <p>
        Explore quality second-hand refrigerators
        at affordable prices.
        </p>

    </div>
    """)

    st.write("")

    if st.button("Browse Products →", key="home_products"):
        st.switch_page("pages/refrigerators.py")


with col2:

    render_html("""
    <div class="feature-card">

        <div class="feature-icon">🔄</div>

        <h3>Smart Exchange</h3>

        <p>
        Exchange your old refrigerator and
        discover better upgrade options.
        </p>

    </div>
    """)

    st.write("")

    if st.button("Explore Exchange →", key="home_exchange"):
        st.switch_page("pages/exchange.py")


with col3:

    render_html("""
    <div class="feature-card">

        <div class="feature-icon">🔧</div>

        <h3>Repair Services</h3>

        <p>
        Get dependable refrigerator repair
        and maintenance solutions.
        </p>

    </div>
    """)

    st.write("")

    if st.button("Our Services →", key="home_services"):
        st.switch_page("pages/services.py")


# ==========================================
# FOOTER
# ==========================================

st.write("")
st.write("")

render_html("""
<div class="footer">

    <h2>❄️ Frostly</h2>

    <p>
    Find Your Cool. Upgrade Your Comfort.
    </p>

    <p>
    Quality Refrigerators | Reliable Repairs |
    Smart Exchanges
    </p>

    <p style="font-size:13px;">
    © 2026 Frostly. All Rights Reserved.
    </p>

</div>
""")
