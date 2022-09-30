import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your virtual assistant. Tell me how may I help you ")

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = sr.listen(source)
            query = sr.recognize_google(voice)
            query = query.lower()
            if 'alexa' in query:
                command = query.replace('alexa', '')
                print(query)
    except:
        pass
    return query

# def takeCommand():
#     #It takes microphone input from the user and returns string output
#
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
#
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query}\n")
#
#     except Exception as e:
#         # print(e)
#         print("Say that again please...")
#         return "None"
#     return query

def talk(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search' in query:
            speak('Searching in Wikipedia wait for a moment "Sir...')
            query = query.replace("search", "")


            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

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

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('f"Sir,Current time is ' + time)

        elif 'team members' in query:
            talk('We have 4 members in our group they are ,, 1st Shreyansh, 2nd Nitin,  3rd Vikas, 4th Utkarsh')

        elif 'stop'in query:
            exit(0)