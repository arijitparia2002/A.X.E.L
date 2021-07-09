import requests
import pyttsx3
from PIL import Image
import time
import pyautogui
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # select 1 voice among the voices
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
# print(voices)b


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

nasa_api_key = 'uHZ9vghYNeLWlvtGAsbpNu4n9KiYfSfQa9E7hngJ'


def nasa_news(date):
    speak(f'Extracting information from NASA, on the date {date}')
    url = 'https://api.nasa.gov/planetary/apod?api_key=' + str(nasa_api_key)
    parameters = {'date': date}

    r = requests.get(url, params=parameters)

    data = r.json()
    title = data['title']
    info = data['explanation']
    image_url = data['url']
    
    speak('Data extraction finished! I found something. Reading now.')
    engine.setProperty('rate', 170) #decreasing voice rate
    speak(f'The title is  {title}.')
    print(f'The title is : {title}.')

    # image extraction process
    try:
        img_req = requests.get(image_url)
        file_name = str(date) + '.jpg' #image file name
        file_path = 'Database\\Nasa_images\\' + file_name

        with open(file_path, 'wb') as  f:
            f.write(img_req.content)

        img = Image.open(file_path)

    
        speak(f'Found this image, displaying now.')
        img.show()
    except Exception as e:
        print(e)

    speak(f'According to NASA\'s database : {info}')
    print(f'According to NASA\'s database : {info}')
    time.sleep(2)
    speak(f'Done sir!')
    pyautogui.hotkey('alt','f4')

    engine.setProperty('rate', 185)

if __name__ == '__main__':
    nasa_news('2020-09-14')
    # pyautogui.hotkey('alt','F4')
