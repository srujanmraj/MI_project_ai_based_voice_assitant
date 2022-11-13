import pyttsx3

def say(Text):
    engine  = pyttsx3.init("sapi5") # sapi5 - microsoft speaking api
    voices = engine.getProperty('voices') #taking the property
    engine.setProperty('voices',voices[0].id) #setting the voices
    engine.setProperty('rate',170) #setting up the speed
    print("     ")
    print(f"alpha: {Text}")
    engine.say(text = Text)
    engine.runAndWait()
    print("            ")

#say("srujan")
