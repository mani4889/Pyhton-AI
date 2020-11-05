import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")

    speak("I am jarvis boss!.Please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and give string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print (e)

        print("Repeat it again Boss!")
        return "none"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing task based on query
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open amazon" in query:
            webbrowser.open("amazon.com")

        elif "play music" in query:
            music_dir="D:\\music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[6]))

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{strTime}")

        elif "open photos" in query:
            photopath="D:\\images\\rameswaram\\DSCN4199"
            os.startfile(photopath)
