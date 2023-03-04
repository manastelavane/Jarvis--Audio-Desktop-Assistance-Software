import pyttsx3
import speech_recognition as sr
from pywikihow import search_wikihow
from playsound import playsound
import smtplib  # smtp means Simple Mail Transfer Protocol
from tkinter import *
from tkinter.messagebox import *

# sapi5 is microsoft's speech recognition IDE
Assistant = pyttsx3.init('sapi5')

# create an instance variable named as voices to get different voices
voices = Assistant.getProperty('voices')
print(voices)

# id 0 is for male and 1 is for female voice
Assistant.setProperty('voices', voices[1].id)
# rate of speed of speaking is 200 by default
Assistant.setProperty('rate', 180)

# path for google chrome.
path = "C://Program Files//Google//Chrome//Application//chrome.exe %s"
# I have used this path to open every thing
# in chrome rather than opening in edge by default


def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f":{audio}")
    # print("    ")
    Assistant.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone(1) as source:  # use Microphone(1) if you have
        print("Listening...")
        command.adjust_for_ambient_noise(source)
        # command.pause_threshold=1
        command.energy_threshold = 250
        audio = command.listen(source)
        x = True
        while x == True:
            try:
                print("Recognizing...")
                query = command.recognize_google(
                    audio, language='en-in').lower()
                print(f"You said: {query}\n")
                Speak(f"You said: {query}\n")
                x = False
            except Exception as error:
                print("Say that again please...")
                return "None"
            return query.lower()


people = {
    "anushka": "anushkasunilbhilare@ternaengg.ac.in",
    "manas": "manastelavane@ternaengg.ac.in",
    "vritti": "vruttishringarpure@ternaengg.ac.in"
}

f = ("Ariel", 20, "bold")


def email(person, subject, text):
    # with open("people.csv") as quotes_file:
    #     all_quotes = quotes_file.readlines()
    #     print(all_quotes)

    my_email = "vrutti.shringarpure.development@gmail.com"  # put sender email here
    my_password = "oasooxizrdkkllsq"
    SUBJECT = subject
    TEXT = text
    mymsg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    # establishing connection with gmail's smtp server, we use this syntax so that we don't have to write connection.close() statement
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # TLS means transport layer security...this is a way of securing our connection with the email server...this basically encrypts our email
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=people[person],
                            msg=mymsg,
                            )


def actual_email(person):
    x = True
    while x == True:
        Speak("what should be the subject?")
        subj = takecommand()
        print(subj)
        while True:
            Speak("what will be the body of the mail?")
            text = takecommand()
            print(text)
            email(person, subj, text)
            Speak("Email sent.")
            x = False
            break


def send_email():
    flag=True
    while True:
            Speak("whom should i send the email?")
            person = takecommand()
            print(person)

            for d in people:
                if d == person:
                    actual_email(person)
                    flag=False
                    break
            if flag==True:
                Speak("Email does not exist in your email list.")
                print("Email does not exist in your email list.")

            if flag==False:
                break

# def TaskExe():
#     y = True

#     while y == True:
#         query = takecommand()

#         if "email" in query:


def Automated_Email_Sending():
    while True:
        Speak("Do you want to send email to someone from your contact list?")
        query = takecommand()

        if query == "yes":
            while True:
                Speak(
                    "do you want me to read out names of your contact list?")
                want_names = takecommand()

                if want_names == "yes":
                    Speak("Your list includes")
                    for d in people:
                        print(d)
                        Speak(d)
                    send_email()
                    break

                elif want_names == "no":
                    send_email()
                    break                        

        elif query == "no":
            Speak(
                "please enter name and email id of the person you want to send email to")

            class GetEntry():
                def __init__(self, master):
                    self.master = master
                    self.entry_name_contents = None
                    self.entry_email_contents = None
                    self.enlbl=Label(master,text="Enter name of the person: ",font=("Ariel",15,"bold"))
                    self.en = Entry(master,font=("Ariel",15,"bold"),bd=2)
                    self.eelbl=Label(master,text="Enter Email of the person: ",font=("Ariel",15,"bold"))
                    self.ee = Entry(master,font=("Ariel",15,"bold"),bd=2)
                    self.enlbl.grid(row=0, column=0)
                    self.en.grid(row=0, column=1)
                    self.en.focus_set()
                    self.eelbl.grid(row=1, column=0)
                    self.ee.grid(row=1, column=1)
                    self.ee.focus_set()

                    Button(master, text="get", width=10, bg="yellow",
                            command=self.callback).grid(row=10, column=0)

                def callback(self):
                    """ get the contents of the Entry and exit
                    """
                    self.entry_name_contents = self.en.get()
                    self.entry_email_contents = self.ee.get()
                    self.master.quit()

            master = Tk()
            master.geometry("500x500+100+100")
            master.title("Enter new contact")
            GE = GetEntry(master)
            master.mainloop()

            while True:
                person = GE.entry_name_contents
                people[person] = GE.entry_email_contents
                print(people)
                actual_email(person)
                break
        break

    else:
        Speak("I don't know what to do on this instruction")