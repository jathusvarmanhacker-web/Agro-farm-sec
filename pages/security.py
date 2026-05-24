import streamlit as st
import random
from datetime import datetime

def show():
    st.title("🛡 Security System")
    st.caption("Flame and intrusion monitoring")

    # Simulated sensor values
    flame    = False
    intruder = False

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔥 Fire Detection")
        if flame:
            st.error("🚨 FIRE DETECTED!\nCheck your garden immediately.")
        else:
            st.success("✅ No Fire — All Safe")
        st.caption("Flame sensor (digital pin 7)")

    with col2:
        st.subheader("👁 Storage Security")
        if intruder:
            st.warning("⚠️ INTRUDER DETECTED!\nUnauthorized movement in storage area.")
        else:
            st.success("✅ Storage Secure")
        st.caption("HC-SR04 ultrasonic sensor")

    st.markdown("---")
    st.subheader("📋 Security Log")

    log = [
        {"time": "12:30", "event": "System armed",                "level": "info"},
        {"time": "11:45", "event": "Storage accessed — authorized","level": "info"},
        {"time": "09:12", "event": "All clear",                    "level": "success"},
    ]

    for entry in log:
        t = entry["time"]
        e = entry["event"]
        if entry["level"] == "success":
            st.success(f"**{t}** — {e}")
        elif entry["level"] == "warning":
            st.warning(f"**{t}** — {e}")
        elif entry["level"] == "error":
            st.error(f"**{t}** — {e}")
        else:
            st.info(f"**{t}** — {e}")

    if st.button("🔄 Refresh"):
        st.rerun()
