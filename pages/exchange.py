
import streamlit as st


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
# EXCHANGE PAGE DESIGN
# ==========================================

st.markdown("""
<style>

/* PAGE BACKGROUND */

.stApp {
    background: #F5F9FC;
}

/* HERO SECTION */

.exchange-hero {
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

.exchange-hero h1 {
    color: #FFFFFF !important;
    font-size: 40px;
    font-weight: 850;
}

.exchange-hero p {
    color: #D5EAF7 !important;
    font-size: 16px;
    max-width: 700px;
}

.exchange-label {
    color: #62D6FF !important;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}

/* PROCESS CARDS */

.step-card {
    background: #FFFFFF;
    border: 1px solid #E0EAF1;
    padding: 25px;
    border-radius: 18px;
    min-height: 165px;
    box-shadow: 0 5px 18px rgba(18, 52, 75, 0.04);
    transition: all 0.3s ease;
}

.step-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 28px rgba(18, 52, 75, 0.10);
    border-color: #66C8EF;
}

.step-number {
    color: #168BD2;
    font-size: 13px;
    font-weight: 850;
    letter-spacing: 1px;
}

.step-card h3 {
    color: #12344B !important;
    font-size: 20px;
}

.step-card p {
    color: #61798B !important;
    font-size: 14px;
}

/* FORM INTRO */

.form-heading {
    color: #12344B;
    font-size: 27px;
    font-weight: 850;
}

.form-description {
    color: #61798B;
    font-size: 14px;
}

/* BUTTON */

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

.exchange-footer {
    background: #071C30;
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    margin-top: 35px;
}

.exchange-footer h3 {
    color: white !important;
}

.exchange-footer p {
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
<div class="exchange-hero">

    <div class="exchange-label">
        SMARTER EXCHANGE. BETTER COMFORT.
    </div>

    <h1>Exchange Your Old. Upgrade Your Cool.</h1>

    <p>
        Thinking about upgrading your refrigerator?
        Tell us about your existing appliance and
        explore exchange possibilities with
        Frostly.
    </p>

</div>
""")


# ==========================================
# HOW IT WORKS
# ==========================================

st.markdown(
    '<div class="form-heading">How Our Exchange Process Works</div>',
    unsafe_allow_html=True
)

st.write("")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:

    render_html("""
    <div class="step-card">
        <div class="step-number">STEP 01</div>
        <h3>📝 Share Details</h3>
        <p>
            Tell us about your existing refrigerator,
            its age, brand and current condition.
        </p>
    </div>
    """)


with col2:

    render_html("""
    <div class="step-card">
        <div class="step-number">STEP 02</div>
        <h3>🔍 Get an Evaluation</h3>
        <p>
            Our team will review the information
            and discuss possible exchange options.
        </p>
    </div>
    """)


with col3:

    render_html("""
    <div class="step-card">
        <div class="step-number">STEP 03</div>
        <h3>❄️ Explore Your Upgrade</h3>
        <p>
            Discover suitable refrigerators and
            discuss your next upgrade with us.
        </p>
    </div>
    """)


# ==========================================
# EXCHANGE FORM
# ==========================================

st.write("")
st.write("")

st.markdown(
    '<div class="form-heading">Request Your Refrigerator Exchange</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="form-description">'
    'Fill in the details below so our team can understand your requirements.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

with st.container(border=True):

    with st.form("exchange_form"):

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

        st.markdown("### Existing Refrigerator Details")

        brand_col, type_col = st.columns(2)

        with brand_col:
            brand = st.selectbox(
                "Current Refrigerator Brand",
                [
                    "Samsung",
                    "LG",
                    "Whirlpool",
                    "Godrej",
                    "Haier",
                    "Other"
                ]
            )

        with type_col:
            refrigerator_type = st.selectbox(
                "Refrigerator Type",
                [
                    "Single Door",
                    "Double Door",
                    "Side-by-Side",
                    "French Door",
                    "Other"
                ]
            )

        age_col, condition_col = st.columns(2)

        with age_col:
            age = st.selectbox(
                "Approximate Refrigerator Age",
                [
                    "Less than 1 year",
                    "1-3 years",
                    "3-5 years",
                    "5-8 years",
                    "More than 8 years"
                ]
            )

        with condition_col:
            condition = st.selectbox(
                "Current Condition",
                [
                    "Excellent",
                    "Good",
                    "Average",
                    "Needs Repair"
                ]
            )

        st.divider()

        st.markdown("### Additional Information")

        message = st.text_area(
            "Tell us more about your refrigerator",
            placeholder=(
                "Mention any issues, model details "
                "or exchange preferences..."
            ),
            height=110
        )

        st.write("")

        submitted = st.form_submit_button(
            "Submit Exchange Request →",
            width="stretch"
        )

        if submitted:

            if customer_name.strip() and phone.strip():

                st.success(
                    "Thank you! Your exchange request details "
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
<div class="exchange-footer">

    <h3>❄️ Frostly</h3>

    <p>Exchange Your Old. Upgrade Your Cool.</p>

    <p>Find Your Cool. Save More.</p>

</div>
""")
