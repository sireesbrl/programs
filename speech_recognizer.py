import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


while True:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration = 0.2)
            audio2 = r.listen(source2)
            text = r.recognize_google(audio2)
            text = text.lower()
            speak(text)

    except sr.RequestError as e:
        print("Couldn't request results: {0}".format(e))
        
    except sr.UnknownValueError:
        print("Unknown error occured")
