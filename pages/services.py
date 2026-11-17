
import streamlit as st
from pathlib import Path

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
# SERVICES PAGE DESIGN
# ==========================================

st.markdown("""
<style>

/* PAGE BACKGROUND */

.stApp {
    background: #F5F9FC;
}

/* HERO SECTION */

.services-hero {
    background: linear-gradient(
        120deg,
        #061626,
        #103B59,
        #0875B8
    );
    padding: 48px 40px;
    border-radius: 22px;
    margin-bottom: 30px;
    animation: fadeIn 0.8s ease;
}

.services-hero h1 {
    color: #FFFFFF !important;
    font-size: 39px;
    font-weight: 850;
}

.services-hero p {
    color: #D5EAF7 !important;
    font-size: 16px;
}

.services-label {
    color: #62D6FF !important;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}

/* SERVICE CARDS */

.service-card {
    background: #FFFFFF;
    border: 1px solid #E0EAF1;
    border-radius: 18px;
    padding: 25px;
    min-height: 235px;
    box-shadow: 0 5px 18px rgba(18, 52, 75, 0.04);
    transition: all 0.3s ease;
}

.service-card:hover {
    transform: translateY(-5px);
    border-color: #66C8EF;
    box-shadow: 0 12px 28px rgba(18, 52, 75, 0.10);
}

.service-card h3 {
    color: #12344B !important;
    font-size: 20px;
}

.service-card p {
    color: #61798B !important;
    font-size: 14px;
    line-height: 1.9;
}

/* SECTION HEADINGS */

.services-heading {
    color: #12344B;
    font-size: 27px;
    font-weight: 850;
}

.services-description {
    color: #61798B;
    font-size: 14px;
}

/* TECHNICIAN IMAGE */

div[data-testid="stImage"] img {
    border-radius: 18px;
}

/* FORM BUTTON */

div[data-testid="stFormSubmitButton"] button {
    background: #168BD2 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 800 !important;
    min-height: 45px;
    transition: all 0.25s ease;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: #0875B8 !important;
    transform: translateY(-2px);
}

/* FOOTER */

.services-footer {
    background: #071C30;
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    margin-top: 35px;
}

.services-footer h3 {
    color: white !important;
}

.services-footer p {
    color: #B9D0E0 !important;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(12px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# HERO SECTION
# ==========================================

render_html("""
<div class="services-hero">

    <div class="services-label">
        EXPERT CARE. RELIABLE COOLING.
    </div>

    <h1>Professional Refrigerator Repair Services.</h1>

    <p>
        From cooling problems to electrical faults,
        explore our repair and maintenance services
        to keep your refrigerator running smoothly.
    </p>

</div>
""")


# ==========================================
# TECHNICIAN IMAGE
# ==========================================

technician_image = (
    BASE_DIR / "assets" / "service_technician.png"
)

if technician_image.is_file():

    st.image(
        str(technician_image),
        caption="Refrigerator repair and maintenance",
        width="stretch"
    )


# ==========================================
# OUR SERVICES
# ==========================================

st.markdown(
    '<div class="services-heading">What We Offer</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="services-description">'
    'Explore our refrigerator repair and maintenance services.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

col1, col2 = st.columns(2, gap="medium")

with col1:

    render_html("""
    <div class="service-card">

        <h3>❄️ Cooling Problems</h3>

        <p>
            • Refrigerator not cooling<br>
            • Freezer not freezing<br>
            • Temperature issues<br>
            • Excessive ice formation
        </p>

    </div>
    """)

    st.write("")

    render_html("""
    <div class="service-card">

        <h3>🔌 Electrical Repairs</h3>

        <p>
            • Compressor-related issues<br>
            • Thermostat problems<br>
            • Wiring and electrical faults<br>
            • Control board issues
        </p>

    </div>
    """)


with col2:

    render_html("""
    <div class="service-card">

        <h3>💧 General Repairs</h3>

        <p>
            • Water leakage<br>
            • Unusual noises<br>
            • Door gasket replacement<br>
            • Door and hinge problems
        </p>

    </div>
    """)

    st.write("")

    render_html("""
    <div class="service-card">

        <h3>🧰 Maintenance</h3>

        <p>
            • General refrigerator inspection<br>
            • Cleaning and maintenance<br>
            • Cooling performance checks<br>
            • Preventive maintenance
        </p>

    </div>
    """)


# ==========================================
# SERVICE REQUEST FORM
# ==========================================

st.write("")
st.write("")

st.markdown(
    '<div class="services-heading">Request a Repair Service</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="services-description">'
    'Tell us about your refrigerator issue and your team can review your enquiry.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

with st.container(border=True):

    with st.form("service_form"):

        st.markdown("### Personal Information")

        name_col, phone_col = st.columns(2)

        with name_col:

            customer_name = st.text_input(
                "Full Name",
                placeholder="Enter your full name"
            )

        with phone_col:

            phone = st.text_input(
                "Phone Number",
                placeholder="Enter your contact number"
            )

        st.divider()

        st.markdown("### Refrigerator Information")

        brand_col, issue_col = st.columns(2)

        with brand_col:

            brand = st.selectbox(
                "Refrigerator Brand",
                [
                    "Samsung",
                    "LG",
                    "Whirlpool",
                    "Godrej",
                    "Haier",
                    "Other"
                ]
            )

        with issue_col:

            issue = st.selectbox(
                "What is the problem?",
                [
                    "Not Cooling",
                    "Water Leakage",
                    "Unusual Noise",
                    "Freezer Problem",
                    "Electrical Issue",
                    "Compressor Issue",
                    "Other"
                ]
            )

        st.divider()

        st.markdown("### Service Location")

        address = st.text_area(
            "Service Address",
            placeholder="Enter your complete address..."
        )

        description = st.text_area(
            "Describe the Problem",
            placeholder=(
                "Explain the issue and any symptoms "
                "you have noticed..."
            ),
            height=110
        )

        st.write("")

        submitted = st.form_submit_button(
            "Submit Service Enquiry →",
            width="stretch"
        )

        if submitted:

            if customer_name.strip() and phone.strip():

                st.success(
                    "Thank you! Your service enquiry details "
                    "have been prepared. The form is currently "
                    "a demo and does not send or store submissions yet."
                )

            else:

                st.warning(
                    "Please enter your name and phone number."
                )


# ==========================================
# FOOTER
# ==========================================

render_html("""
<div class="services-footer">

    <h3>❄️ Frostly</h3>

    <p>Reliable Repairs. Dependable Cooling.</p>

    <p>Find Your Cool. Save More.</p>

</div>
""")
