import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

print("Initializing YANTRA MAANAV")

MASTER = "Shrey"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning" + MASTER)
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening" + MASTER)
    speak("Please wait, Installing required drivers....")
    speak("All systems are normaled......")
    speak("Tempreture is under control.........")
    speak("I am YANTRA MAANAV version 1 point o speed 1 giga heartz space 1 terabyte. How may i help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        speak("opening the task")

    except Exception as e:
        print("Say that again please")
        query = None
    return query

wishMe()
query = takeCommand()
if 'wikipedia' in query.lower():
    speak("searching wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)

elif 'open youtube' in query.lower():
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open github' in query.lower():
    url = "github.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open instagram' in query.lower():
    url = "instagram.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir = "F:\\YANTRA MAANAV"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[1]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f'{MASTER} the time is {strTime}')

elif 'open code' in query.lower():
    codePath = "Your Path"
    os.startfile(codePath)

elif 'who are you' in query.lower():
    speak("I am JARVIS, My master SHREY GHELANI had made me on 10-february-2020, i am his personal assistant")

elif 'i am hungry' in query.lower():
    url = "swiggy.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open facebook' in query.lower():
    url = "facebook.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'good bye' in query.lower():
    speak("Bye Sir, I am in standby position now")


elif 'open fortnite' in query.lower():
    codePath = "Your Path"
    os.startfile(codePath)
