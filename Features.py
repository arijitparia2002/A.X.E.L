import pyttsx3
import pywhatkit
import wikipedia
import time
import os
import webbrowser as web
from pywikihow import WikiHow, search_wikihow
import wolframalpha  # wolfram alpha site
import datetime
from playsound import playsound
import random
import speech_recognition as sr
import pyautogui


wolfram_api_key = 'L4284H-2KUK99QVH4'
whatsapp_path = 'C:\\Users\\ariji\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
messenger_path = 'C:\\Users\\ariji\\AppData\\Local\\Programs\\Messenger\\Messenger.exe'
music_dir = "C:/Users/ariji/Music/songs"


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # select 1 voice among the voices
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
# print(voices)b


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
        ans = ["Say that again please!!",
               'sorry sir! i did not get that.', 'please repeat again sir!']
        speak(random.choice(ans))
        return "None"

    return query.lower()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")

    speak("Hope you are doing great !")


def startup():
    playsound('Database\\Sounds\\wake_up.mp3')
    wish_me()
    say_time()


def shutdown():
    speak("ok sir! Have a great day, Going offline... ")
    playsound('Database\\Sounds\\shutdown.mp3')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def youTube_search(topic):
    result = 'https://www.youtube.com/results?search_query=' + topic
    web.open(result)
    print(f'Topic : {topic}')
    speak(f'This is what i found from youtube on {topic}')


def youTube_play(topic):
    speak(f'playing video from youtube on the topic {topic}')
    print(f'Topic : {topic}')
    pywhatkit.playonyt(topic)

def play_music_vlc():
    os.system('taskkill /f /im vlc.exe')
    songs = os.listdir(music_dir)
    print(songs)
    # choosing a random song
    song = random.choice(songs)
    song_path = os.path.join(music_dir, song)
    speak(f"Playing {song}")
    os.startfile(song_path)
    pyautogui.hotkey('win', 'M')
    speak('Enjoy the music sir...')


def google_search(text_command):
    """
    1.pass the whole command text in the function no need to replace anything
    2.it will search the command on google
    3.Speak wikipidia result on the topic and print it also.
    4.If ask 'how to do something' gives list of instructions.
    """

    topic = text_command.replace('axel', '')
    topic = topic.replace('what is', '')
    topic = topic.replace('how to', '')
    topic = topic.replace('who is', '')
    topic = topic.replace('search', '')
    topic = topic.replace('what is', '')

    print(f'Topic : {topic}')

    Query = str(text_command)
    speak('Opening google chrome:')
    speak(f'This is the search results for, {Query}')
    # search the whole command on google
    pywhatkit.search(Query)

    if 'how to' in Query:
        # give a list of instruction of how to ....
        speak('I found a list of instruction on :')
        max_results = 1  # max list of instruction you want
        how_to_function = search_wikihow(query=Query, max_results=max_results)
        assert len(how_to_function) == 1
        how_to_function[0].print()
        speak(how_to_function[0].summary)
    else:
        # speak wikipidia results
        result = wikipedia.summary(Query, 2)
        print(f'wikipidia result : {result}')
        speak(f'according to wikipidia,  {result}')

    speak(f'sir! If you want me to close this tab, say yes !')
    reply = take_command()
    
    if 'yes' in reply or 'ok' in reply:
        pyautogui.hotkey('ctrl', 'w')
    else:
        speak('keeping the search result tab open!')

def alarm(command):
    with open('data.txt', 'a')as f:
        f.write(command)
    print(command)
    time.sleep(1)
    os.startfile('Database\\extra_programs\\alarm.pyw')

def say_time():
    str_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {str_time}")

def youTube_download():
    time.sleep(3)
    os.startfile('Database\\extra_programs\\yt_download.pyw')

def wolfram(query):

    try:
        requester = wolframalpha.Client(wolfram_api_key)
        requested = requester.query(query)
        answere = next(requested.results).text
        print(f'Result : {answere}')
        return(answere)
    except Exception as e:
        print(e)
        speak('Sorry sir! could not find the answere of your question. Please try again!')

def calculator(query):
    speak('Ok sir calculating...')
    query = query.replace('calculate', '')
    query = query.replace('plus', '+')
    query = query.replace('minus', '-')
    query = query.replace('multiply', '*')
    query = query.replace('into', '*')
    query = query.replace('multiply by', '*')
    query = query.replace('devide', '/')
    query = query.replace('by', '/')
    query = query.replace('point', '.')
    query = query.replace('to the power', '^')

    expression = str(query)
    print(f'Expression : {expression}')
    try:
        result = wolfram(expression)
        result = result.replace('/', 'devided by')
        speak(f'The result is: {result}')
    except Exception as e:
        print(f'e')

def temperature(query):  # returns the temparature
    result = wolfram(query)
    return (f'{result}')

def whatsapp_msg(query):
    if 'to' not in query:
        speak('who or where do want me to send message')
        name = take_command()
    else:
        name = query
    while 1:
        name = name.replace('the ', '')
        name = name.replace('a ', '')
        name = name.replace('name ', '')
        name = name.replace('is ', '')
        name = name.replace('to ', '')
        name = name.replace('message ', '')
        if 'None' not in name:
            speak(f'Did you say the name , {name}')
            reply = take_command()
            if 'yes' in reply:
                speak('ok')
            elif 'close whatsapp' in reply:
                speak('ok sir! closing whatsapp.')
                break
            else:
                speak('Tell me the name again sir!,')
                name = take_command()
                continue

        else:
            name = take_command()
            continue

        speak('What you want me to send.')
        while 1:
            msg = take_command()
            if 'None' not in msg:
                speak(f'Your message is, {msg} , do you want me to send sir?')
                print('fuck')
                reply = take_command()
                if 'yes' in reply or 'sure' in reply:
                    os.startfile(whatsapp_path)
                    time.sleep(10)
                    pyautogui.press('tab')
                    time.sleep(1)
                    pyautogui.write(name)
                    time.sleep(1)
                    pyautogui.press('tab')
                    time.sleep(0.5)
                    pyautogui.press('enter')
                    pyautogui.write(msg)
                    pyautogui.press('enter')
                    speak('Message sent sir!')
                    break
                elif 'no' in reply:
                    speak('do you want to repeat the msg,')
                    reply = take_command()
                    if 'close whatsapp' in reply or 'no' in reply:
                        speak('ok sir closing whatsapp...')
                        pyautogui.hotkey('ctrl', 'w')
                        break
                    else:
                        speak('please repeat your msg.')
                        continue
            else:
                speak('please repeat the message.')
                continue

        break
        # pywhatkit.sendwhatmsg('+913897831712','bluh bluh',18,44)
        # pywhatkit.sendwhatmsg_to_group('Dqe95xHr0bn4sQv7rsqAN9', 'This is a demo msg for testing.', 18,59)

def spam_here():
    speak('Tell me the message to spam')
    spam = take_command()
    speak(f'The message is {spam}')
    speak(f'Should i start sir?')
    reply = take_command()
    if 'no' not in reply and 'None' not in reply:
        try:
            speak(f'How many times should i spam ?')
            number = [x for x in take_command().split() if x.isdigit()==True][0]
            print(number)
            with open('data.txt', 'a')as f:
                f.write(f'{spam}||{number}')
                
            print(f'{spam} {number}')
            time.sleep(2)
            os.startfile('Database\\extra_programs\\spam_engine.pyw')
        except Exception:
            speak(f'Sorry sir there was an error! please try again!')
    else:
        speak(f'ok sir exiting spam...')

def nasa_news_teller(query):#takes query including date
    date = date_extract(query)
    from Database.extra_programs.nasa import nasa_news
    nasa_news(date)
    
def mars_image_viewer(query):#takes query including date
    date = date_extract(query)
    from Database.extra_programs.nasa import mars_image
    mars_image(date)

def date_extract(text):
    MONTHS = {"january": '01', "february": '02', "march": '03', "april": '04',
              "may": '05', "june": '06', "july": '07', "august": '08', "september": '09', "october": '10', "november": '11', "december": '12'}
    DAY_EXTENTIONS = ["rd", "th", "st", "nd"]
    
    if 'latest' in text or 'recent' in text:
        import datetime
        date = datetime.date.today()
    else:
        for word in text.split():
            if word in MONTHS.keys():
                month = MONTHS[word]
            elif word.isdigit() and len(word) == 4:
                year = str(word)
            elif word.isdigit():
                day = int(word)
            else:
                for ext in DAY_EXTENTIONS:
                    found = word.find(ext)
                    if found > 0:
                        try:
                            day = int(word[:found])
                        except:
                            pass
        # print(year,day,month)
        if len(str(day)) < 2:
            day = '0' + str(day)
        else:
            day = str(day)
        date = year + '-' + month + '-' + day

    print(date)
    return date

def messenger_msg(query):
    if 'to' not in query:
        speak('who, or where, do want me to send message : ')
        name = take_command()
    else:
        name = query
    while 1:
        name = name.replace('the ', '')
        name = name.replace('from ', '')
        name = name.replace('on ', '')
        name = name.replace('a ', '')
        name = name.replace('name ', '')
        name = name.replace('is ', '')
        name = name.replace('to ', '')
        name = name.replace('message ', '')
        name = name.replace(' ', '')
        if 'None' not in name:
            speak(f'Did you say the name , {name}')
            reply = take_command()
            if 'yes' in reply:
                speak('ok')
            elif 'close messenger' in reply:
                speak('ok sir! closing messenger.')
                break
            else:
                speak('Tell me the name again sir!,')
                name = take_command()
                continue

        else:
            name = take_command()
            continue
        
        print(name)
        speak('What you want me to send : ')
        while 1:
            msg = take_command()
            if 'None' not in msg:
                speak(f'Your message is, {msg} , do you want me to send sir?')
                reply = take_command()
                if 'yes' in reply or 'sure' in reply:
                    speak('ok sir! sending messege...')
                    os.startfile(messenger_path)
                    time.sleep(12)
                    pyautogui.hotkey('ctrl' , 'k')
                    time.sleep(2)
                    pyautogui.write(name)
                    time.sleep(5)
                    pyautogui.press('down')
                    time.sleep(2)
                    pyautogui.press('enter')
                    time.sleep(2)
                    pyautogui.write(msg)
                    time.sleep(2)
                    pyautogui.press('enter')
                    speak('Message sent sir!')
                    break
                elif 'no' in reply:
                    speak('do you want to repeat the msg,')
                    reply = take_command()
                    if 'close messenger' in reply or 'no' in reply:
                        speak('ok sir closing messsenger...')
                        # pyautogui.hotkey('ctrl', 'w')
                        break
                    else:
                        speak('please repeat your msg.')
                        continue
            else:
                speak('please repeat the message.')
                continue

        break

def messenger_call(query):

    name = query
    while 1:
        name = name.replace('the ', '')
        name = name.replace('from ', '')
        name = name.replace('on ', '')
        # name = name.replace('a ', '')
        name = name.replace('name ', '')
        name = name.replace('is ', '')
        name = name.replace('to ', '')
        name = name.replace('message ', '')
        name = name.replace('call ', '')
        name = name.replace(' ', '')
        if 'None' not in name:
            speak(f'Did you say the name , {name}')
            reply = take_command()
            if 'yes' in reply:
                speak('ok')
            elif 'close messenger' in reply:
                speak('ok sir! closing messenger.')
                break
            else:
                speak('Tell me the name again sir!,')
                name = take_command()
                continue

        else:
            name = take_command()
            continue
        
        print(name)
        try:
            speak(f'calling {name} from messenger')
            os.startfile(messenger_path)
            time.sleep(10)
            pyautogui.hotkey('ctrl' , 'k')
            time.sleep(.5)
            pyautogui.write(name)
            time.sleep(3)
            pyautogui.press('down')
            time.sleep(.2)
            pyautogui.press('enter')
            time.sleep(.2)
            pyautogui.press('tab')
            time.sleep(.1)
            pyautogui.hotkey('ctrl' , 'k')
            time.sleep(1)
            pyautogui.write(name)
            time.sleep(2)
            pyautogui.press('down')
            time.sleep(.1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('tab')
            time.sleep(.2)
            pyautogui.hotkey('shift', 'F10')
            time.sleep(1)
            pyautogui.press('down')
            time.sleep(.1)
            pyautogui.press('down')
            time.sleep(.2)
            pyautogui.press('down')
            time.sleep(.1)
            pyautogui.press('enter')
        except Exception as e:
            print(e)
            speak("Sorry Sir! There was an error while calling.")
            speak("Exiting messenger ... ")
            os.system('taskkill /f /im Messenger.exe')

        break

if __name__ == '__main__':
    # google_search('who is iron man')
    #alarm('set alarm at 8:46 pm.')
    # youTube_download()
    spam_here()
