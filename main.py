import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing Jarvis")


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# will speak the string which is consumed 
def speak(text):
    engine.say(text)
    engine.runAndWait()

# will wish a time designation
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12: 
        speak("Good Morning sir")

    elif hour >= 12 and hour < 17:
        speak("Good Afternoon sir")

    else: speak("Good Evening sir")

    speak("How may I help you?")

# to take a command from the user
def takeCommand():
    r = sr.Recognizer ()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try : 
        print("Recognizing...")
        question = r.recognize_google(audio, Language= 'en-us')
        print(f"user said: {question}\n")

    except Exception as e:
        print("Say that again please")


# main program
speak("Initializing Jarvis")
wishMe()
takeCommand()