
import streamlit as st

# ==========================================
# CONTACT PAGE
# ==========================================

st.markdown("# 📞 Contact Frostly")

st.write(
    "Have questions about refrigerators, repairs, "
    "exchanges or spare parts? We'd love to hear from you."
)

st.divider()

# CONTACT INFORMATION

st.markdown("## We're Here to Help")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📱 Phone")
    st.write("Add your business phone number")

with col2:
    st.markdown("### 💬 WhatsApp")
    st.write("Connect with us for enquiries")

with col3:
    st.markdown("### 🔧 Support")
    st.write("Refrigerators, repairs and exchanges")

st.divider()

# CONTACT FORM

st.markdown("## Send Us an Enquiry")

with st.form("contact_form"):

    name = st.text_input("Your Name")

    phone = st.text_input("Phone Number")

    email = st.text_input("Email Address")

    enquiry_type = st.selectbox(
        "Enquiry Type",
        [
            "Refrigerator Purchase",
            "Exchange",
            "Spare Parts",
            "Repair Services",
            "General Enquiry"
        ]
    )

    message = st.text_area("Your Message")

    submitted = st.form_submit_button("Submit Enquiry")

    if submitted:

        if name.strip() and phone.strip():

            st.success(
                "Thank you for contacting Frostly! "
                "Your enquiry is ready for processing."
            )

        else:

            st.warning(
                "Please enter your name and phone number."
            )

# FOOTER

st.divider()

st.markdown("""
<div style="text-align:center; padding:20px;">
    <h3>❄️ Frostly</h3>
    <p>Find Your Cool. Save More.</p>
    <p>Quality Refrigerators. Reliable Repairs.</p>
    <p>© 2026 Frostly. All Rights Reserved.</p>
</div>
""", unsafe_allow_html=True)
