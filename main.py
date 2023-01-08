from Jarvis import JarvisAssistant
import re
import os
import random
import pprint
import datetime
import requests
import sys
import urllib.parse  
import wikipedia     
import smtplib
from pywikihow import search_wikihow
import pyjokes
import time
import PyPDF2
from bs4 import BeautifulSoup
import pyautogui
import pywhatkit
import wolframalpha
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
import speech_recognition as sr
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pyttsx3 #module to build a assistance
import webbrowser
from googlesearch import search
from PyQt5.uic import loadUiType
from Jarvis.features.gui import Ui_MainWindow
from Jarvis.config import config
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
from Jarvis.features.curloc import *

obj = JarvisAssistant()



# ================================ MEMORY ===========================================================================================================

GREETINGS = ["hello jarvis","hello", "jarvis", "wake up jarvis", "you there jarvis", "time to work jarvis", "hey jarvis",
             "ok jarvis", "are you there"]
GREETINGS_RES = ["always there for you sir", "i am ready sir",
                 "your wish my command", "how can i help you sir?", "i am online and ready sir"]

# EMAIL_DIC = {
#     'myself': 'developerdwm@gmail.com',
#     'friend email': 'itsvishal2417@gmail.com',
# }

# CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy","show me the calender","calender"]
# =======================================================================================================================================================

Assistant =pyttsx3.init('sapi5')   # microsoft ide for speech recognition.
voices=Assistant.getProperty('voices') #creating instance variable\


# print(voices)
Assistant.setProperty('voices',voices[7].id) #setting id of first voice to voices variable
# ) is male voice, 1 is female voice
Assistant.setProperty('rate',170) #changing speed of jarvis speech . default=200


def speak(text):
    obj.tts(text) #text to speech lib


app_id = config.wolframalpha_id


def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None

def takeHindi():
    command=sr.Recognizer()
    # print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        print("Listening......")
        # command.pause_threshold=1
        command.adjust_for_ambient_noise(source, duration=1) #remove background soun
        audio=command.listen(source)

        try:
            print("Recognizing......")
            query = command.recognize_google(audio,language="hi")  #audio to text converter
            print(f"You said : {query}")

        except Exception as Error:
            return "none"         #print("Something went wrong")

        return query.lower() 

def Tran():
    speak("Tell me the line!")
    line=takeHindi()
    print(line)
    translator= Translator()
    result=translator.translate(line)
    Text=result.text
    speak(f"The translation for this line is : {Text}")
    print(Text)

def startup():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
    # wish()
    
def SpeedTest():
    import speedtest
    speak("Checking Speed....")
    speed=speedtest.Speedtest(secure=True)
    downloading=speed.download() #mbpt
    correctDown=int(downloading/800000)
    uploading=speed.upload() #mbpt
    correctUp=int(uploading/800000)
    speak(f"Your Downloading Speed is {correctDown} mbps. Your Uploading Speed is {correctUp} mbps")
    print(f"Your Downloading Speed is {correctDown} mbps. Your Uploading Speed is {correctUp} mbps")

def filterwords(command):
    command=command.replace("to","")
    command=command.replace("about","")
    command=command.replace("the","")
    command=command.replace("a","")
    command=command.replace("give","")
    command=command.replace("tell","")
    command=command.replace("of","")
    command=command.replace("for","")
    command=command.replace("on","")
    command=command.replace("wikipedia","")
    command=command.replace("search","")
    command=command.replace("extract","")
    return command

def Reader():
    speak("Tell me the name of Book!")
    name=obj.mic_input()
    if ("example" in name) or ("Example" in name):
        os.startfile("example.pdf")
        book=open("example.pdf",'rb')
        pdfreader=PyPDF2.PdfFileReader(book)
        pages=pdfreader.getNumPages()
        speak(f"Number of pages in this book are {pages}")
        speak("From which page should I start reading?")
        numPage =int(input("Enter the Page number:"))
        page=pdfreader.getPage(numPage)
        text=page.extractText()
        speak(text)
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    c_time = obj.tell_time()
    speak(f"Currently it is {c_time}")
    speak("I am Jarvis. Online and ready sir. Please tell me how may I help you")
# if __name__ == "__main__":


class MainThread(QThread): #app starts with this
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        startup()
        # wish()
        print(len(voices))
        while True:
            command = obj.mic_input()
            command=command.replace("jarvis","")
            if re.search('date', command):
                date = obj.tell_me_date()
                print(date)
                speak(date)

            elif "time" in command:
                time_c = obj.tell_time()
                print(time_c)
                speak(f"Sir the time is {time_c}")

            elif command in GREETINGS:
                speak("Hello Sir! How may I help you?")


            elif "buzzing" in command or "news" in command or "headlines" in command or "headline" in command :
                news_res = obj.news()
                speak('Source: BBC News')
                speak('Todays Headlines are..')
                for i in news_res:
                    speak(i)
                speak('These were the top headlines, Have a nice day Sir!!..')
            elif "information" in command or "wikipedia" in command:
                command=command.replace("search ","")
                command=command.replace("wikipedia ","")
                command=command.replace("on ","")
                command=command.replace("extract ","")
                command=command.replace("give ","")
                command=command.replace("about ","")
            
                speak("Searching "+command+ " on Wikipedia....") #mobile
                wiki=wikipedia.summary(command,2) #2 is number of words in sentence
                print(wiki)
                speak(f"According to wikipedia:{wiki}")
                continue
            
            elif "play music" in command or "hit some music" in command:
                command=command.replace("play","")
                command=command.replace("music","")
                command=command.replace("some","")
                speak("Playing music"+command)
                pywhatkit.playonyt(command)

            elif 'youtube' in command:
                command=command.replace("play ","")
                command=command.replace("music ","")
                speak(f"Okay sir, opening {command} on youtube")
                pywhatkit.playonyt(command)
            elif "repeat my words" in command:
                speak("Speak Sir!")
                jj=obj.mic_input()
                speak(f"You said :{jj}")


            if "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "system" in command:
                sys_info = obj.system_info()
                print(sys_info)
                speak(sys_info)

            elif "where is" in command:
                place = command.split('where is ', 1)[1]
                current_loc, target_loc, distance = obj.location(place)
                city = target_loc.get('city', '')
                state = target_loc.get('state', '')
                country = target_loc.get('country', '')
                # datetime.time.sleep(1)
                try:

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(res)
                        speak(res)

                except:
                    res = "Sorry sir, I couldn't get the co-ordinates of the location you requested. Please try again"
                    speak(res)

            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")

            elif "switch the window" in command or "switch window" in command:
                speak("Okay sir, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                # timesleep.(1)
                pyautogui.keyUp("alt")

            elif "where i am" in command or "current location" in command or "where am i" in command:
                curloc=getcurrentlocation()
                speak(f"Your current location is {curloc}")

            elif "take screenshot" in command or "screenshot" in command or "take a screenshot" in command or "capture the screen" in command:
                speak("By what name do you want to save the screenshot?")
                name = obj.mic_input()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")

            elif "remember that" in command or "make a note" in command:
                rememberMsg= command.replace("remember that","")
                rememberMsg= command.replace("jarvis","")
                speak(f"You Told Me remind that:{rememberMsg}")
                remember=open('data.txt','w')
                remember.write(rememberMsg)
                remember.close()

            elif ("translate" in command) or ("translator" in command):
                Tran()

            elif "alarm" in command:
                speak("Enter the time!")
                time=input(": Enter the time :")
                while True:
                    Time_Ac =datetime.datetime.now()
                    now=Time_Ac.strftime("%H:%M:%S")
                    if now==time:
                        speak("Time to wake up sir!")
                        speak("Alarm Closed!")
                    elif now>time:
                        break 

            elif "what do you remember" in command:
                remember=open('data.txt','r')
                speak(f"You Told Me remind that:{remember.read()}")

            elif "speed test" in command:
                SpeedTest()

            elif "temperature" in command or "weather" in command:
                url=f"https://www.google.com/search?q={command}"
                r=requests.get(url)
                data=BeautifulSoup(r.text,"html.parser")
                temperature=data.find("div",class_="BNeawe").text
                speak(f"The temperature outside is {temperature}")

            elif "read book" in command:
                Reader()

            elif ("website" in command) or ("launch" in command) or ("open" in command):
                speak("Ok Sir, Launching....")
                command=command.replace("launch","")
                command=command.replace("jarvis","")
                command=command.replace("website","")
                command=command.replace("open","")
                web1=""
                print(command)
                for url in search(command,stop=1):
                    web1=url
                print(web1)
                webbrowser.open(web1)
                speak("Launched!")

            elif "goodbye" in command or "offline" in command or "bye" in command or "break" in command:
                speak("Alright sir, going offline. It was nice working with you")
                sys.exit()

            elif "how to" in command or "steps" in command:
                op=command.replace("jarvis","")
                max_result=1
                how_to_func=search_wikihow(op,max_result)
                assert len(how_to_func)==1
                speak(how_to_func[0].summary)
            elif 'google' in command or "search" in command:
                command=command.replace("search","")
                command=command.replace("google","")
                command=command.replace("for","")
                obj.search_anything_google(command)

            else:
                continue

startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    # def run(self):
    #     self.TaskExection
    def startTask(self):
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Jarvis/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv) #ui will be generated
jarvis = Main() #object for ui is called
jarvis.show()
exit(app.exec_()) #stop execution of app