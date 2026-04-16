import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pyautogui
#List of pakages used.
'''
pip install pyttsx3
pip install tools
pip intall pygame
pip install gTTS
pip install pyttsx3
pip install Pyaudio
pip install SpeechRecognition
pip install pyautogui # use this to go to desktop
pip install pocketsphinx
'''

# from openai import OpenAI
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init() 


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
#I have commented this as i do not have any api key
'''def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content'''

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening google...")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening facebook...")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening youtube...")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening linkedin...")

    elif "open monkey type" in c.lower():
        webbrowser.open("https://monkeytype.com/")
        speak("Opening monkey type...")

    elif "open chat ai" in c.lower():
        webbrowser.open("https://chatgpt.com/")
        speak("Opening chat gpt...")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        speak(f"playing {song}")

    elif "go home" in c.lower():
        pyautogui.hotkey('win', 'd')
        speak("Going to desktop")

    elif "open whatsapp" in c.lower():
       webbrowser.open("https://web.whatsapp.com/")

    # else:
    # output = aiProcess(c)
    # speak(output)

    
    else:
        # Let AI handle the request
        webbrowser.open("https://chatgpt.com/")
        speak("use this to ger your answer") 





if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes...")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))