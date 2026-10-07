import os
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Secret Santa 🎁", page_icon="🎁", layout="centered")

# Secret Santa Assignments
assignments = {
    "Kylee-Ann": "Ohenewaa",
    "Mitchelle": "Fynn",
    "Ainoo-Brey": "Awo Doe",
    "Ama Osaa": "Gifty",
    "Firdaus": "Laurena",
    "Owusuah": "Phylix",
    "Maame Korkor": "Nana Yaa",
    "Nana Afia": "Nelly",
    "Akosua Offei": "Louisa",
    "Phylix": "Firdaus",
    "Laurena": "Maame Araba",
    "Lucky": "Deborah",
    "Maame Araba": "Afia",
    "Jessie": "Owusuah",
    "Awo Doe": "Ora",
    "Yvonne": "Aatifah",
    "Ora": "Hadile",
    "Angela": "Lucky",
    "Akua": "Angela",
    "Sabina": "Grace",
    "Pamela": "Oheneba",
    "Nana Yaa": "Yvonne",
    "Hadile": "Akua",
    "Mary": "Akosua Offei",
    "Michelle": "Ainoo Brey",
    "Ummul": "Nana Afia",
    "Diana": "Mitchelle",
    "Aatifah": "Ummul",
    "Nana Ama": "Pamela",
    "Nelly": "Michelle",
    "Grace": "Ama Osaa",
    "Louisa": "Jessie",
    "Afia": "Jessica",
    "Gifty": "Maame Korkor",
    "Jessica": "Nana Ama",
    "Fynn": "Mary",
    "Oheneba": "Sabina",
    "Esther Doe": "Diana",
    "Deborah": "Kylee Ann",
    "Ohenewaa": "Stephanie",
    "Sofia": "Esther Doe",
    "Benedicta": "Sofia",
    "Stephanie": "Benedicta"
}

USED_FILE = "used_names.txt"

# Helper function to get used names
def get_used_names():
    if os.path.exists(USED_FILE):
        with open(USED_FILE, "r") as f:
            return set(line.strip() for line in f)
    return set()

# Helper function to mark a name as used
def mark_name_as_used(name):
    with open(USED_FILE, "a") as f:
        f.write(name + "\n")

# App Header
st.title("🎁 Secret Santa Reveal")
st.write("Select your name from the list below to reveal who you are giving a gift to!")

used_names = get_used_names()

# Name Dropdown
names_list = ["-- Select your name --"] + sorted(list(assignments.keys()))
selected_name = st.selectbox("Your Name:", names_list)

if selected_name != "-- Select your name --":
    st.divider()
    
    if selected_name in used_names:
        st.error("⚠️ This name has already viewed their Secret Santa assignment.")
        st.info("If you forgot your recipient, please contact the organizer!")
    else:
        # Show result button to prevent accidental reveals
        if st.button("✨ Click to Reveal My Secret Santa"):
            recipient = assignments[selected_name]
            mark_name_as_used(selected_name)
            
            st.success(f"🎄 You are Secret Santa for: **{recipient}**")
            st.warning("🔒 Please close this page after viewing so no one else sees your match!")
    
