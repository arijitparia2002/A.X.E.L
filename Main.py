import pyttsx3
from time import *
import datetime
import speech_recognition as sr
from functools import lru_cache
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes
import pyautogui  # controls mouse keybord and other automation task
import json
import requests
import time
from gtts import gTTS
from playsound import playsound
# features file
from Features import *
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # select 1 voice among the voices
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
# print(voices)b


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak_assis(audio):
    gTTS(audio).save('Assis.mp3')
    playsound('Assis.mp3')

def wake_up_call():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("sleeping...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        # print(f" Your command : {query}")

    except Exception as e:
        print(e)
        return "None"

    return query.lower()

def take_command():
    """
    Takes voice command from mic, and returns string output.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f" Your command : {query}")

    except Exception as e:
        print(e)
        # print("Say that again please!!")
        ans = ["Say that again please!!",
               'sorry sir! i did not get that.', 'please repeat again sir!']
        speak(random.choice(ans))
        return "None"

    return query.lower()


def take_command_hindi():
    """
    For Hindi language :
    Takes voice command from mic, and returns string output.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='hi')
        print(f" Your command : {query}")

    except Exception as e:
        print(e)
        # print("Say that again please!!")
        speak("Say that again please!!")
        return "None"

    return query.lower()


def task_exe():
    while 1:
        query = take_command()
        # search on youtube
        if 'search' in query and 'youtube' in query:
            query = query.replace('search', '')
            query = query.replace('axel', '')
            query = query.replace('in youtube', '')
            query = query.replace('from youtube', '')
            query = query.replace('on youtube', '')
            from Features import youTube_search
            youTube_search(query)

        # play on youtube
        elif 'play' in query and 'youtube' in query:
            query = query.replace('play', '')
            query = query.replace('axel', '')
            query = query.replace('in youtube', '')
            query = query.replace('from youtube', '')
            query = query.replace('on youtube', '')
            from Features import youTube_play
            youTube_play(query)

        # google search
        elif 'search' in query:
            query.replace('search', '')
            google_search(query)

        elif 'good afternoon' in query or 'good morning' in query or 'good evening' in query:
            wish_me()

        elif 'set' in query and 'alarm' in query:

            # for single digit alarm iinput
            num_list = [x for x in query if x.isdigit() == True]
            if ':' not in query and len(num_list) == 1:
                if int(num_list[0]) < 10:
                    query = query.replace(num_list[0], '0'+num_list[0]+':00')
                elif int(num_list[0]) < 12:
                    query = query.replace(num_list[0], num_list[0]+':00')
            # take a valid set alarm input
            while 1:
                if len([x for x in query.split() if ':' in x]) == 0:
                    speak('Sorry sir i could not get the time for alarm!')
                    query = take_command()
                elif 'a.m' not in query and 'p.m' not in query and 'am' not in query and 'pm' not in query:
                    speak('sorry sir! Please mention AM or PM !')
                    query = take_command()
                else:
                    query = query.replace('p.m', 'pm')
                    query = query.replace('a.m', 'am')
                    alarm(query)
                    break

        elif 'download' in query and 'youtube' in query:
            youTube_download()

        elif 'calculate' in query:
            calculator(query)

        elif 'temperature' in query:
            temperature(query)
        
        # break the loop, for it to rest
        elif 'rest now' in query:
            speak('Ok sir! i am going to sleep mode. Call me anytime!')
            break

        elif 'none' not in query:
            speak('Anything else i can do for you sir?')


if __name__ == '__main__':
    while 1:
        permission = wake_up_call()
        if 'wake up' in permission:
            speak('Yes sir! I am awake. what can i do for you.')
            task_exe()
        elif 'good afternoon' in permission or 'good morning' in permission or 'good evening' in permission:
            wish_me()
            task_exe()
        elif 'go offline' in permission or 'shut down' in permission:
            break
