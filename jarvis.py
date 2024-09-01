import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("Hello I am Jarvis AI. How may I help you?")

def takeCommand():
    #Takes microphone input from user and returns string output
 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password')
    server.sendmail('youremail@gmail.com',to, content)
    server.close()

if __name__== "__main__":
    wishMe()
    while True:
    # if 1:
        query=takeCommand().lower()
        
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak('According to Wikipedia')
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")    
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            
        elif 'open vs code' in query:
            codePath = "C:\\Users\\ridan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
           
        elif 'email to rida' in query:
            try:
                speak('What should I say?')
                content= takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except  Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")
                
        elif 'play a song' in query or 'play some song' in query:
            speak('What song should I play?')
            spotify = takeCommand()
            webbrowser.open(f'https:\\open.spotify.com\\search\\{spotify}')
            pyautogui.click(x=1055,y=617)
            speak('Playing'+ spotify)
                            
                    
        
        elif 'quit' in query:
            sys.exit(0)
                 
                