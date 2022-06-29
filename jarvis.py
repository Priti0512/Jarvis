from datetime import datetime
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17 :
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello mam I am jarvis, How can I help you !")

def takeCommand():
    # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please.....")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("'smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('pritikumariiit@gmail.com','99999999999')
    server.sendmail('pritikumariit@gmail.com',to ,content)
    server.close()

if __name__ == "__main__":
    #speak("Priti is good girl")
    wishMe()
    while True:
       query = takeCommand().lower()
    #logic for executing tasks based on query
       if 'wikipedia' in query:
           speak('Searching wikipedia......')
           query= query.replace('wikipedia', "")
           results = wikipedia.summary(query,sentences = 2)
           speak("According to wikipedia ")
           print(results)
           speak(results)
        
       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       elif 'open google' in query:
           webbrowser.open("google.com")
       elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")
       elif 'play music' in query:
           music_dir = 'C:\\Users\\91809\\New folder'
           songs = os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[5]))
       elif 'the time' in query:
           strTime = datetime.now().strftime("%H:%M:%S") 
           speak(f"Mam, the time is {strTime}")
       elif 'open code' in query:
           codePath = "C:\\Users\\91809\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
       elif 'email to priti' in query:
           try:
               speak("What should i say")
               content = takeCommand()
               to = "pritikumariiit@gmail.com"
               sendEmail(to,content)
               speak("Email has been sent")
           except Exception as e:
               print(e)
               speak("Sorry ! Adress not Found")
       elif 'quit' in query or 'bye' in query:
           speak("Quitting mam, thanks for using jarvis ")
           exit() 


