import streamlit as st
import random
import time

def show():
    st.title("🏠 Dashboard")
    st.caption("Live sensor monitoring")

    # Simulated sensor data
    moisture  = random.randint(30, 80)
    water     = random.choice(["LOW", "MED", "HIGH"])
    flame     = False
    intruder  = False

    # Alert banners
    if flame:
        st.error("🔥 FIRE DETECTED — Check your garden immediately!")
    if intruder:
        st.warning("⚠️ INTRUDER DETECTED in storage area!")

    st.info("🌧 Rain expected tomorrow — Skip watering today")

    st.markdown("---")
    st.subheader("Live Sensor Readings")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("💧 Soil Moisture", f"{moisture}%",
                  delta="OK" if moisture > 30 else "LOW")

    with col2:
        st.metric("🪣 Water Tank", water)

    with col3:
        st.metric("🔥 Fire Sensor", "SAFE" if not flame else "FIRE!")

    with col4:
        st.metric("🛡 Storage", "SECURE" if not intruder else "BREACH!")

    st.markdown("---")
    st.subheader("Soil Moisture History")

    # Simulated chart data
    import pandas as pd
    import numpy as np
    data = pd.DataFrame({
        "Time": pd.date_range(end=pd.Timestamp.now(), periods=20, freq="3s"),
        "Moisture (%)": np.random.randint(38, 75, 20)
    })
    st.line_chart(data.set_index("Time"))

    if st.button("🔄 Refresh Sensors"):
        st.rerun()
