# app.py
import streamlit as st
st.image("logo.jpg", width=170)

st.title("Care For Life Foundation Drug Verifier")
nafdac_registry = {
    "04-0411": {
        "Name": "Emzor 500 mg tablet",
        "Status": "Verified",
        "Producer": "Emzor",
        "Category": "Malaria Frontline",
        "Active Ingredient": "Paracetamol"
    },
    "04-9927": {
        "Name": "Lonart DS Arthemether/Lumefantrine(80/480mg)",
        "Status": "Verified",
        "Category": "Malaria Frontline",
        "Producer": "Greenlife Pharmaceuticals",
        "Active Ingredient": "Arthemether/Lumefantrine"
    },
    "04-3275": {
        "Name": "Coartem",
        "Status": "Verified",
        "Category": "Malaria Frontline",
        "Producer": "Novartis Nigeria Limited",
        "Active Ingredient": "Arthemeter/Lumefantrine"
    },
    "04-1928": {
        "Name": "Augmetin(625mg)",
        "Status": "Verified",
        "Category": "Infant/Pediatric Antibiotic",
        "Producer": "GlaxoSmithKline(GSK)",
        "Active Ingredient": "Amoxicilin/Clavulanate Potassium"
    },
    "04-0268": {
        "Name": "Emzor Folic Acid",
        "Status": "Verified",
        "Category": "Maternal/Pregnancy Care",
        "Producer": "Emzor Pharmaceutical Industries",
        "Active Ingredient": "Folic Acid(Vitamin B9,5mg)"
    },
    "A4-5443": {
        "Name": "Aldomet",
        "Status": "Verified",
        "Category": "Maternal Blood Pressure",
        "Producer": "Aspen Pharmacare Nigeria Limited",
        "Active Ingredient": "Methyldopa(250mg)"
    },
    "04-9127": {
        "Name": "Amoxil",
        "Status": "Verified",
        "Category": "Antibiotic/Bacterial Infection",
        "Producer": "GlaxoSmithKline Nigeria",
        "Active Ingredient": "Amoxicilin(500mg)"
    },
    "04-3022": {
        "Name": "Ciprotab",
        "Status": "Verified",
        "Category": "Antibiotic/Broad Spectrum",
        "Producer": "Fidson Healthcare PLC",
        "Active Ingredient": "Ciproflaxin(500mg)"
    },
    "04-0325": {
        "Name": "Flagyl",
        "Status": "Verified",
        "Category": "Antibiotics/Infections",
        "Producer": "May & Baker Nigeria PLC",
        "Active Ingredient": "Metronidazole(400mg)"
    },
    "A4-2810": {
        "Name": "Cataflam",
        "Status": "Verified",
        "Category": "Pain/Inflammation",
        "Producer": "Novartis Nigeria Limited",
        "Active Ingredient": "Diclofenac Potassium"
    },
    "04-4341": {
        "Name": "Amloc",
        "Status": "Verified",
        "Category": "Chronic Care/Hypertension",
        "Producer": "Fidson Healthcare Plc",
        "Active Ingredient": "Amlodipine(5mg/10mg)"
    },
    "B4-3112": {
        "Name": "Glucophage",
        "Status": "Verified",
        "Category": "Chronic Care/Hypertension",
        "Producer": "Merck Sante/Sereno",
        "Active Ingredient": "Metformin Hydrochloride(500mg)"
    },
    "A4-4120": {
        "Name": "Omez",
        "Status": "Verified",
        "Category": "Ulcer/Acidity relief",
        "Producer": "Dr. Reddy's Laboratories/ local partners",
        "Active Ingredient": "Omeprazole(20mg)"
    },
    "A4-3501": {
        "Name": "Clarityne",
        "Status": "Verified",
        "Category": "Anithistamine/Allergy",
        "Producer": "Bayer/Schering-Plough",
        "Active Ingredient": "Loratidine(10mg)"
    },
    "04-3638(general penicilin series)": {
        "Name": "Nelb Penicilin Injection 1  Mega",
        "Status": "Verified",
        "Category": "Severe Infection/Neonatal Care",
        "Producer": "Nelb/Local Distributors",
        "Active Ingredient": "Benzylpenicilin Sodium(1 Mega IU)"
    },
    "A4-9168": {
        "Name": "Bentarpen Injection",
        "Status": "Verified",
        "Category": "Long-Acting Antibiotic/Specialized",
        "Producer": "Sterling Drugs Ltd/Inject Care",
        "Active Ingredient": "Benzathine Benzylpenicilin(2,400,000IU)"
    },
    "04-0633": {
        "Name": "M&B Paracetamol Tablet",
        "Status": "Verified",
        "Category": "Analgesic/Fever",
        "Producer": "May & Baker Nigeria PLC",
        "Active Ingredient": "Paracetamol(500mg)"
    },
    "04-0975": {
        "Name": "Paradana Tablets",
        "Status": "Verified",
        "Category": "Analgesic/Pain Relief",
        "Producer": "Dana Pharmaceuticals",
        "Active Ingredient": "Paracetamol(500mg)"
    },
    "A11-1213": {
        "Name": "Masedyl Expectorant",
        "Status": "Verified",
        "Category": "Cold,Flu & Cough Syrup",
        "Producer": "May & Baker Nigeria PLC",
        "Active Ingredient": "Diphenhydramine/Ammonium Chloride/ Sodium Citrate/Menthol"
    },
    "A4-1680": {
        "Name": "Coartem",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Novartis Nigeria Ltd",
        "Active Ingredient": "Arthemeter/Lumefantrine"
    },
    "B4-0262": {
        "Name": "Coartem",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Novartis Nigeria Ltd",
        "Active Ingredient": "Arthemeter/Lumefantrine"
    },
    "04-0005": {
        "Name": "Panadol Extra Caplet",
        "Status": "Verified",
        "Category": "Analgesic",
        "Producer": "GlaxoSmithKline Consumer Nigeria PLC",
        "Active Ingredient": "Paracetamol(500mg) + Caffeine(65mg)"
    },
    "04-0373": {
        "Name": "Buscopan Tablets(10mg)",
        "Status": "Verified",
        "Category": "Antispasmodic",
        "Producer": "Boehringer Ingelheim",
        "Active Ingredient": "Hyoscine Butylbromide(10mg)"
    },
    "04-9495": {
        "Name": "P-Alaxin (Dihydroartemisinin 40 mg & Piperaquine 320 mg) Tablets",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Greenlife Pharmaceutical Limited",
        "Active Ingredient": "Dihydroartemisinin; Piperaquine Phosphate"
    },
"A4-100926": {
        "Name": "P-Alaxin 20/160 Dispersible Tablet",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Greenlife Pharmaceutical Limited",
        "Active Ingredient": "Dihydroartemisinin; Piperaquine Phosphate"
    },
"A4-100927": {
        "Name": "P-Alaxin 20/160 Dispersible Tablet",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Greenlife Pharmaceutical Limited",
        "Active Ingredient": "Dihydroartemisinin; Piperaquine Phosphate"
    },
    "A4-100810": {
        "Name": "P-Alaxin 40/320 Dispersible Tablet",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Greenlife Pharmaceutical Limited",
        "Active Ingredient": "Dihydroartemisinin; Piperaquine Phosphate"
    },
    "B4-8892": {
        "Name": "P-Alaxin TS",
        "Status": "Inactive",
        "Category": "Antimalarial",
        "Producer": "Greenlife Pharmaceutical Limited",
        "Active Ingredient": "Dihydroartemisinin; Piperaquine Phosphate"
    },
    "04-8970": {
        "Name": "Lonart 20/120 Powder For Oral Suspension",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Greenlife",
        "Active Ingredient": "Artemether; Lumefantrine"
    },
    "A4-4238": {
        "Name": "Lonart Dispersible Tablets",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Greenlife",
        "Active Ingredient": "Artemether; Lumefantrine"
    },
    "04-8969": {
        "Name": "Lonart Tablets",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Greenlife",
        "Active Ingredient": "Artemether; Lumefantrine"
    },
    "A4-1680": {
        "Name": "Coartem 20/120 Dispersible Tablets",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Novartis Nigeria Ltd",
        "Active Ingredient": "Artemether; Lumefantrine"
    },
    "B4-0262": {
        "Name": "Coartem 80/480 Tablets",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Novartis Nigeria Ltd",
        "Active Ingredient": "Artemether; Lumefantrine"
    },
    "B4-0953": {
        "Name": "Amatem 20/120 Softgel",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Elbe Pharma Nigeria Limited",
        "Active Ingredient": "Artemether; Lumefantrine"
    },
    "B4-0952": {
        "Name": "Amatem Forte Soft Gel Capsules",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Elbe Pharma Nigeria Limited",
        "Active Ingredient": "Artemether; Lumefantrine"
    },
    "A4-3489": {
        "Name": "Amatem Forte Tablets",
        "Status": "Verified",
        "Category": "Antimalarial",
        "Producer": "Elbe Pharma Nigeria Limited",
        "Active Ingredient": "Artemether; Lumefantrine"
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "Emzor Pharmaceutical Industries Limited",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "Emzor Pharmaceutical Industries Limited",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "Emzor Pharmaceutical Industries Limited",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "Emzor Pharmaceutical Industries Limited",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "Emzor Pharmaceutical Industries Limited",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "Emzor Pharmaceutical Industries Limited",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "Emzor Pharmaceutical Industries Limited",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "Emzor Pharmaceutical Industries Limited",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
    "": {
        "Name": "",
        "Status": "",
        "Category": "",
        "Producer": "",
        "Active Ingredient": ""
    },
}
st.write(f"Please make sure of correct input and punctuations, the program is case sensitive")
Drug = st.text_input("What is the NAFDAC registration number of the product? ")
if Drug in nafdac_registry:
    info = nafdac_registry[Drug]
    st.success("\nProduct found!")
    st.write(f"Name : {info['Name']}")
    st.write(f"Status: {info['Status']}")
    st.write(f"Producer : {info['Producer']}")
    st.write(f"Category : {info['Category']}")
    st.write(f"Active Ingredient: {info['Active Ingredient']}")
elif Drug =="":
    st.write("Waiting for input")
else:
    st.error("Warning, Drug not foud")
    st.warning("Make sure of correct input or Check NAFDAC greenbook")
    st.markdown("https://greenbook.nafdac.gov.ng/")



st.write("Warning Signs of Fake Drugs found below;")

from pathlib import Path
from PIL import Image
import streamlit as st

image_path = Path(__file__).resolve().parent / "Ws.jpg"

if image_path.exists():
    image = Image.open(image_path)
    st.image(image, caption="WS image", width=600)
else:
    st.warning(f"Image not found: {image_path}")