import streamlit as st

st.set_page_config(page_title="Secret Santa 🎁", page_icon="🎁", layout="centered")

st.title("🎁 Secret Santa Generator")
st.write("Select your name below to reveal who you are giving a gift to!")

assignments = {
    "Aatifah": "Ummul",
    "Ainoo Brey": "Awo Doe",
    "Akosua Offei": "Louisa",
    "Akua": "Angela",
    "Ama Osaa": "Gifty",
    "Angela": "Lucky",
    "Awo Doe": "Ora",
    "Benedicta": "Sofia",
    "Deborah": "Kylee Ann",
    "Diana": "Mitchelle",
    "Esther Doe": "Diana",
    "Firdaus": "Laurena",
    "Fynn": "Mary",
    "Gifty": "Maame Korkor",
    "Grace": "Ama Osaa",
    "Hadile": "Akua",
    "Jessica": "Nana Ama",
    "Jessie": "Owusuah",
    "Kylee Ann": "Ohenewaa",
    "Laurena": "Maame Araba",
    "Louisa": "Jessie",
    "Lucky": "Deborah",
    "Maame Araba": "Afia",
    "Maame Korkor": "Nana Yaa",
    "Mary": "Akosua Offei",
    "Michelle": "Ainoo Brey",
    "Mitchelle": "Fynn",
    "Nana Afia": "Nelly",
    "Nana Ama": "Pamela",
    "Nana Yaa": "Yvonne",
    "Nelly": "Michelle",
    "Oheneba": "Sabina",
    "Ohenewaa": "Stephanie",
    "Ora": "Hadile",
    "Owusuah": "Phylix",
    "Pamela": "Oheneba",
    "Phylix": "Firdaus",
    "Sabina": "Grace",
    "Sofia": "Esther Doe",
    "Stephanie": "Benedicta",
    "Ummul": "Nana Afia",
    "Yvonne": "Aatifah",
    "Afia": "Jessica"
}

names_list = ["-- Select your name --"] + sorted(list(assignments.keys()))
selected_name = st.selectbox("Your Name:", names_list)

if selected_name != "-- Select your name --":
    recipient = assignments[selected_name]
    st.divider()
    st.success(f"🎄 You are Secret Santa for: **{recipient}**")
    st.caption(" Please keep this secret and do not share your screen!")
