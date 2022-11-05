import pyttsx3
import datetime
from gtts import gTTS
import playsound
import speech_recognition as sr
import wikipedia
import weathercom
import json
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# name = input("enter your name :-")


engine.setProperty('voice',voices[0].id)  # change voice from here

# print (voices[0].id) # to cheak voices avalable in system

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():

    hour = int(datetime.datetime.now().hour)

    if  hour >= 20 and hour < 6:
        speak(f"Good night sir!")

    elif hour >= 6 and hour < 11:
        speak(f"Good morning sir !")

    elif hour >=11 and hour< 16:
        speak(f"Good Afternoon sir!")

    else:
        speak(f"Good evening sir!")


def time():
    strDate = datetime.datetime.now().strftime("%d %B")
    strDay = datetime.datetime.now().strftime("%A")
    speak(f"today is {strDay} and date {strDate}")
    speak("i am devil,how can i help you!")


def audio_playback(text):
    filename = "test.mp3"
    tts = gTTS(text=text, lang='en-in')
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def weatherReport(city):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    humidity = json.loads(weatherDetails)["vt1observation"]["humidity"]
    temp = json.loads(weatherDetails)["vt1observation"]["temperature"]
    phrase = json.loads(weatherDetails)["vt1observation"]["phrase"]
    return humidity, temp, phrase


def takeCommand():           # this function is take input from user as voice using micropone of system
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")   #this shows microphonw=e is listening our voice
        r.pause_threshold = 1 # similary you can increse enery_threshold for high voice
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query} \n ")

    except Exception as e:
        #print(e)
        speak(f" ")
        return "None"
    return query



if _name_ == '_main_':
    wishMe()
    time()
    while True:
        query = takeCommand().lower() 

        if "exit" in query:
            exit() 

        elif "weather" in query:
            city = "Solapur"
            humidity, temp, phrase = weatherReport(city)
            speak("currently in " + city + "  temperature is " + str(temp)+ " degree celsius, " + "humidity is " + str(humidity) + " percent and sky is " + phrase)
            print("currently in " + city + "  temperature is " + str(temp) + "degree celsius, " + "humidity is " + str(humidity) + " percent and sky is " + phrase)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif "open moodle" in query:
            webbrowser.open("http://103.127.76.195/login/index.php")

        elif "open coursera" in query:
            webbrowser.open("https://www.coursera.org/")

        elif "open instagram" in query:
            speak("opening instagram")
            webbrowser.open("instagram.com")

        elif "play music" in query:
            music_dir = "D:\\youtube\\music"    # copy path on music drive here
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))

        elif "play video" in query:
            video_dir = "D:\\youtube\\vantas\\minecraft"    # copy path on music drive here
            video = os.listdir(video_dir)
            print(video)
            os.startfile(os.path.join(video_dir,video[1]))


        elif "next" in query:
            music_dir = "D:\\youtube\\music"    # copy path on music drive here
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[2]))


        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif "open code" in query:
            speak("visual studio opening please wait!")
            code_path="E:\\desktop\\Visual_Studio"
            os.startfile(code_path)

        elif "who are you" in query:
            speak(" I am Devil ,nice to meet you")

        elif "who am I"  in query:
            speak("sorry sir i don't know please put your name")
            Name=input("enter your name:--> ")
            speak(f"hello {Name} nice to meet you! ")

        elif "video of" in query:
            webbrowser.open(f'youtube.com\{query}')
