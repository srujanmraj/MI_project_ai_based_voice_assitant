#function
# 2 types
#1- non input functions ex; time , date , speedtest
#2- input - ex-google search, wikipedia
import datetime
from speak import say
import wikipedia
import pywhatkit
import pyjokes
import wolframalpha
import webbrowser
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from urllib.request import urlopen
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import os
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
import speech_recognition as sr

def takeCommand():
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    return query

def Time():
    time  = datetime.datetime.now().strftime("%H:%M")
    say(time)
    
def Date():
    date = datetime.date.today()
    say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    say(day)

def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "youtube" in query:
        webbrowser.open("youtube.com")



# def Wikipedia(tag,query):
#     name = str(query).replace("","")
#     import wikipedia
#     result = wikipedia.summary(name)
#     say(result)
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('apollohades2050@gmail.com', 'lightningdeath')
    server.sendmail('apollohades2050@gmail.com', to, content)
    server.close()


def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("what","").replace("where","").replace("about","").replace("wikipedia","")
        import wikipedia
        result = wikipedia.summary(name)
        say(result)

    elif "google" in tag:
        query =  str(query).replace("google","")
        query=str(query).replace("search","")
        pywhatkit.search(query)

    elif "joke" in tag:
        say(pyjokes.get_joke())
    
    elif "calculate" in tag:
             
        app_id = "6VUT62-AEXY978HH5" 
        client = wolframalpha.Client(app_id)
        indx = query.lower().split().index('calculate')
        query = query.split()[indx + 1:]
        res = client.query(' '.join(query))
        answer = next(res.results).text
        print("The answer is " + answer)
        say("The answer is " + answer)


    elif "write a note" in tag:
            say("What should i write, sir")
            note = takeCommand()
            file = open('alpha.txt', 'w')
            say("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
    elif "show note" in tag:
        say("Showing Notes")
        file = open("alpha.txt", "r")
        print(file.read())
        say(file.read(6))

    elif "email" in tag:
        
        try:
            say("What should I say?")
            content = takeCommand()
            to = "sruju16@gmail.com"   
            sendEmail(to, content)
            say("Email has been sent !")
        except Exception as e:
            print(e)
            say("I am not able to send this email")
