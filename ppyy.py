import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!! Sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!! ")

    else:
        speak("Good Evening!")

    speak("Hello  I am Friday your very own virtual assistant ")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as es:
        # print(es)
        print("Say that again please...")
        return "None"
    return query


def talk(text):
    engine.say(text)
    engine.runAndWait()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'who is ' in query:
            speak('Searching in Wikipedia wait for a moment Sir...')
            query = query.replace("who is ", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            talk('I am fine ,thank you')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play' in query:
            song = query.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open nit ' in query:
            webbrowser.open("manit.ac.in")

        elif 'open project' in query:
            project_path= "E:\\python_project"
            os.startfile(project_path)

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('f"Sir,Current time is ' + time)

        elif 'open code' in query:
            path = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'team members' in query:
            talk('We have 4 members in this group they are ,, 1st Shreyansh, 2nd Nitin,  3rd Vikas, 4th Utkarsh')

        elif 'thank you' in query:
            talk('anytime')

        elif 'stop' in query:
            talk('Ok sir, good- bye')
            exit(0)

            # how are you
            # team members
            # what is the current time
            # who is narendra modi
            # play vande matram in youtube
            # open nit bhopal site
            # thank you


