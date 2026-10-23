# app.py
import streamlit as st
st.title("Care For Life Foundation Drug Verifier")
st.image("logo.jpg", width=120)
nafdac_registry = {
    "04-0411": {
        "Name": "Emzor 500 mg tablet",
        "Status": "Verified", 
        "Producer": "Emzor",
        "Category": "Malaria Frontline",
        "Active Ingredient": "Paracetamol"
    },
    "B4-0262": {
        "Name": "Lonart DS Arthemether/Lumefantrine(80/480mg)",
        "Status": "Verified",
        "Category": "Malaria Frontline",
        "Producer": "Greenlife Pharmaceuticals",
        "Active Ingredient": "Arthemether/Lumefantrine"
    },
    "04-9927": {
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
    "B4-5980": {
        "Name": "Masedyl All-Day",
        "Status": "Verified",
        "Category": "Multi-Symptom Cold & Flu",
        "Producer": "May & Baker Nigeria PLC",
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
else:
    st.error("Warning, Drug not foud")
    st.warning("Make sure of correct input or Check NAFDAC greenbook")
    st.markdown("https://greenbook.nafdac.gov.ng/")
