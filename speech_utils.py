import speech_recognition as sr
import pyttsx3

def recognize_speech():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        audio = recognizer.listen(source)

    try:

        return recognizer.recognize_google(audio)

    except:

        return ""

def speak_text(text):

    engine = pyttsx3.init()

    engine.say(text)

    engine.runAndWait()