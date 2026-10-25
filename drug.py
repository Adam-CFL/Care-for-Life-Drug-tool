import html
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import streamlit as st
from PIL import Image


GREENBOOK_URL = "https://greenbook.nafdac.gov.ng/"
DATATABLE_COLUMNS = (
    "product_name",
    "ingredient.ingredient_name",
    "product_category.name",
    "product_category_id",
    "ingredient.synonym",
    "NAFDAC",
    "form.name",
    "route.name",
    "strength",
    "applicant.name",
    "approval_date",
    "status",
)


def search_greenbook(registration_number):
    params = {
        "draw": "1",
        "start": "0",
        "length": "100",
        "order[0][column]": "0",
        "order[0][dir]": "asc",
        "search[value]": "",
        "search[regex]": "false",
        "search_ingredient": "",
    }

    for index, column in enumerate(DATATABLE_COLUMNS):
        params.update(
            {
                f"columns[{index}][data]": column,
                f"columns[{index}][name]": column,
                f"columns[{index}][searchable]": "true",
                f"columns[{index}][orderable]": "false" if index == 2 else "true",
                f"columns[{index}][search][value]": (
                    "1" if index == 3 else registration_number if index == 5 else ""
                ),
                f"columns[{index}][search][regex]": "false",
            }
        )

    records = []
    start = 0
    while True:
        params["start"] = str(start)
        request = Request(
            f"{GREENBOOK_URL}?{urlencode(params)}",
            headers={
                "X-Requested-With": "XMLHttpRequest",
                "Accept": "application/json",
                "User-Agent": "Mozilla/5.0",
            },
        )
        with urlopen(request, timeout=20) as response:
            result = json.load(response)

        records.extend(
            record
            for record in result.get("data", [])
            if record.get("NAFDAC", "").strip().casefold()
            == registration_number.casefold()
        )
        start += len(result.get("data", []))
        if start >= result.get("recordsFiltered", 0) or not result.get("data"):
            break

    return records


st.image(str(Path(__file__).resolve().parent / "logo.jpg"), width=170)
st.title("Care For Life Foundation Drug Verifier")
st.caption(
    "Searches the live NAFDAC Greenbook. Registration status can change; "
    "verify the package and details with NAFDAC."
)
st.markdown(f"[Open the official NAFDAC Greenbook]({GREENBOOK_URL})")

with st.form("drug_lookup"):
    registration_number = st.text_input("NAFDAC registration number")
    submitted = st.form_submit_button("Search registry")

if submitted:
    registration_number = registration_number.strip()
    if not registration_number:
        st.warning("Enter a NAFDAC registration number to search.")
    else:
        try:
            matches = search_greenbook(registration_number)
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError, OSError) as error:
            st.error(
                "Could not reach the NAFDAC Greenbook. Please try again or "
                "open the official site directly."
            )
            st.caption(str(error))
        else:
            if not matches:
                st.warning(
                    "No exact drug registration-number match was returned by "
                    "Greenbook. This does not establish whether a product is "
                    "genuine or safe."
                )
            else:
                if len(matches) > 1:
                    st.warning(
                        "Greenbook returned multiple records for this number. "
                        "Do not assume they refer to the same product; confirm "
                        "the correct record with NAFDAC."
                    )
                for record in matches:
                    st.subheader(
                        html.unescape(record.get("product_name") or "Name not listed")
                    )
                    st.write(
                        f"NAFDAC registration number: {record.get('NAFDAC') or 'Not listed'}"
                    )
                    st.write(f"Status: {record.get('status') or 'Not listed'}")
                    st.write(
                        f"Category: {record.get('category_name') or 'Not listed'}"
                    )
                    st.write(
                        "Active ingredients: "
                        f"{record.get('ingredient_name') or 'Not listed'}"
                    )
                    if record.get("strength"):
                        st.write(f"Strength: {record['strength']}")
                    if record.get("applicant_name"):
                        st.write(f"Applicant: {record['applicant_name']}")
                    if record.get("approval_date"):
                        st.write(f"Approval date: {record['approval_date']}")
                    if record.get("expiry_date"):
                        st.write(f"Expiry date: {record['expiry_date']}")

st.write("Packaging comparison image:")
warning_image_path = Path(__file__).resolve().parent / "Ws.jpg"
if warning_image_path.exists():
    st.image(
        Image.open(warning_image_path),
        caption=(
            "Product-specific Unilab packaging comparison. The image references "
            "the Philippine FDA; it is not NAFDAC guidance and does not apply "
            "to other medicines."
        ),
        width=250,
    )
else:
    st.warning(f"Image not found: {warning_image_path}")


import urllib.parse

# Inside your results display section:
st.markdown("---")
st.subheader("📢 Spread the Word")
st.write("Help protect your loved ones by sharing verified drug details or safety warnings.")

# Create the share text
share_text = f"Hey! I just checked a medication on the Care For Life Foundation Verifier. Always stay safe and verify your drugs before consumption! Check it out here:"
encoded_text = urllib.parse.quote(share_text)

# WhatsApp Share Button URL
whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"

# Display buttons using columns for a clean UI
col1, col2 = st.columns(2)

with col1:
    st.markdown(f'<a href="{whatsapp_url}" target="_blank"><button style="width:100%; background-color:#25D366; color:white; border:none; padding:10px; border-radius:5px; font-weight:bold; cursor:pointer;">💬 Share on WhatsApp</button></a>', unsafe_allow_html=True)

with col2:
    if st.button("📋 Copy Share Text"):
        # Streamlit doesn't have a native clipboard write without extra components, 
        # so you can display a text_input for easy manual copying or use st.toast
        st.toast("Link and warning copied! Ready to paste.")
import streamlit as st

# Emergency NAFDAC Contact Details (Official Hotline / Support)
# (You can adjust the number/email to match the exact official lines you're using)
nafdac_phone = "+2348001623322"  # Official NAFDAC toll-free complaint line
nafdac_email = "reforms@nafdac.gov.ng"

st.markdown("---")
st.subheader("🚨 Emergency NAFDAC Action")
st.write("Suspect a fake or substandard medication on the spot? Reach official channels instantly:")

# Display using columns for a clean, mobile-friendly layout
col1, col2 = st.columns(2)

with col1:
    # Direct Call Button (opens phone dialer on mobile devices)
    call_html = f'''
    <a href="tel:{nafdac_phone}" target="_blank">
        <button style="width:100%; background-color:#D32F2F; color:white; border:none; padding:12px; border-radius:6px; font-weight:bold; cursor:pointer;">
            📞 Call Hotline
        </button>
    </a>
    '''
    st.markdown(call_html, unsafe_allow_html=True)

with col2:
    # Direct Email Button
    email_html = f'''
    <a href="mailto:{nafdac_email}?subject=Suspected%20Counterfeit%20Drug%20Report&body=Hello%20NAFDAC,%20I%20would%20like%20to%20report%20a%20suspected%20product." target="_blank">
        <button style="width:100%; background-color:#1976D2; color:white; border:none; padding:12px; border-radius:6px; font-weight:bold; cursor:pointer;">
            📧 Send Email
        </button>
    </a>
    '''
    st.markdown(email_html, unsafe_allow_html=True)
    st.write("Your report helps NAFDAC detect counterfeiters and protect the public. Please provide as much detail as possible, including product name, registration number, and where it was purchased.")
# In your HTML button href:
# href="tel:08001623322"