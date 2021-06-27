import pyttsx3
import pywhatkit
import wikipedia
import time
import os
import webbrowser as web
from pywikihow import WikiHow, search_wikihow
import wolframalpha  # wolfram alpha site
import  datetime

wolfram_api_key = 'L4284H-2KUK99QVH4'


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # select 1 voice among the voices
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
# print(voices)b

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")

    speak("Hope you are great sir!, How can i help you?")


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


def alarm(command):
    with open('data.txt', 'a')as f:
        f.write(command)
    print(command)
    time.sleep(2)
    os.startfile('Database\\extra_programs\\alarm.pyw')


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

    expression = str(query)
    print(f'Expression : {expression}')
    result = wolfram(expression)
    result = result.replace('/', 'devided by')
    speak(f'The result is: {result}')


def temperature(query):
    result = wolfram(query)
    speak('Ok sir! searching...')
    result = wolfram(query)
    speak(f'According to my database, it\'s {result}')


if __name__ == '__main__':
    # google_search('who is iron man')
    #alarm('set alarm at 8:46 pm.')
    # youTube_download()
    print(wolfram('weather in gosaba'))
