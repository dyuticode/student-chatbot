# 🤖 TolearnChatbot

An AI-powered Student Assistant built using Streamlit and Google Gemini AI.

TolearnChatbot helps students learn faster by providing intelligent answers, voice interaction, document analysis, image understanding, and chat history management in a clean and modern interface.

---

## ✨ Features

### 🔐 Secure Login System

* Username and password authentication
* Credentials stored securely in `.env`
* Session-based login management

### 💬 AI Chat Assistant

* Powered by Google Gemini AI
* Natural language conversations
* Fast and intelligent responses
* Context-aware chat history

### 🎤 Voice Input

* Speak directly to the chatbot
* Speech-to-text using SpeechRecognition
* Hands-free interaction

### 🔊 Voice Output

* AI responses are spoken aloud
* Text-to-speech using pyttsx3

### 📂 File Upload & Analysis

Supports:

* PDF Documents
* JPG Images
* JPEG Images
* PNG Images

The chatbot can:

* Read PDF content
* Summarize documents
* Answer questions from uploaded files
* Analyze images and describe their contents

### 🖼️ Image Understanding

Upload images and ask questions about them.

The AI can:

* Detect objects
* Read visible text
* Explain diagrams
* Analyze charts and visuals

### 💾 Chat History Management

* Save conversations automatically
* Create multiple chats
* Load previous chats
* Delete old chats

### 🎨 Modern UI

* Dark-themed interface
* Responsive Streamlit layout
* Clean chatbot experience

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### AI Model

* Google Gemini 2.0 Flash

### Backend Utilities

* Python

### Libraries Used

* google-genai
* python-dotenv
* SpeechRecognition
* pyttsx3
* PyPDF2
* python-docx
* pandas
* openpyxl
* pillow
* pyaudio

---

## 📁 Project Structure

```bash
TolearnChatbot/
│
├── app.py
├── auth.py
├── chat_manager.py
├── speech_utils.py
├── file_processor.py
│
├── uploads/
├── saved_chats/
│
├── .env
├── .gitignore
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/tolearnchatbot.git
cd tolearnchatbot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
USERNAME=your_username
PASSWORD=your_password
```

Do NOT upload your `.env` file to GitHub.

---

## 🚀 Running the Application

```bash
streamlit run app.py
```

Application will open in your browser.

---

## 📚 How To Use

1. Login using your credentials.
2. Enter your Gemini API Key.
3. Start chatting with the AI.
4. Upload PDFs or Images for analysis.
5. Use voice input by clicking the microphone button.
6. Listen to AI responses using built-in text-to-speech.
7. Save and revisit previous conversations.

---

## 🔒 Security

The project uses:

* Environment variables for credentials
* `.gitignore` protection for sensitive files
* Session-based authentication

Never expose:

* Gemini API Keys
* `.env` files
* Personal credentials

---

## 🎯 Future Improvements

* User Registration System
* Multiple User Accounts
* Database Integration (MongoDB)
* Chat Search Feature
* AI Study Notes Generator
* Quiz Generator
* Flashcard Creator
* OCR for Image Text Extraction
* Cloud Deployment
* Dark/Light Theme Toggle
* Export Chats as PDF

---

## 👨‍💻 Author

Developed by Dyuti Asok B

A personal AI-powered learning assistant designed to make studying smarter, faster, and more interactive.
