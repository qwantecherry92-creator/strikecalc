import streamlit as st
from math import log, ceil

st.title("🎯 StrikeCalc — Weaponeering & CDE Calculator")

st.markdown("""
Enter the target details and munition parameters below.
""")

# Inputs
target = st.text_input("Target Name", "Target X")
desired_conf = st.slider("Desired Confidence (%)", 50, 100, 85) / 100
pk = st.number_input("Munition Pk per round (e.g., 0.15)", min_value=0.01, max_value=1.0, value=0.15)
hazard_dist = st.number_input("Hazard Distance (m)", min_value=1, value=75)
civilian_dist = st.number_input("Nearest Civilian Structure Distance (m)", min_value=0, value=50)

if st.button("Calculate"):
    failure_per_round = 1 - pk
    rounds_needed = ceil(log(1 - desired_conf) / log(failure_per_round))

    # CDE calculation
    if civilian_dist >= hazard_dist:
        cde = 1
    elif civilian_dist >= hazard_dist / 2:
        cde = 2
    else:
        cde = 3

    st.subheader(f"Results for {target}")
    st.write(f"📊 Rounds Required: **{rounds_needed}**")
    st.write(f"💥 CDE Level: **{cde}**")

    if cde <= 2:
        st.success("CDE Level within BCT approval authority.")
    else:
        st.warning("CDE Level may require higher HQ approval.")
