import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak (text):
    engine.say(text)
    engine.runAndwait()
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout = 2)
        print("recognizing...")
            #Listen for the wake word jarvis.
        try:
            command  = r.recognize_google_cloud(audio)
            print(command)
        except Exception as e:
            print("Sphinx could not understand audio.")


