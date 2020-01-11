import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


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

    else: 
        speak("Good Evening sir")

    speak("How may I help you")

    


# to take a command from the user
def takeCommand():
    r = sr.Recognizer ()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try : 
        print("Recognizing...")
        command = r.recognize_google(audio, language = 'en-us')
        print(f"user said: {command}\n")
    except Exception as e:
        print("Say that again please")
        command = None

    return command


# main program


def main():
    wishMe()
    command = takeCommand()
# speaks summary of topic spoken with "Wikipedia" in the command
    if "Wikipedia" in command:
        speak ("searching wikipedia...")
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences =2)
        print(results)
        speak(results)

    # opens google home page with "open Google" in the command
    elif "open Google" in command:
        webbrowser.open ("google.com")

    # opens youtube on internet explorer with "open YouTube" in the command
    elif "open YouTube" in command:
        webbrowser.open("youtube.com")

    elif "play music" in command:
        songs = os.listdir("C:\\Users\\Ryan\\Downloads\\Music")
        print(songs)

    elif 'the time' in command:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f" Sir the time is {strTime}")

main()