from datetime import datetime
import time
import pywhatkit as kit
import speech_recognition as sr
import pyttsx3
import wikipedia
import pyjokes


 
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
       with sr.Microphone() as source:
        print('listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in  command:
            command = command.replace('alexa','')
        print(command)
    except:
         pass
    return command
     
def run_alexa():
    comm = take_command()
    if 'play' in comm:
        song = comm.replace('play','')
        talk('playing '+song)
        kit.playonyt(song)
    elif 'time' in comm:
        time = datetime.now().strftime('%I:%M %p')
        talk('Current time is :'+time)
    elif 'who' in comm:
        person = comm.replace('who','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in comm:
        talk('Sorry, I have a headache!')
    elif 'are you single' in comm:
        talk('Currently I am in a reltionship with wifi')
    elif 'joke' in comm:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry I dont understand Please repeat the command again!')


while True:
    run_alexa()