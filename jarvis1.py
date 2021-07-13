import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import psutil
import pyjokes
import pyautogui as pt
import time
import wolframalpha

engine = pyttsx3.init()
wolframalpha_app_id = 'wolfram alpha from api'

def speak(audio):
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time = datetime.datetime.now().strftime("%H : %M : %S")     #for 12 hours time
    speak('The current time is')
    speak(Time)


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak('the current date is')
    speak(date)
    speak(month)
    speak(year)


def wishes():
    speak('welcome back mubin')
    time_()
    date()

    #Greeting


    hour = datetime.datetime.now().hour

    if hour >=6 and hour <12:
        speak('Good morning sir!')

    elif hour >=12 and hour <18:
        speak('Good afternoon sir!')
    elif hour >=18 and hour <24:
        speak('Good evening sir!')
    else:
        speak('Good night sir!')

    speak('jarvis at your service, please tell me how can I help you today?')

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing......')
        query = r.recognize_google(audio , language='en-Us')
        print(query)

    except Exception as e:
        print(e)
        print('say that again pls.....')
        return 'None'
    return query

def cpu():
    usage = str(psutil.cpu_percent())
    speak('cpu is at'+usage)

    battery = psutil.sensors_battery()
    speak('battery is at')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def screenshot():
    speak('taking screenshot')
    img = pt.screenshot()
    img.save('D:/screenshot/scrsh.png')

if __name__ == '__main__':

    wishes()

    while True:
        query = TakeCommand().lower()

        #all commands will be stored in lower letter
        #for easy recognition

        if 'time' in query:     #it tells time
            time_()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak('searching....')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query,sentences=3)
            print(result)
            speak(result)


        elif 'search google' in query:
            speak('what to search?')
            search = TakeCommand().lower()
            speak('searching.....')
            wb.open_new_tab('https://www.google.com/search?q='+search)




        elif ' youtube' in query:
            speak('what to search')
            search_term = TakeCommand().lower()
            speak('here we go to youtube')
            wb.open('https://www.youtube.com/results?search_query='+search_term)

        elif 'cpu' in query:
            cpu()

        elif 'jokes' in query:
            jokes()


        elif 'offline' in query:
            speak('going offline sir!')
            quit()

        elif 'take note' in query:
            speak('what to write in note')
            notes = TakeCommand()
            file = open('notes.txt','w')

        elif 'show notes' in query:
            speak('showing notes...')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        #elif 'hi jarvis' in query:
            #speak('yes sir!')
            #wishes()

        elif 'screenshot' in query:
            screenshot()


        #elif 'play song' in query:
         #  song_dir = 'D:/songs'
          #music =os.listdir(song_dir)
         #os.startfile(os.path.join(song_dir))

        elif 'remember that' in query:
            speak('what should I remember?')
            memory = TakeCommand()
            speak('you asked me to remember that'+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('you asked me to rememeber that'+remember.read())

        #elif 'news' in query:
         #   try:

        elif 'where is' in query:
            query = query.replace('where is','')
            location = query
            speak('user asked to locate'+location)
            wb.open_new_tab('https://www.google.co.in/maps/place/'+location)

        elif 'stop listening' in query:
            speak('for how many second you want me to stop listening to your commands?')
            ans =int(input('time please'))
            time.sleep(ans)
            print(ans)

        #elif 'what is' in query or 'who is' in query:

        #    client = wol