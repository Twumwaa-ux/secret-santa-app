import os
import streamlit as st

st.set_page_config(
    page_title="Secret Santa",
    page_icon="🎁",
    layout="centered"
)

assignments = {
    "Afia": "Owusuah",
    "Aatifah": "Sabina",
    "Ainoo Brey": "Benedicta",
    "Akosua Offei": "Firdaus",
    "Akua": "Fynn",
    "Ama Osaa": "Kylee Ann",
    "Angela": "Maame Araba",
    "Awo Doe": "Ohenewaa",
    "Benedicta": "Pamela",
    "Deborah": "Sofia",
    "Diana": "Akosua Offei",
    "Esther Doe": "Mary",
    "Firdaus": "Aatifah",
    "Fynn": "Jessica",
    "Gifty": "Diana",
    "Grace": "Lucky",
    "Hadile": "Louisa",
    "Jessica": "Gifty",
    "Jessie": "Esther Doe",
    "Kylee Ann": "Maame Korkor",
    "Laurena": "Ummul",
    "Louisa": "Nelly",
    "Lucky": "Angela",
    "Maame Araba": "Grace",
    "Maame Korkor": "Hadile",
    "Mary": "Ama Osaa",
    "Michelle": "Ainoo Brey",
    "Mitchelle": "Nana Ama",
    "Nana Afia": "Mitchelle",
    "Nana Ama": "Stephanie",
    "Nana Yaa": "Jessie",
    "Nelly": "Oheneba",
    "Oheneba": "Nana Yaa",
    "Ohenewaa": "Laurena",
    "Ora": "Akua",
    "Owusuah": "Phylix",
    "Pamela": "Deborah",
    "Phylix": "Nana Afia",
    "Sabina": "Michelle",
    "Sofia": "Ora",
    "Stephanie": "Yvonne",
    "Ummul": "Awo Doe",
    "Yvonne": "Afia"
}

USED_FILE = "used_names.txt"


def get_used_names():
    if os.path.exists(USED_FILE):
        with open(USED_FILE, "r") as f:
            return set(line.strip() for line in f)
    return set()


def mark_name_as_used(name):
    with open(USED_FILE, "a") as f:
        f.write(name + "\n")


if "revealed_in_session" not in st.session_state:
    st.session_state["revealed_in_session"] = False


st.title("🎁 Secret Santa Reveal")

with st.expander("🔑 Admin Options (Reset List)"):
    admin_pass = st.text_input(
        "Enter Admin Password to Reset:",
        type="password"
    )

    if admin_pass == "santa2026":
        if st.button("Reset All Used Names"):
            if os.path.exists(USED_FILE):
                os.remove(USED_FILE)

            st.session_state["revealed_in_session"] = False

            st.success(
                "All names reset! Everyone can view their match again."
            )

            st.rerun()


st.write("Select your name below to reveal your match.")

used_names = get_used_names()

names_list = ["-- Select your name --"] + sorted(
    list(assignments.keys())
)

selected_name = st.selectbox(
    "Your Name:",
    names_list
)


if selected_name != "-- Select your name --":

    st.divider()

    if st.session_state["revealed_in_session"]:

        st.error(
            "🛑 You have already revealed a match during this session!"
        )

        st.info(
            "Please close this browser tab before letting someone else use this device."
        )

    elif selected_name in used_names:

        st.error(
            "⚠️ This name has already been viewed."
        )

        st.info(
            "If you forgot who you got, ask the organizer to check or reset."
        )

    else:

        if st.button("✨ Reveal My Match"):

            recipient = assignments[selected_name]

            mark_name_as_used(selected_name)

            st.session_state["revealed_in_session"] = True

            st.success(
                f"🎄 You are Secret Santa for: **{recipient}**"
            )

            st.warning(
                "🔒 Please close this page now so no one else sees your match!"
            )
