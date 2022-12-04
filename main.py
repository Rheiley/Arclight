import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import sys
import bs4
import requests

print("I am Arclight, Rheiley's personal assistant")
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
command = ''

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try: 
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            global command
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'arclight' in command:
                command = command.replace('arclight', '')
                print(command)
    except:
        pass
    return command

def run_arclight():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing ' + song)
        pywhatkit.playonyt(song)   
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'search up' in command or 'tell me about' in command or 'who is' in command:
        person = command.replace('who is' or 'search up' or 'tell me about', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'thanks' in command or 'thank you' in command:
        talk("You're welcome, good friend")
    elif 'who are you' in command or 'what are you' in command:
        talk("I am simply an illusion")
    elif 'google docs' in command:
        webbrowser.open_new("https://docs.google.com/document/u/0/")
    elif 'google slides' in command:
        webbrowser.open_new("https://docs.google.com/presentation/u/0/?tgif=d")
    elif 'google drive' in command:
        webbrowser.open_new("https://drive.google.com/drive/u/0/my-drive")
    elif 'hello' in command or "what's up" in command:
        talk("Hello, nice weather we're having")
    elif 'google' in command:
        query = command.replace('google','')
        webbrowser.open_new("https://google.com/search?q=" + query)
    elif 'look up' in command:
        query = command.replace('look up','')
        webbrowser.open_new("https://google.com/search?q=" + query)    
    elif 'goodbye' in command or 'goodnight' in command or 'see you later' in command:
        sys.exit(talk("see you later"))

while True:
    command = ''
    run_arclight()

