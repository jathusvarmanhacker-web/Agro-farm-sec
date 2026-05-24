import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY", "")

def show():
    st.title("🌦 Weather Intelligence")
    st.caption("Forecast and irrigation advice")

    # City input — user can change location
    city = st.text_input("📍 Location", value=os.getenv("CITY", "Kandy"))

    if not API_KEY:
        st.warning("⚠️ No OpenWeather API key found. Add OPENWEATHER_API_KEY to your .env file.")
        st.stop()

    if not city:
        st.info("Enter a city name above.")
        st.stop()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&cnt=7"

    try:
        res      = requests.get(url, timeout=5).json()
        fore_res = requests.get(forecast_url, timeout=5).json()
    except Exception as e:
        st.error(f"Could not fetch weather: {e}")
        st.stop()

    if res.get("cod") != 200:
        st.error(f"City not found: {res.get('message', 'Unknown error')}")
        st.stop()

    # Current conditions
    temp     = round(res["main"]["temp"])
    feels    = round(res["main"]["feels_like"])
    humidity = res["main"]["humidity"]
    wind     = round(res["wind"]["speed"] * 3.6)  # m/s to km/h
    desc     = res["weather"][0]["description"].title()

    st.markdown("---")
    st.subheader(f"Current Conditions — {city}")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🌡 Temperature", f"{temp}°C", f"Feels {feels}°C")
    col2.metric("💧 Humidity",    f"{humidity}%")
    col3.metric("🌬 Wind Speed",  f"{wind} km/h")
    col4.metric("🌤 Condition",   desc)

    # Rain alert
    if "rain" in desc.lower():
        st.info("🌧 Rain detected — No watering needed today!")
    else:
        st.success("☀️ No rain expected — Check soil moisture before watering.")

    # Watering advice
    st.markdown("---")
    st.subheader("💡 Smart Advice")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info(f"**Watering:** {'Skip — rain coming' if 'rain' in desc.lower() else 'Check soil moisture'}")
    with col2:
        st.info(f"**Humidity:** {'High — watch for fungus' if humidity > 80 else 'Normal range'}")
    with col3:
        st.info(f"**Wind:** {'Strong — protect seedlings' if wind > 30 else 'Calm — good for spraying'}")

    # 5-day forecast
    if fore_res.get("cod") == "200":
        st.markdown("---")
        st.subheader("📅 5-Day Forecast")
        cols = st.columns(len(fore_res["list"]))
        for i, item in enumerate(fore_res["list"]):
            day  = item["dt_txt"].split(" ")[0]
            t    = round(item["main"]["temp"])
            d    = item["weather"][0]["description"].title()
            cols[i].metric(day, f"{t}°C", d)
