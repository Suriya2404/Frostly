
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
# SPARE PARTS PAGE DESIGN
# ==========================================

st.markdown("""
<style>

/* PAGE BACKGROUND */

.stApp {
    background: #F5F9FC;
}

/* HERO */

.parts-hero {
    background: linear-gradient(
        120deg,
        #061626,
        #103B59,
        #0875B8
    );
    padding: 45px 40px;
    border-radius: 22px;
    margin-bottom: 30px;
    animation: fadeIn 0.8s ease;
}

.parts-hero h1 {
    color: white !important;
    font-size: 39px;
    font-weight: 850;
}

.parts-hero p {
    color: #D5EAF7 !important;
    font-size: 16px;
}

.parts-label {
    color: #62D6FF !important;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 2px;
}

/* CATEGORY CARDS */

.parts-card {
    background: #FFFFFF;
    border: 1px solid #E0EAF1;
    padding: 25px;
    border-radius: 18px;
    min-height: 250px;
    box-shadow: 0 5px 18px rgba(18, 52, 75, 0.04);
    transition: all 0.3s ease;
}

.parts-card:hover {
    transform: translateY(-5px);
    border-color: #66C8EF;
    box-shadow: 0 12px 28px rgba(18, 52, 75, 0.10);
}

.parts-card h3 {
    color: #12344B !important;
    font-size: 20px;
}

.parts-card p {
    color: #61798B !important;
    font-size: 14px;
    line-height: 1.9;
}

.parts-heading {
    color: #12344B;
    font-size: 27px;
    font-weight: 850;
}

.parts-description {
    color: #61798B;
    font-size: 14px;
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

.parts-footer {
    background: #071C30;
    padding: 30px;
    border-radius: 18px;
    text-align: center;
    margin-top: 35px;
}

.parts-footer h3 {
    color: white !important;
}

.parts-footer p {
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
<div class="parts-hero">

    <div class="parts-label">
        GENUINE REQUIREMENTS. RELIABLE SUPPORT.
    </div>

    <h1>Find the Right Parts for Your Refrigerator.</h1>

    <p>
        Looking for replacement components?
        Explore our spare parts categories and
        tell us what your refrigerator needs.
    </p>

</div>
""")


# ==========================================
# SPARE PART CATEGORIES
# ==========================================

st.markdown(
    '<div class="parts-heading">Explore Spare Parts</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="parts-description">'
    'Browse the major refrigerator component categories.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

col1, col2, col3 = st.columns(3, gap="medium")

with col1:

    render_html("""
    <div class="parts-card">

        <h3>❄️ Cooling Components</h3>

        <p>
            • Compressor<br>
            • Condenser<br>
            • Evaporator<br>
            • Cooling Fan
        </p>

    </div>
    """)


with col2:

    render_html("""
    <div class="parts-card">

        <h3>🔌 Electrical Components</h3>

        <p>
            • Thermostat<br>
            • Temperature Sensor<br>
            • Control Board<br>
            • Start Relay
        </p>

    </div>
    """)


with col3:

    render_html("""
    <div class="parts-card">

        <h3>🚪 External Components</h3>

        <p>
            • Refrigerator Handles<br>
            • Door Gaskets<br>
            • Shelves<br>
            • Door Trays
        </p>

    </div>
    """)


# ==========================================
# SPARE PART ENQUIRY FORM
# ==========================================

st.write("")
st.write("")

st.markdown(
    '<div class="parts-heading">Request a Spare Part</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="parts-description">'
    'Share your refrigerator details and the component you need.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")

with st.container(border=True):

    with st.form("spare_parts_form"):

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

        st.markdown("### Refrigerator Details")

        brand_col, model_col = st.columns(2)

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

        with model_col:

            model = st.text_input(
                "Refrigerator Model",
                placeholder="Enter model if known"
            )

        part = st.selectbox(
            "Select Spare Part",
            [
                "Compressor",
                "Condenser",
                "Evaporator",
                "Cooling Fan",
                "Thermostat",
                "Temperature Sensor",
                "Control Board",
                "Start Relay",
                "Door Gasket",
                "Handle",
                "Shelf",
                "Other"
            ]
        )

        st.divider()

        st.markdown("### Additional Requirements")

        description = st.text_area(
            "Describe the part or issue",
            placeholder=(
                "Tell us more about the component "
                "you need or the problem you are facing..."
            ),
            height=110
        )

        st.write("")

        submitted = st.form_submit_button(
            "Submit Spare Parts Enquiry →",
            width="stretch"
        )

        if submitted:

            if customer_name.strip() and phone.strip():

                st.success(
                    "Thank you! Your spare parts enquiry "
                    "details have been prepared. The form is "
                    "currently a demo and does not send or "
                    "store submissions yet."
                )

            else:

                st.warning(
                    "Please enter your name and phone number."
                )


# ==========================================
# FOOTER
# ==========================================

render_html("""
<div class="parts-footer">

    <h3>❄️ Frostly</h3>

    <p>Quality Parts. Reliable Cooling.</p>

    <p>Find Your Cool. Save More.</p>

</div>
""")
