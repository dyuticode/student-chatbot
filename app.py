from dotenv import load_dotenv
from PIL import Image
import os
import re
import streamlit as st
from google import genai
import speech_recognition as sr
import json
import time
import pyttsx3
from datetime import datetime
from PyPDF2 import PdfReader

load_dotenv()

st.set_page_config(
    page_title="tolearnchatbot",
    page_icon="🤖",
    layout="wide"
)

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

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")

if not st.session_state.logged_in:

    st.title("🔐 Login to AI Assistant")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == USERNAME and password == PASSWORD:

            st.session_state.logged_in = True

            st.rerun()

        else:
            st.error("Invalid username or password")

    st.stop()

CHAT_FOLDER = "saved_chats"

if not os.path.exists(CHAT_FOLDER):
    os.makedirs(CHAT_FOLDER)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def save_chat(chat_name, messages):

    filepath = os.path.join(
        CHAT_FOLDER,
        f"{chat_name}.json"
    )

    with open(filepath, "w") as f:
        json.dump(messages, f)

def load_chat(chat_name):

    filepath = os.path.join(
        CHAT_FOLDER,
        f"{chat_name}.json"
    )

    if os.path.exists(filepath):

        with open(filepath, "r") as f:
            return json.load(f)

    return []

def get_chat_list():

    chats = []

    for file in os.listdir(CHAT_FOLDER):

        if file.endswith(".json"):

            chats.append(
                file.replace(".json", "")
            )

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

def speak_text(text):

    engine = pyttsx3.init()

    engine.say(text)

    engine.runAndWait()

st.title("🤖 Tolearnchatbot")

st.caption("Your personal AI study buddy")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_chat" not in st.session_state:
    st.session_state.current_chat = None

with st.sidebar:

    st.header("⚙ Settings")

    if st.button("🚪 Logout"):

        st.session_state.logged_in = False

        st.rerun()

    api_key = GEMINI_API_KEY

    st.divider()

    uploaded_file = st.file_uploader(
        "📂 Upload File",
        type=["pdf", "jpg", "jpeg", "png"]
    )

    if uploaded_file:

        file_type = uploaded_file.type

        if file_type.startswith("image"):

            image = Image.open(uploaded_file)

            st.image(
                image,
                caption="Uploaded Image",
                use_container_width=True
            )

    st.divider()

    if st.button("➕ New Chat"):

        chat_name = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        st.session_state.current_chat = chat_name

        st.session_state.messages = []

        save_chat(chat_name, [])

        st.rerun()

    st.divider()

    st.subheader("💬 Saved Chats")

    chat_list = get_chat_list()

    for chat in chat_list:

        col1, col2 = st.columns([4, 1])

        with col1:

            if st.button(
                chat,
                key=f"load_{chat}",
                use_container_width=True
            ):

                st.session_state.current_chat = chat

                st.session_state.messages = load_chat(chat)

                st.rerun()

        with col2:

            if st.button("❌", key=f"del_{chat}"):

                os.remove(
                    os.path.join(
                        CHAT_FOLDER,
                        f"{chat}.json"
                    )
                )

                if (
                    st.session_state.current_chat
                    == chat
                ):

                    st.session_state.current_chat = None

                    st.session_state.messages = []

                st.rerun()

if api_key:

    try:
       client = genai.Client(api_key=api_key)
    except Exception as e:
       st.error(f"Failed to initialize Gemini: {e}")
       st.stop()

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if st.button("🎤 Speak"):

        voice_text = recognize_speech()

        if voice_text:
            st.session_state.voice_prompt = voice_text

    prompt = st.chat_input("Ask anything...")

    if "voice_prompt" in st.session_state:

        prompt = st.session_state.voice_prompt

        del st.session_state.voice_prompt

    if prompt:

        if st.session_state.current_chat is None:

            short_name = re.sub(
            r'[^a-zA-Z0-9_]',
            '',
            prompt[:30].replace(" ", "_")
            )

            timestamp = datetime.now().strftime(
                "%H-%M-%S"
            )

            chat_name = (
                f"{short_name}_{timestamp}"
            )

            st.session_state.current_chat = chat_name

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        pdf_text = ""
        image_prompt = ""

        if uploaded_file:

            file_type = uploaded_file.type

            if file_type == "application/pdf":

                pdf_reader = PdfReader(uploaded_file)

                for page in pdf_reader.pages:

                    text = page.extract_text()

                    if text:
                        pdf_text += text

            elif file_type.startswith("image"):

                image_prompt = """
                User has uploaded an image.
                Analyze the image carefully.
                Describe objects, text, diagrams,
                charts or anything visible.
                """

        conversation_history = ""

        system_prompt = """
        You are a helpful AI student assistant.
        Give clear, friendly and well-formatted answers.
        Use markdown formatting whenever useful.
        """

        conversation_history += (
            system_prompt + "\n\n"
        )

        if pdf_text:

            conversation_history += (
                "Here is PDF content:\n"
                + pdf_text +
                "\n\n"
            )

        if image_prompt:

            conversation_history += (
                image_prompt +
                "\n\n"
            )

        for msg in st.session_state.messages:

            role = msg["role"]

            content = msg["content"]

            conversation_history += (
                f"{role}: {content}\n"
            )

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                try:

                    if uploaded_file and uploaded_file.type.startswith("image"):

                        image = Image.open(uploaded_file)

                        response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            contents=[
                                prompt,
                                image
                            ]
                        )

                    else:

                        response = client.models.generate_content(
                            model="gemini-2.0-flash",
                            contents=conversation_history
                        )
                        
                    reply = response.text

                    message_placeholder = st.empty()

                    full_response = ""

                    for word in reply.split():

                        full_response += (
                            word + " "
                        )

                        time.sleep(0.03)

                        message_placeholder.markdown(
                            full_response + "▌"
                        )

                    message_placeholder.markdown(
                        full_response
                    )

                    speak_text(reply)

                except Exception as e:

                    reply = f"⚠ Error: {str(e)}"

                    st.error(reply)

                    print("Gemini Error:", e)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

        save_chat(
            st.session_state.current_chat,
            st.session_state.messages
        )

else:

    st.info(
        "Enter your Gemini API key in the sidebar."
    )