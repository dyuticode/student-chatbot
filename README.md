# 🤖 ToLearnChatbot

An AI-powered Student Assistant built with Streamlit and Google Gemini AI. This chatbot helps students learn, ask questions, analyze PDFs and images, use voice input, save chat history, and interact with AI through a modern web interface.

---

## 🚀 Features

### 💬 AI Chat Assistant

* Powered by Google Gemini AI
* Answers academic and general questions
* Maintains conversation history

### 🔐 Secure Login System

* Username and password authentication
* Credentials stored securely using environment variables

### 🎤 Voice Input

* Speech-to-text using SpeechRecognition
* Speak your question instead of typing

### 🔊 Text-to-Speech

* AI responses can be read aloud
* Powered by pyttsx3

### 📄 PDF Analysis

* Upload PDF files
* Extract and analyze text content
* Ask questions about uploaded documents

### 🖼️ Image Analysis

* Upload images (JPG, JPEG, PNG)
* Gemini Vision analyzes image content
* Detects objects, text, diagrams, and charts

### 💾 Chat History

* Automatically saves conversations
* Load previous chats anytime
* Delete unwanted chat sessions

### 🎨 Modern UI

* Dark-themed interface
* Responsive design
* Streamlit-powered web application

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* Pillow (PIL)
* SpeechRecognition
* Pyttsx3
* PyPDF2
* Python-dotenv

---

## 📂 Project Structure

```text
ToLearnChatbot/
│
├── app.py
├── .env
├── requirements.txt
├── uploads/
├── saved_chats/
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/tolearnchatbot.git
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

### 4. Create .env File

```env
GEMINI_API_KEY=your_gemini_api_key
APP_USERNAME=admin
APP_PASSWORD=password123
```

### 5. Run Application

```bash
streamlit run app.py
```

---

## 🔑 Getting Gemini API Key

1. Visit Google AI Studio
2. Create a new API key
3. Copy the key
4. Add it to the `.env` file

---

## 📸 Supported Upload Formats

### Images

* JPG
* JPEG
* PNG

### Documents

* PDF

---

## 🎯 Future Improvements

* User registration system
* Multiple user accounts
* Database integration (MongoDB)
* Chat export to PDF
* AI-generated study notes
* Quiz generation
* Flashcard generation
* Student dashboard
* Cloud deployment

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to GitHub
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Dyuti Asok B

Aspiring Full Stack Developer | AI Enthusiast | Student Developer

If you like this project, don't forget to ⭐ the repository.

