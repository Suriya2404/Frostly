
import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Frostly",
    page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# GLOBAL STYLING
# ==========================================

st.markdown("""
<style>

.stApp {
    background-color: #F7FBFE;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #12344B !important;
}

p {
    color: #526C7E;
}

[data-testid="stHeader"] {
    display: none;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stAppDeployButton"] {
    display: none;
}

[data-testid="stSidebar"] {
    display: none;
}

div[data-testid="stButton"] button {
    background-color: #168BD2;
    color: white !important;
    border: none;
    border-radius: 10px;
    font-weight: 700;
}

div[data-testid="stButton"] button:hover {
    background-color: #0875B8;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# PAGE DEFINITIONS
# ==========================================

home_page = st.Page(
    "pages/home.py",
    title="Home",
    icon="🏠",
    default=True
)

refrigerators_page = st.Page(
    "pages/refrigerators.py",
    title="Refrigerators",
    icon="🧊"
)

exchange_page = st.Page(
    "pages/exchange.py",
    title="Exchange",
    icon="🔄"
)

spare_parts_page = st.Page(
    "pages/spare_parts.py",
    title="Spare Parts",
    icon="⚙️"
)

services_page = st.Page(
    "pages/services.py",
    title="Services",
    icon="🔧"
)

contact_page = st.Page(
    "pages/contact.py",
    title="Contact",
    icon="📞"
)


# ==========================================
# NAVIGATION
# ==========================================

pages = st.navigation(
    {
        "Frostly": [
            home_page,
            refrigerators_page,
            exchange_page,
            spare_parts_page,
            services_page,
            contact_page
        ]
    },
    position="hidden"
)


# ==========================================
# CUSTOM TOP NAVIGATION BAR
# ==========================================

logo, home, products, exchange, parts, services, contact = st.columns(
    [2.2, 0.8, 1.2, 1, 1.2, 1, 0.9]
)

with logo:
    st.image("assets/logo.png", width=180)

with home:
    if st.button("Home", use_container_width=True):
        st.switch_page("pages/home.py")

with products:
    if st.button("Refrigerators", use_container_width=True):
        st.switch_page("pages/refrigerators.py")

with exchange:
    if st.button("Exchange", use_container_width=True):
        st.switch_page("pages/exchange.py")

with parts:
    if st.button("Spare Parts", use_container_width=True):
        st.switch_page("pages/spare_parts.py")

with services:
    if st.button("Services", use_container_width=True):
        st.switch_page("pages/services.py")

with contact:
    if st.button("Contact", use_container_width=True):
        st.switch_page("pages/contact.py")

st.divider()


# ==========================================
# DISPLAY SELECTED PAGE
# ==========================================

pages.run()
