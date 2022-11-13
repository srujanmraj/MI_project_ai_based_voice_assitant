import random
import json
import torch
from brain import NeuralNet
from NeuralNetwork import bag_of_words, tokenize

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

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open("intents.json",'r') as json_data:
    intents = json.load(json_data)


FILE = "TrainData.pth"
data =  torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state =  data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#------
Name = "Alpha"
from listen import Listen
from speak import say
from task import NonInputExecution
from task import InputExecution
def Main():
    sentence = Listen()
    result = str(sentence)
    #query = takeCommand().lower()
    if sentence == "quit" or sentence == "exit":
        exit()

    sentence = tokenize(sentence)
    X = bag_of_words(sentence,all_words)
    X = X.reshape(1,X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)

    _ , predicted = torch.max(output,dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output,dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent["responses"])

                if "time" in reply:
                    NonInputExecution(reply)
                elif "date" in reply:
                    NonInputExecution(reply)
                elif "day" in reply:
                    NonInputExecution(reply)
                elif "wikipedia" in reply:
                    InputExecution(reply,result)
                elif "google" in reply:
                    InputExecution(reply,result)
                elif "joke" in reply:
                    InputExecution(reply, result)
                elif "calculate" in reply:
                    InputExecution(reply,result)
                elif 'youtube' in reply:
                    NonInputExecution(reply)
                    # say("Here you go to Youtube\n")
                    # webbrowser.open("youtube.com")
                elif "write a note" in reply:
                    InputExecution(reply,result)
                elif "show note" in reply:
                    InputExecution(reply, result)
                elif "email" in reply:
                    InputExecution(reply,result)

                else:
                    say(reply)

while True:
    Main()


