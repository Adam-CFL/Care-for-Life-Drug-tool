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
with st.expander("🚨 Suspect this product is fake? Take Action"):
    st.write("If the packaging or physical check doesn't match, do not consume it. Report it immediately to the regulators:")
    st.markdown("- **Call NAFDAC Hotline:** [0800-1-623322](tel:08001623322)")
    st.markdown("- **Email Evidence:** [reforms@nafdac.gov.ng](mailto:reforms@nafdac.gov.ng)")
    st.write("Your report helps NAFDAC track down counterfeiters and protect the public.")