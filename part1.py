#making a simple jarvis programe

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

    speak("hellow  my name is hinata. how can i help you?")
    
    
    
#the function takeCommand take our voice as input from microphone
def takeCommand():
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
    
    return query

#the function for the stone paper scissor game 
def stonepaper():
    run=True
    while run:
        lst=["stone","paper","scissor"]
        my=random.choice(lst)
    
        speak("what you want to choose from the stone paper scissor")
        yourchoice=takeCommand().lower()
    
        if my=="stone" and "paper" in yourchoice:
             print(f"user choice{yourchoice}")
             print(f"my choice is {my}")
             speak("nice move you win")
         
        elif my=="paper" and "stone" in yourchoice:
             print(f"user choice{yourchoice}")
             print(f"my choice is {my}")
             speak("lol i win")
           
        elif my=="scissor" and "paper" in yourchoice:
             print(f"user choice{yourchoice}")
             print(f"my choice is {my}")
             speak("lol i win")
     
        elif my=="paper" and "scissor" in yourchoice:
             print(f"user choice {yourchoice}")
             print(f"my choice is {my}")
             speak("nice that was preety smart guess you win")
    
        elif my=="scissor" and "stone" in yourchoice:
             print(f"user choice{yourchoice}")
             print(f"my choice is {my}")
             speak("nice you win")
        
        elif  my=="stone" and "scissor" in yourchoice:
             print(f"user choice{yourchoice}")
             print(f"my choice is {my}")
             speak("nice you win")
             speak("quiting the game")
        elif "pause" in yourchoice:
            run=False
        else:
            speak("please choose the valid option")
    
        
#the gues the number game function is written here
def guessit():
    speak("you are in a condition ,where you have only two choices ,the condition is you are in a car whose breaks are fail ,what you will do ,the first choice is pull the handbreaks , or the seconfd choice is nuteral  the car")
    run=True
    while run:
       my=takeCommand().lower()
       if "handbrake" in my:
          print(my)
          print("you loose")
          speak("you die because of sudden friction which roll the vehicle")
        
       elif "neutral" in my:
          print(my)
          print("you win")
          speak("that was the clever decision you win this game")
        
       elif "quit" in my:
          print("my")
          print("exiting")
          speak("exiting")
       else:
           speak("the option you choose is invalid")

if __name__=='__main__':
    wishMe()
    run=True
    while run:
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
    
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            
        elif "open google" in query:
            webbrowser.open("google.com") 
            
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
            
        elif "pause" in query:
            run=False
        
        elif "how are you" in query:
            speak("i am fine . thanks for asking")
        
        elif ("tell me about yourself" )in query:
            speak("hellow my name is hinata,i am an artificial intelligence assistent created as a group project , i am designed using python")
        
        elif 'play music' in query:
            music_dir="F:\\music"
            songs=os.listdir(music_dir)
            ran=random.randint(0,len(songs))
            print(songs)
            os.startfile(os.path.join(music_dir,songs[ran]))
            
        elif "play game" in query:
            speak("which game you want to play from my game list ,first is stone paper scissor ,and the second is predict the output")
            
        elif "stone paper scissor" in query:
            stonepaper()
            
        elif "guess it" in query:
            guessit()
            
            
            

