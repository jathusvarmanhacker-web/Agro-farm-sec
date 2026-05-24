# 🌿 AgroShield AI

> **AI-powered smart gardening & protected storage dashboard**
> Integrates Arduino sensor monitoring, weather intelligence, crop tracking, security alerts, and multilingual AI farming assistance — built with Python & Streamlit.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Arduino](https://img.shields.io/badge/Arduino-Serial-00979D?style=flat&logo=arduino&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## Features

| Module | Description |
|--------|-------------|
| Dashboard | Live sensor cards — soil moisture, water tank, fire status, storage security |
| Crop Manager | Add crops with planting and harvest dates, auto harvest reminders |
| Weather Intelligence | OpenWeather API — real-time conditions, rain alerts, irrigation advice |
| Fire Alert System | Real-time flame sensor monitoring |
| Storage Security | Ultrasonic sensor intrusion detection |
| AI Assistant | Gemini-powered farming help in English, Tamil, Sinhala |

---

## Project Structure

```
AgroShieldAI/
|
+-- streamlit_app.py         Main entry point
+-- requirements.txt         Python dependencies
+-- crops.json               Crop data storage
+-- .env                     API keys (never commit this)
+-- .env.example             API key template
+-- .gitignore
|
+-- pages/
|   +-- __init__.py
|   +-- dashboard.py         Dashboard page
|   +-- crops.py             Crop management page
|   +-- weather.py           Weather page
|   +-- security.py          Security monitoring page
|   +-- ai_chat.py           AI assistant page
|
+-- assets/
    +-- logo.png
```

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AgroShieldAI.git
cd AgroShieldAI
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Activate on Linux / macOS
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Edit `.env` with your keys:

```env
OPENWEATHER_API_KEY=your_openweather_key_here
GEMINI_API_KEY=your_gemini_key_here
ARDUINO_PORT=COM3
ARDUINO_BAUD=9600
CITY=Kandy
COUNTRY_CODE=LK
```

### 5. Run the app

```bash
streamlit run streamlit_app.py
```

Open your browser at `http://localhost:8501`

---

## API Keys

| Key | Free | Get It At |
|-----|------|-----------|
| OpenWeather API | Yes | https://openweathermap.org/api |
| Google Gemini API | Yes | https://aistudio.google.com/app/apikey |

---

## Arduino Setup

### Expected Serial Output

```
SOIL:45
WATER:MED
FLAME:0
ULTRA:0
---
```

| Key | Values | Sensor |
|-----|--------|--------|
| SOIL | 0-100 (%) | Soil moisture sensor |
| WATER | LOW / MED / HIGH | Water level float switch |
| FLAME | 0 = safe, 1 = fire | IR flame sensor |
| ULTRA | 0 = clear, 1 = intruder | HC-SR04 ultrasonic |

### Find Your Arduino Port

Windows — open Device Manager, look under Ports (COM & LPT)

Linux:
```bash
ls /dev/tty*
# Usually /dev/ttyUSB0 or /dev/ttyACM0
```

macOS:
```bash
ls /dev/tty.*
# Usually /dev/tty.usbmodem... or /dev/tty.usbserial...
```

---

## Deployment on Streamlit Cloud

1. Push your repo to GitHub (make sure `.env` is in `.gitignore`)
2. Go to https://share.streamlit.io
3. Click **New app** and connect your GitHub repo
4. Set **Main file path** to `streamlit_app.py`
5. Click **Advanced settings** then **Secrets** and paste:

```toml
OPENWEATHER_API_KEY = "your_key_here"
GEMINI_API_KEY      = "your_key_here"
CITY                = "Kandy"
COUNTRY_CODE        = "LK"
```

6. Click **Deploy**

> Note: Arduino serial connection only works when running locally.
> On Streamlit Cloud, sensor data shows simulated values.

---

## Common Errors

| Error | Fix |
|-------|-----|
| `SyntaxError: invalid character` | Wrong file in repo — make sure .py files contain only Python code |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `SerialException` | Wrong COM port — check Device Manager |
| `City not found` | Check city spelling in the weather input |
| `Gemini API error` | Check your GEMINI_API_KEY in .env |

---

## Important Notes

- Never paste JavaScript or JSX code into a `.py` file
- `streamlit_app.py` is the only entry point — always run this file
- `AgroShieldAI.jsx` is the separate React version — keep it out of the Streamlit folder
- Never commit your `.env` file to GitHub

---

## License

MIT License — see LICENSE for details.
