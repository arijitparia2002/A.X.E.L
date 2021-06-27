import re
from playsound import playsound
import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # select 1 voice among the voices
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)
# print(voices)b


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


f = open('data.txt', 'r+')
set_alarm_command = f.read()

# extracted_time.seek(0)
f.truncate(0)
f.close()


def ring_alarm(set_alarm_command):
    alarm_time = [t for t in set_alarm_command.split() if ':' in t][0]
    h, m = alarm_time.split(':')
    if int(h) < 10 and len(h) == 1:
        h = '0'+h
    if int(m) < 10 and len(m) == 1:
        m = '0'+m
    alarm_time = h+':'+m

    if 'am' in set_alarm_command:
        alarm_time = alarm_time + ' AM'
    if 'pm' in set_alarm_command:
        alarm_time = alarm_time + ' PM'

    
    print(alarm_time)
    speak(f'Done sir! I have turned on the alarm for {alarm_time}')
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    print(current_time)

    if 'AM' in current_time and 'AM' in alarm_time:
        if alarm_time < current_time:
            speak(f'It\'s already past {alarm_time} sir! please give me a valid time!')
    elif 'PM' in current_time and 'PM' in alarm_time:
        if alarm_time < current_time:
            speak(f'It\'s already past {alarm_time} sir! please give me a valid time!')

    while 1:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        # print(current_time)

        if alarm_time == current_time:

            speak('Wake up Sir!')
            print('Wake up Sir!')

            playsound('Database\\Sounds\\alarm.wav')

        elif alarm_time < current_time:
            
            break


if __name__ == '__main__':

    ring_alarm(set_alarm_command)
