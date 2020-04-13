import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
  
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon")
    
    else:
        speak("Good Evening!")
        print("Good Evening")

    speak("Welcome to voice assistant!Tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query  

if __name__ == "__main__":  
    wishMe()
    if 1:
        query  = takeCommand().lower()
        
        if 'the time' in query:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
            print(strTime)
        
        elif 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("Wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)
             
        elif 'open youtube' in query:
             webbrowser.open("https://www.youtube.com/")
        
        elif 'open google' in query:
             webbrowser.open("https://www.google.com/")

        elif 'open stackoverflow' in query:
             webbrowser.open("https://stackoverflow.com/")
        
        elif 'play music' in query:
             webbrowser.open("https://www.youtube.com/watch?v=SlPhMPnQ58k")
             
        



    