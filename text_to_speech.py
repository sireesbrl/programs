import pyttsx3

engine = pyttsx3.init()
#voices = engine.getProperty('voices')
engine.setProperty("voice","american")
engine.say("welcome sir. please wait while i initialize the program")
engine.runAndWait()

while True:
    usr_input = (input("Write something: ")).lower()
    if usr_input == "exit":
        engine.say("exiting in 3...2...1")
        engine.runAndWait()
        break
    engine.say(usr_input)
    engine.runAndWait()


