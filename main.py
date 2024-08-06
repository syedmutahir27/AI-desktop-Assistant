import speech_recognition as sr
import os
import win32com.client
import webbrowser
import openai
import datetime
speaker = win32com.client.Dispatch("SAPI.SpVoice")




def say(text):

    s = text
    speaker.Speak(s)

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio,language= "en-in")
            print(f"USer said : {query}")
            return query
        except Exception as e:
            return"Some error Occured Sorry from jarvis "

if __name__ == '__main__':
    print("hi")
    say("hello i am jarvis ai")
    while True:
        print("Listening..")
        query = take_command()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],
        ["google","https://www.google.com"],]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = "C:\\Users\syedm\Music\\Nostalgia.mp3"
            os.system(musicPath)

        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"The time is {strfTime}")

