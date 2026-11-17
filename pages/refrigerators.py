
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
# REFRIGERATOR CATALOGUE
# ==========================================

st.markdown("""
<style>

/* PAGE BACKGROUND */

.stApp {
    background: #F5F9FC;
}

/* PAGE HERO */

.catalogue-hero {
    background: linear-gradient(120deg, #EAF7FF, #D5EFFF);
    padding: 38px;
    border-radius: 20px;
    margin-bottom: 25px;
}

.catalogue-hero h1 {
    color: #12344B !important;
    font-size: 38px;
    font-weight: 850;
}

.catalogue-hero p {
    color: #526C7E !important;
    font-size: 16px;
}

/* PRODUCT CARDS */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #FFFFFF;
    border: 1px solid #E0EAF1;
    border-radius: 18px;
    padding: 12px;
    transition: all 0.3s ease;
    box-shadow: 0 5px 18px rgba(18, 52, 75, 0.04);
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: #66C8EF;
    box-shadow: 0 12px 28px rgba(18, 52, 75, 0.10);
    transform: translateY(-4px);
}

/* PRODUCT TEXT */

.product-name {
    color: #12344B;
    font-size: 22px;
    font-weight: 800;
    line-height: 1.35;
    margin-bottom: 8px;
}

.product-rating {
    color: #E5A000;
    font-size: 23px;
    letter-spacing: 2px;
}

.rating-number {
    color: #526C7E;
    font-size: 14px;
    font-weight: 600;
}

.product-condition {
    display: inline-block;
    background: #E5F8ED;
    color: #087A3B;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 800;
}

.product-capacity {
    color: #61798B;
    font-size: 14px;
}

.product-price {
    color: #12344B;
    font-size: 29px;
    font-weight: 850;
    margin-top: 10px;
}

.product-label {
    color: #168BD2;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
}

/* BUTTONS */

div[data-testid="stButton"] button {
    background: #168BD2 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 750 !important;
    transition: all 0.25s ease;
}

div[data-testid="stButton"] button:hover {
    background: #0875B8 !important;
    transform: translateY(-2px);
    box-shadow: 0 7px 16px rgba(22, 139, 210, 0.2);
}

/* FOOTER */

.catalogue-footer {
    background: #071C30;
    padding: 30px;
    border-radius: 18px;
    text-align: center;
}

.catalogue-footer h3 {
    color: white !important;
}

.catalogue-footer p {
    color: #B9D0E0 !important;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# PAGE HEADER
# ==========================================

render_html("""
<div class="catalogue-hero">

    <p style="
        color:#168BD2 !important;
        font-weight:800;
        letter-spacing:2px;">
        OUR COLLECTION
    </p>

    <h1>Find Your Perfect Refrigerator.</h1>

    <p>
        Explore quality second-hand refrigerators
        at affordable prices.
        Find the right fit for your home.
    </p>

</div>
""")


# ==========================================
# PRODUCT DATABASE
# ==========================================

products = [

    {
        "name": "Samsung Double Door Refrigerator",
        "image": "fridge_01.png",
        "rating": 4.6,
        "reviews": 128,
        "condition": "Refurbished",
        "price": "₹12,999",
        "capacity": "253 L",
        "category": "Double Door"
    },

    {
        "name": "LG Double Door Refrigerator",
        "image": "fridge_02.png",
        "rating": 4.5,
        "reviews": 97,
        "condition": "Used - Excellent",
        "price": "₹11,499",
        "capacity": "260 L",
        "category": "Double Door"
    },

    {
        "name": "Whirlpool Single Door Refrigerator",
        "image": "fridge_03.png",
        "rating": 4.3,
        "reviews": 85,
        "condition": "Refurbished",
        "price": "₹7,999",
        "capacity": "190 L",
        "category": "Single Door"
    },

    {
        "name": "Haier Double Door Refrigerator",
        "image": "fridge_04.png",
        "rating": 4.7,
        "reviews": 142,
        "condition": "Used - Like New",
        "price": "₹13,499",
        "capacity": "320 L",
        "category": "Double Door"
    },

    {
        "name": "Godrej Single Door Refrigerator",
        "image": "fridge_05.png",
        "rating": 4.2,
        "reviews": 68,
        "condition": "Used",
        "price": "₹6,999",
        "capacity": "185 L",
        "category": "Single Door"
    },

    {
        "name": "LG Side-by-Side Refrigerator",
        "image": "fridge_06.png",
        "rating": 4.8,
        "reviews": 176,
        "condition": "Refurbished",
        "price": "₹29,999",
        "capacity": "584 L",
        "category": "Side-by-Side"
    },

    {
        "name": "Samsung French Door Refrigerator",
        "image": "fridge_07.png",
        "rating": 4.7,
        "reviews": 120,
        "condition": "Used - Excellent",
        "price": "₹34,999",
        "capacity": "550 L",
        "category": "French Door"
    }

]


# ==========================================
# SEARCH AND FILTER
# ==========================================

st.markdown("## Explore Our Collection")

search_col, filter_col = st.columns([2, 1])

with search_col:

    search = st.text_input(
        "Search refrigerators",
        placeholder="Search by brand or model..."
    )

with filter_col:

    selected_category = st.selectbox(
        "Filter by type",
        [
            "All Refrigerators",
            "Single Door",
            "Double Door",
            "Side-by-Side",
            "French Door"
        ]
    )


# ==========================================
# FILTER PRODUCTS
# ==========================================

filtered_products = []

for product in products:

    matches_search = (
        search.lower() in product["name"].lower()
    )

    matches_category = (
        selected_category == "All Refrigerators"
        or product["category"] == selected_category
    )

    if matches_search and matches_category:
        filtered_products.append(product)


st.write("")

st.markdown(
    f"**{len(filtered_products)} refrigerators available in catalogue**"
)

st.write("")


# ==========================================
# DISPLAY PRODUCT CARDS
# ==========================================

for index, product in enumerate(filtered_products):

    with st.container(border=True):

        image_col, details_col = st.columns(
            [1.15, 2.5],
            gap="large"
        )

        # PRODUCT IMAGE

        with image_col:

            image_path = (
                BASE_DIR
                / "assets"
                / "refrigerators"
                / product["image"]
            )

            if image_path.is_file():

                st.image(
                    str(image_path),
                    width="stretch"
                )

            else:

                st.warning(
                    f"Image unavailable: {product['image']}"
                )


        # PRODUCT DETAILS

        with details_col:

            st.markdown(
                '<div class="product-label">'
                'Frostly COLLECTION'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="product-name">'
                f'{product["name"]}'
                f'</div>',
                unsafe_allow_html=True
            )

            full_stars = int(product["rating"])

            stars = (
                "★" * full_stars
                + "☆" * (5 - full_stars)
            )

            st.markdown(
                f'<span class="product-rating">{stars}</span>'
                f'&nbsp; '
                f'<span class="rating-number">'
                f'{product["rating"]}/5'
                f'</span>',
                unsafe_allow_html=True
            )

            st.caption(
                f'{product["reviews"]} sample reviews'
            )

            st.markdown(
                f'<span class="product-condition">'
                f'{product["condition"]}'
                f'</span>',
                unsafe_allow_html=True
            )

            st.write("")

            st.markdown(
                f'<div class="product-capacity">'
                f'❄️ Capacity: {product["capacity"]}'
                f' &nbsp; | &nbsp; '
                f'Category: {product["category"]}'
                f'</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="product-price">'
                f'{product["price"]}'
                f'</div>',
                unsafe_allow_html=True
            )

            if st.button(
                "Enquire About This Refrigerator →",
                key=f"enquire_{products.index(product)}"
            ):

                st.info(
                    "WhatsApp enquiry integration will be "
                    "connected after adding your business number."
                )


# ==========================================
# EMPTY SEARCH RESULT
# ==========================================

if not filtered_products:

    st.info(
        "No refrigerators found. Try another search."
    )


# ==========================================
# FOOTER
# ==========================================

st.write("")
st.write("")

render_html("""
<div class="catalogue-footer">

    <h3>❄️ Frostly</h3>

    <p>
        Find Your Cool. Upgrade Your Comfort.
    </p>

    <p>
        Quality Refrigerators. Reliable Repairs.
    </p>

</div>
""")
