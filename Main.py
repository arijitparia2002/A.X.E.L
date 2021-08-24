import pyttsx3
from time import *
import datetime
import speech_recognition as sr
from functools import lru_cache
import webbrowser
import os
import random
import smtplib
import pyjokes
import pyautogui  # controls mouse keybord and other automation task
import json
import time
from gtts import gTTS
from playsound import playsound
# features file
from Features import *
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # select 1 voice among the voices
newVoiceRate = 185
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
        print(f" : {query}")

    except Exception as e:
        print(e)
        print("None")
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
        query = r.recognize_google(audio, language='en')
        print(f" Your command : {query}")

    except Exception as e:
        print(e)
        # print("Say that again please!!")
        # ans = ["Say that again please!!",
        #        'sorry sir! i did not get that.', 'please repeat again sir!']
        # speak(random.choice(ans))
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
        print(f" Your command : {query.lower()}")

    except Exception as e:
        print(e)
        # print("Say that again please!!")
        speak("Say that again please!!")
        return "None"

    return query.lower()


def task_exe():
    no_query_loop = 0
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
            no_query_loop = 0

        # play on youtube
        elif 'play' in query and 'youtube' in query:
            query = query.replace('play', '')
            query = query.replace('axel', '')
            query = query.replace('in youtube', '')
            query = query.replace('from youtube', '')
            query = query.replace('on youtube', '')
            from Features import youTube_play
            youTube_play(query)
            speak('Enjoy the video sir! Call me if you need anything!')
            break

        elif "close" in query and "chrome" in query:
            speak('Ok sir! closing chrome')
            os.system('taskkill /f /im chrome.exe')
            break

        elif 'play' in query and 'music' in query or 'song' in query:
            os.system('taskkill /f /im vlc.exe')
            music_dir = "C:/Users/ariji/Music/songs"
            songs = os.listdir(music_dir)
            print(songs)
            # choosing a random song
            song = random.choice(songs)
            song_path = os.path.join(music_dir, song)
            speak(f"Playing {song}")
            os.startfile(song_path)
            pyautogui.hotkey('win', 'M')
            speak('Enjoy the music sir...')
            break

        elif 'stop' in query and 'music' in query:
            speak('Ok sir! closing media player.')
            os.system('taskkill /f /im vlc.exe')

        # google search
        elif 'search' in query:
            query = query.replace('search', '')
            google_search(query)
            time.sleep(1)
            speak('Do you want me to close the chrome window sir?say yes or no')
            while 1:
                reply = take_command()
                if 'yes' in reply:
                    speak('Ok sir! closing chrome')
                    os.system('taskkill /f /im chrome.exe')
                    break

                elif 'no' in reply:
                    speak('Ok sir!')
                    break
                else:
                    speak('plese say , yes or no sir!')
            no_query_loop = 0

        elif 'good afternoon' in query or 'good morning' in query or 'good evening' in query:
            wish_me()
            no_query_loop = 0

        elif 'set' in query and 'alarm' in query:
            try:
                # for single digit alarm iinput
                num_list = [x for x in query if x.isdigit() == True]
                if ':' not in query and len(num_list) == 1:
                    if int(num_list[0]) < 10:
                        query = query.replace(
                            num_list[0], '0'+num_list[0]+':00')
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
            except Exception:
                speak(
                    'Sorry Sir! there was an error while setting the alarm, please try again!')

        elif 'stop' in query and 'alarm' in query:
            with open('data.txt', 'a')as f:
                f.write(query)
        elif 'download' in query and 'youtube' in query:
            youTube_download()
            no_query_loop = 0

        elif 'calculate' in query:
            calculator(query)
            no_query_loop = 0

        elif 'temperature' in query:
            speak('Ok sir! searching...')
            speak(f'According to my database, it\'s {temperature(query)}')
            no_query_loop = 0

        # tels the time
        elif 'time' in query and ('say' in query or 'tell' in query or 'what is' in query):
            say_time()
            no_query_loop = 0

        # break the loop, for it to rest
        elif 'rest now' in query or 'sleep ' in query:
            speak('Ok sir! i am going to sleep mode. Call me anytime!')
            break

        elif ('go offline' in query or 'shut down' in query) and 'axel' in query or 'excel' in query:
            shutdown()
            quit()

        elif 'send' in query and 'whatsapp' in query:
            os.system('taskkill /f /im WhatsApp.exe')
            query = query.replace('whatsapp', '')
            query = query.replace('send ', '')
            whatsapp_msg(query)
            speak('Do you want me to close whats app sir!')
            ans = take_command()
            if 'yes' in ans or 'close' in ans:
                os.system('taskkill /f /im WhatsApp.exe')
            else:
                speak('OK sir, keeping whatsapp open for you.')

        elif 'spam' in query and 'stop' in query:
            speak('Stopping spam..')
            
            with open('data.txt', 'a')as f:
                f.write(query)

        elif 'spam' in query:
            spam_here()
        
        elif 'close' in query and 'whatsapp' in query:
            os.system('taskkill /f /im WhatsApp.exe')
            speak('OK sir, closing whats app.')

        elif 'volume' in query and 'up' in query or 'increase' in query:
            fold = 10
            try:
                if '%' in query:
                    fold = int([i.rstrip('%')
                               for i in query.split() if '%' in i][0])
                else:
                    fold = int([i for i in query.split()
                               if i.isdigit() == True][0])

                print(fold)
                if fold > 100:
                    raise 'cant do'
                for i in range(fold//2):
                    pyautogui.press('volumeup')
            except Exception:
                fold = 10
                [pyautogui.press('volumeup') for i in range(5)]
            speak(f'{fold} percent Volume up, sir!')

        elif 'volume' in query and 'down' in query or 'decrease' in query:
            fold = 10
            try:
                if '%' in query:
                    fold = int([i.rstrip('%')
                               for i in query.split() if '%' in i][0])
                else:
                    fold = int([i for i in query.split()
                               if i.isdigit() == True][0])
                print(fold)
                if fold > 100:
                    raise 'cant do'
                for i in range(fold//2):
                    pyautogui.press('volumedown')
            except Exception:
                fold = 10
                [pyautogui.press('volumedown') for i in range(5)]
            speak(f'{fold} percent Volume down, sir!')

        elif 'mute' in query or 'unmute' in query:
            pyautogui.press('volumemute')
            speak('Unmuted sir!')
    ###############################Space Exploration #########################
        elif 'nasa' in query and 'news ' in query:
            try:
                nasa_news_teller(query)
            except Exception as e:
                print(e)
                speak('Sorry sir, there was an error while extracting the information. Maybe try another date.')

        elif 'mars' in query and 'images' in query or  'picture' in query or 'image' in query or  'pictures' in query:
            try:
                mars_image_viewer(query)
            except Exception as e:
                print(e)
                speak('Sorry sir, there was an error while extracting the information. Maybe try another date.')
    
    ##########################################################################
        elif 'shut down ' in query and 'pc' in query or 'device' in query or 'laptop' in query:
            speak('Do you want to shut down the device sir? say yes or no')
            ans = take_command()
            if 'yes' in ans:
                os.system('shutdown /s /t 1') 
            else:
                speak('ok sir! Keeping the device ON!')
        

        elif 'send' in query and 'messenger' in query:
            os.system('taskkill /f /im Messenger.exe')
            query = query.replace('messenger','')
            query = query.replace('send ', '')
            messenger_msg(query)
            speak('Do you want me to close messenger app sir!')
            ans = take_command()
            if 'yes' in ans or 'close' in ans:
                os.system('taskkill /f /im Messenger.exe')
            else:
              speak('OK sir, keeping messenger open for you.')
                 
        elif 'close' in query and 'messenger' in query:
            os.system('taskkill /f /im Messenger.exe')
            speak('OK sir, closing messenger .')   

        elif 'call' in query and 'messenger' in query:
            os.system('taskkill /f /im Messenger.exe')
            query = query.replace('messenger','')
            query = query.replace('call ', '')
            messenger_call(query)
            speak('ok sir,enjoy you call ! going in rest mode.')
            break

        else:
            no_query_loop += 1
            if no_query_loop == 1:
                ans = ["Say that again please!!",
                'sorry sir! i did not get that.', 'please repeat again sir!']
                speak(random.choice(ans))
            elif no_query_loop == 2:
                speak('Anything else i can do for you sir?')
            elif no_query_loop == 3:
                speak('Sir! Are you there? please say something!')
            elif no_query_loop == 5:
                speak('Sir! if you are there, say yes or No.')
                ans = take_command()
                if 'yes' in ans or 'yeah' in ans:
                    no_query_loop = 0
                    query = ans
                    speak('ok sir! what can i do for you?')
                else:
                    speak('Seems you are not there sir! call me if you need anything.')
                    break
            elif no_query_loop == 6:
                speak('Ok sir! call  me if you need anything..')
                break


def run_axel():
    
    i = 1
    while 1:
        # storing the outside temparature and weather
        if i == 1:
            temp = str(temperature('temparature in gosaba'))
            i += 1

        permission = wake_up_call()
        
        if 'wake up' in permission:
            speak('Yes sir! I am awake. what can i do for you.')
            task_exe()

        elif 'good afternoon' in permission or 'good morning' in permission or 'good evening' in permission:
            startup()
            speak(f'temparature outside is,{temp}')
            speak('let\'s get started sir! what can i do for you')
            task_exe()

        elif 'axel' in permission or 'excel' in permission or 'hey' in permission or 'hello' in permission:
            speak('Yes sir! I\'m here, what you want me to do sir!')
            task_exe()

        elif 'go offline' in permission or 'shut down' in permission:
            shutdown()
            quit()


if __name__ == '__main__':
    run_axel()










