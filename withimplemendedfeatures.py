import webbrowser as wb 
import speech_recognition as sr 
from tkintern import *
from time import ctime
import time
import os 
from gtts import gTTS 
import pygame
from pygame import mixer
from threadpoolct1 import threadpool_info

def speak(audioString):
    global x 
    b=audioString
    if len(b)==0:
        return
    tts=gTTS(text=b,lang='en-us')
    tts.save("voice%s.mp3"%(x))
    
    pygame.init()
    pygame.display.set_model((2,1))
    mixer.music.load("voice%s.mp3"%(x))
    mixer.music.play(0)
    
    x+=1 
    
    clock=pygame.time.Clock()
    Clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
        

 def recordAudio():
     r=sr.Recognizer()
     with sr.Microphone() as source :
         print(" speak...")
         audio=r.listen(source)
         print("heard..waiting for google to recognize audio")
         
     data=""
     
     try:
         data=r.recognize_google(audio)
         print(" you said: "+data)
     except sr.UnknownValueError:
         print(" google could not understand audio")
     except sr.RequestError as e:
         print(" could not request results from google speech recognition ; {0}".format(e))
     return data
     
     
def jarvis(data):
    if "how are you" in data:
        speak(" i am fine")
    elif "what is the time " in data:
        speak(ctime())
    elif "where is " in data:
        data=data.split("")
        location=data[2]
        speak(" i will show you where "+ location+"is.")
        wb.open_new_tab("https://www.google.n1/maps/place/" +location ="/&amp;")
    elif " book an ola " in data:
    	  wb.open_new_tab("https://book.olacabs.com/?")
    elif " what is weather of " in data:
    	  data=data.split("")
	  location=data[4]
	  wb.open_new_tab("http://api.openweathermap.org/data/2.5/weather?q="+location+"")
    elif " search " in data:
    	  data=data.split(“”)
	  location=data[1]
	  wb.open_new_tab("https://www.google.com/search?q="+location+"")
    else:
        speak("...... i did not get what you said !!") 
        
     
    
    x=0
    print("start....")
    speak("hi ! Ted, what can i do for you ")
    data=recordAudio()
    jarvis(data)
    speak("turning off the program ")
    print("run complete")
    
    
