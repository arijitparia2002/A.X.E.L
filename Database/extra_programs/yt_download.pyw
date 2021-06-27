import pyautogui
import requests
import pyttsx3
import pyperclip
from pytube import YouTube
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # select 1 voice among the voices
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
# print(voices)b

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == "__main__":
    
    while 1:
        try:
            import time
            time.sleep(2)
            pyautogui.hotkey('alt', 'd')
            pyautogui.hotkey('ctrl', 'c')
            link = str(pyperclip.paste())
            print('i am here')
            print('i am here')
            response = requests.get(link)
            speak('Ok sir! Trying to download the youtube video..')
            speak('please wait sir! The video is downloading, I will notify you when it is done.')
            print('please wait sir! The video is downloading')

            # download yt video
            url = YouTube(link)
            video = url.streams.first()
            video.download('C:\\Users\\ariji\\Downloads\\')
            playsound('Database\\Sounds\\notification.mp3')
            speak('Sir! Video is downloaded successfullyand saved in the downloads folder.')
            break   
        except Exception:
            speak('Sorry sir! could not download the video. Try again please!')
            break