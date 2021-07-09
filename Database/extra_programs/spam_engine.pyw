from playsound import playsound
import datetime
import pyttsx3
import pyautogui
import time
import speech_recognition as sr
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # select 1 voice among the voices
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
# print(voices)b

# def take_command():
#     """
#     Takes voice command from mic, and returns string output.
#     """
#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("I am listening...")
#         audio = r.listen(source)

#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en')
#         # print(f" Your command : {query}")

#     except Exception as e:
#         print(e)

#     return query.lower()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


f = open('data.txt', 'r+')
text = f.read()
spam_msg, spam_number = text.split('||')
# extracted_time.seek(0)
f.truncate(0)
f.close()

if __name__ == '__main__':
    i = 100
    try:
        speak(f'Starting spam please do not touch the screen...')
        for i in range(int(spam_number)):
            pyautogui.write(spam_msg)
            time.sleep(2)

            # stopping spam on command
            try:
                with open('data.txt', 'r+') as f:
                    command = f.read()

                    # extracted_time.seek(0)
                    f.truncate(0)
                if 'stop' in command and 'spam' in command:
                    i = -1
                    raise 'error'
            except:
                speak('spam is terminated.')
                break

            #####################################################
            pyautogui.press('enter')
            print('Spaming...')
        if i != -1:
            playsound('Database\\Sounds\\notification.mp3')
            speak(f'Done spamming sir!')

    except Exception:
        speak(f'There was an error in spamming sir! please try again.')
