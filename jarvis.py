import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

print(voices)

engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour >=0 and hour <12 :
        speak("Good Moring")
    elif hour >=12 and hour <18 :
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello ! I am Jarvis . How may I help you ?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold=1

        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again please ..")

        return "None"
    return query
        

if __name__== "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing task
        if 'wikipedia' in query:
            print("Searching wikepedia .. ")
            query=query.replace("wikepedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\anubh\\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[5]))

        elif 'what is the time now' in query :
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir . The time is: {strTime}")
        #elif 'open coding environment' in query:
           # path='C:\\Users\\anubh\\AppData\\Local\\Programs\\Python\\Python38\\pythonw.exe'
           # os.startfile(path)
        ##email elif for future
        elif 'quit' in query:
            exit()
