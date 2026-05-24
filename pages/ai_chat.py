import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY", "")

def show():
    st.title("🤖 AI Assistant")
    st.caption("Smart farming help — English | தமிழ் | සිංහල")

    if not API_KEY:
        st.warning("⚠️ No Gemini API key found. Add GEMINI_API_KEY to your .env file.")
        st.stop()

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-pro")

    # Language selector
    lang = st.radio("Language", ["English", "தமிழ்", "සිංහල"], horizontal=True)

    st.markdown("---")

    # Chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Input
    placeholders = {
        "English": "Ask about plant care, diseases, harvest timing...",
        "தமிழ்":   "உங்கள் கேள்வி தட்டச்சு செய்யவும்...",
        "සිංහල":  "ඔබගේ ප්‍රශ්නය ටයිප් කරන්න...",
    }

    user_input = st.chat_input(placeholders.get(lang, "Ask a question..."))

    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        with st.chat_message("user"):
            st.markdown(user_input)

        lang_instruction = f"Please respond in {lang}." if lang != "English" else ""

        system_prompt = f"""You are AgroShield AI, an expert smart gardening and agricultural assistant.
Help with plant care, disease diagnosis, pest control, harvest timing, soil management, and storage protection.
Be concise and practical. {lang_instruction}"""

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = model.generate_content(system_prompt + "\n\nUser: " + user_input)
                    reply = response.text
                except Exception as e:
                    reply = f"Error: {e}"
                st.markdown(reply)

        st.session_state.chat_history.append({"role": "assistant", "content": reply})

    # Clear chat
    if st.button("🗑 Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()
