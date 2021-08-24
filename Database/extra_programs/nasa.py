import requests
import pyttsx3
from PIL import Image
import time
import pyautogui
import random
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # select 1 voice among the voices
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
# print(voices)

nasa_api_key = 'uHZ9vghYNeLWlvtGAsbpNu4n9KiYfSfQa9E7hngJ'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    """
    Takes voice command fromk mic, and returns string output.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)

    except Exception as e:
        print(e)
        return "None"

    return query.lower()


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
    engine.setProperty('rate', 170)  # decreasing voice rate
    speak(f'The title is  {title}.')
    print(f'The title is : {title}.')

    # image extraction process
    try:
        img_req = requests.get(image_url)
        file_name = str(date) + '.jpg'  # image file name
        file_path = 'Database\\Nasa_images\\' + file_name

        with open(file_path, 'wb') as f:
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
    pyautogui.hotkey('alt', 'f4')

    engine.setProperty('rate', 185)


def mars_image(date):
    speak(f'Extracting images from NASA\'s database, on the date {date}')
    url = f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={date}&api_key={nasa_api_key}'
    # print(url)
    r = requests.get(url)
    data = r.json()
    photos = data['photos']  # list of photos

    speak(f'Extraction finishged , i found total {len(photos)} pictures.')
    speak('How many do you want to see SIR?')

    ans = take_command()

    try:
        num = int([n for n in ans.split() if n.isdigit() == True][0])
    except:
        speak('Sorry sir, did not get that!')
        num = 5

    speak(f'Showing random {num} images on your screen. ')
    # random.sample() -- selects random elements without repeating them

    rand_photos_index = sorted(random.sample(range(len(photos)), k=num))

    i = 1
    for index in rand_photos_index:
        try:
            photo = photos[index]
            camera = photo['camera']
            rover = photo['rover']
            rover_name = rover['name']
            camera_name = camera['name']
            camera_full_name = camera['full_name']

            img_url = photo['img_src']
            img_req = requests.get(img_url)

            file_name = str(date) + str(index) + '.jpg'  # image file name
            file_path = 'Database\\Mars_images\\' + file_name

            with open(file_path, 'wb') as f:
                f.write(img_req.content)

            img = Image.open(file_path)
            speak(f'Displaying Image number {i}.')
            

            if i != 1:
                pyautogui.hotkey('alt', 'f4')
            
            i += 1
            img.show()

            engine.setProperty('rate', 170)  # decreasing voice rate
            speak(
                f"Image ID : {index + 1} . Taken from {rover_name} rover on date {str(photo['earth_date'])}")
            speak(
                f'This image was  captured with {camera_name} camera, Full name : {camera_full_name}')
            time.sleep(2)

        except:
            speak('Sorry Sir! could not display this image.')

    speak('Done sir!')

    engine.setProperty('rate', 185)
    pyautogui.hotkey('alt', 'f4')


if __name__ == '__main__':
    nasa_news('2020-11-14')
    # pyautogui.hotkey('alt','F4')
