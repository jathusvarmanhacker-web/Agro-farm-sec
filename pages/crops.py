import streamlit as st
import json
import os
from datetime import date, datetime

CROPS_FILE = "crops.json"

def load_crops():
    if os.path.exists(CROPS_FILE):
        with open(CROPS_FILE, "r") as f:
            return json.load(f)
    return []

def save_crops(crops):
    with open(CROPS_FILE, "w") as f:
        json.dump(crops, f, indent=2)

def days_until(harvest_date_str):
    harvest = datetime.strptime(harvest_date_str, "%Y-%m-%d").date()
    return (harvest - date.today()).days

def show():
    st.title("🌱 Crop Manager")
    st.caption("Track and schedule your harvests")

    crops = load_crops()

    # Harvest reminders
    reminders = [c for c in crops if days_until(c["harvestDate"]) <= 7]
    if reminders:
        st.subheader("⏰ Harvest Reminders")
        for c in reminders:
            d = days_until(c["harvestDate"])
            if d < 0:
                st.error(f"🌿 **{c['name']}** — Overdue by {abs(d)} days!")
            elif d == 0:
                st.success(f"🌿 **{c['name']}** — Ready to harvest TODAY!")
            else:
                st.warning(f"🌿 **{c['name']}** — Ready in {d} day(s)")

    st.markdown("---")

    # Add crop form
    with st.expander("➕ Add New Crop"):
        col1, col2 = st.columns(2)
        with col1:
            name     = st.text_input("Crop Name", placeholder="Tomato")
            variety  = st.text_input("Variety",   placeholder="Cherry")
        with col2:
            plant_date   = st.date_input("Plant Date",   value=date.today())
            harvest_date = st.date_input("Harvest Date", value=date.today())

        if st.button("✅ Add Crop"):
            if name:
                crops.append({
                    "id":          len(crops) + 1,
                    "name":        name,
                    "variety":     variety,
                    "plantDate":   str(plant_date),
                    "harvestDate": str(harvest_date),
                })
                save_crops(crops)
                st.success(f"Added {name}!")
                st.rerun()
            else:
                st.error("Please enter a crop name.")

    st.markdown("---")
    st.subheader(f"Your Crops ({len(crops)})")

    if not crops:
        st.info("No crops added yet. Use the form above to add your first crop.")
    else:
        for i, crop in enumerate(crops):
            d = days_until(crop["harvestDate"])
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.markdown(f"**🌱 {crop['name']}** — *{crop.get('variety', '')}*")
                st.caption(f"Planted: {crop['plantDate']}  |  Harvest: {crop['harvestDate']}")
            with col2:
                if d < 0:
                    st.error(f"{abs(d)}d overdue")
                elif d == 0:
                    st.success("Harvest today!")
                elif d <= 7:
                    st.warning(f"{d} days left")
                else:
                    st.success(f"{d} days left")
            with col3:
                if st.button("🗑", key=f"del_{i}"):
                    crops.pop(i)
                    save_crops(crops)
                    st.rerun()
            st.markdown("---")
