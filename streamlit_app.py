import streamlit as st

st.set_page_config(
    page_title="AgroShield AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.image("https://img.icons8.com/emoji/96/seedling.png", width=60)
st.sidebar.title("🌿 AgroShield AI")
st.sidebar.caption("Smart Gardening Dashboard")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Dashboard", "🌱 Crops", "🌦 Weather", "🛡 Security", "🤖 AI Assistant"]
)

st.sidebar.markdown("---")
st.sidebar.success("🟢 System Online")

# Route to pages
if page == "🏠 Dashboard":
    from pages import dashboard
    dashboard.show()

elif page == "🌱 Crops":
    from pages import crops
    crops.show()

elif page == "🌦 Weather":
    from pages import weather
    weather.show()

elif page == "🛡 Security":
    from pages import security
    security.show()

elif page == "🤖 AI Assistant":
    from pages import ai_chat
    ai_chat.show()
