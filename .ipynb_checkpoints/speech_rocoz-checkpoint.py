import speech_recognition as sr
import pyaudio

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything...")
    audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        print("you said: {}".format(text))
    except:
        print("sorry could not recognize your voice")
