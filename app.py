import streamlit as st
from google import genai
import speech_recognition as sr
import json
import os
from datetime import datetime

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="AI Student Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM DARK UI ----------------
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3, p {
    color: white;
}

.stChatMessage {
    border-radius: 15px;
    padding: 10px;
    margin-bottom: 10px;
}

[data-testid="stSidebar"] {
    background-color: #161A23;
}

.stTextInput input {
    background-color: #262730;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- FOLDER SETUP ----------------
CHAT_FOLDER = "saved_chats"

if not os.path.exists(CHAT_FOLDER):
    os.makedirs(CHAT_FOLDER)

# ---------------- FUNCTIONS ----------------

def save_chat(chat_name, messages):

    filepath = os.path.join(CHAT_FOLDER, f"{chat_name}.json")

    with open(filepath, "w") as f:
        json.dump(messages, f)


def load_chat(chat_name):

    filepath = os.path.join(CHAT_FOLDER, f"{chat_name}.json")

    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)

    return []


def get_chat_list():

    chats = []

    for file in os.listdir(CHAT_FOLDER):

        if file.endswith(".json"):
            chats.append(file.replace(".json", ""))

    chats.sort(reverse=True)

    return chats


def recognize_speech():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        st.info("🎤 Listening... Speak now")

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text

    except:
        return ""

# ---------------- TITLE ----------------
st.title("🤖 AI Student Assistant")

st.caption("Your personal AI study buddy")

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.header("⚙ Settings")

    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password"
    )

    st.divider()

    # NEW CHAT
    if st.button("➕ New Chat"):

        chat_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        st.session_state.current_chat = chat_name
        st.session_state.messages = []

        save_chat(chat_name, [])

        st.rerun()

    st.divider()

    st.subheader("💬 Saved Chats")

    chat_list = get_chat_list()

    for chat in chat_list:

        col1, col2 = st.columns([4,1])

        with col1:
            if st.button(chat, use_container_width=True):

                st.session_state.current_chat = chat
                st.session_state.messages = load_chat(chat)

                st.rerun()

        with col2:

            if st.button("❌", key=chat):

                os.remove(os.path.join(CHAT_FOLDER, f"{chat}.json"))

                if st.session_state.current_chat == chat:
                    st.session_state.current_chat = None
                    st.session_state.messages = []

                st.rerun()

# ---------------- CHECK API KEY ----------------
if api_key:

    # Gemini client
    client = genai.Client(api_key=api_key)

    # ---------------- SHOW OLD MESSAGES ----------------
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # ---------------- VOICE BUTTON ----------------
    if st.button("🎤 Speak"):

        voice_text = recognize_speech()

        if voice_text:
            st.session_state.voice_prompt = voice_text

    # ---------------- CHAT INPUT ----------------
    prompt = st.chat_input("Ask anything...")

    # Voice prompt
    if "voice_prompt" in st.session_state:

        prompt = st.session_state.voice_prompt
        del st.session_state.voice_prompt

    # ---------------- USER MESSAGE ----------------
    if prompt:

        # Auto-create chat if none exists
        if st.session_state.current_chat is None:

            short_name = prompt[:30].replace(" ", "_")

            timestamp = datetime.now().strftime("%H-%M-%S")

            chat_name = f"{short_name}_{timestamp}"

            st.session_state.current_chat = chat_name

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        # Show user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # ---------------- BUILD CONVERSATION ----------------
        conversation_history = ""

        system_prompt = """
        You are a helpful AI student assistant.
        Give clear, friendly and well-formatted answers.
        Use markdown formatting whenever useful.
        """

        conversation_history += system_prompt + "\n\n"

        for msg in st.session_state.messages:

            role = msg["role"]
            content = msg["content"]

            conversation_history += f"{role}: {content}\n"

        # ---------------- AI RESPONSE ----------------
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=conversation_history
                )

                reply = response.text

                st.markdown(reply)

        # Save AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        # SAVE CHAT
        save_chat(
            st.session_state.current_chat,
            st.session_state.messages
        )

# ---------------- NO API KEY ----------------
else:
    st.info("Enter your Gemini API key in the sidebar.")