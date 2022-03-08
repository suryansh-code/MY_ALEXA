import tkinter as tk
import requests
from ast import walk
from random import random
import wikipedia
import pyaudio
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import random


HEIGHT = 500
WIDTH = 600


#taking up the voice property
engine=pyttsx3.init('sapi5')


#tain the sample of vice of ai ie david or zira
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#the function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#the function which greet me according to the givin time
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
        
    elif hour>=12 and hour<=18:
        speak("good Afternoon")
        
    
    else:
        speak("good evening")
        
    
    
def put_cmd():
    query=takeCommand().lower()
        
    if "wikipedia" in query:
        speak('searching on wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
            
    elif "what can you do" in query:
        speak("i can play music ,open websites ,and , apps and many more")
        label['text']="i can play music ,open websites ,and , apps and many more"
    
    elif "open youtube" in query:
        webbrowser.open("youtube.com")
        label['text']="opening youtube"
            
    elif "open google" in query:
        webbrowser.open("google.com")
        label['text']="opening google" 
            
    elif "open stackoverflow" in query:
         webbrowser.open("stackoverflow.com")
         label['text']="opening sopening stackoverflow" 
            
    elif "pause" in query:
         run=False
        
    elif "how are you" in query:
        speak("i am fine . thanks for asking")
        label['text']="i am fine . thanks for asking"
        
    elif ("tell me about yourself" )in query:
        speak("hellow my name is hinata,i am an artificial intelligence assistent created as a group project , i am designed using python")
        label['text']="hellow my name is hinata,i am an artificial intelligence assistent created as a group project , i am designed using python"
        
    elif 'play music' in query:
        music_dir="F:\\music"
        songs=os.listdir(music_dir)
        ran=random.randint(0,len(songs))
        print(songs)
        label['text']=songs
        
        os.startfile(os.path.join(music_dir,songs[ran]))
    
    else:
        speak("not programe for this text yet")
        label['text']="not programe for this text yet"
                    
            
def takeCommand():
    wishMe()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        audio =r.listen(source)
        
    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said: {query}\n")
        
    except Exception as e:
        speak("can you repeat thae again please")
        return "NONE"
    
    label2['text'] = query
    return query
    



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label1 = tk.Label(root, image=background_image)
background_label1.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

label2 = tk.Label(frame, font=('Modern', 12))
label2.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text='LISTEN', font=30, command=lambda: put_cmd())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('MODERN', 15))
label.place(relwidth=1, relheight=1)

root.mainloop()