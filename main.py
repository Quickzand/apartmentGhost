import speech_recognition as sr
import time
import json
from playsound import playsound


# Get wordlist from file
with open('wordlist.json', 'r') as f:
    wordList = json.load(f)






def callback(recognizer, audio):
    print("attempting to understand what you said..")
    # recognize speech using Google Speech Recognition
    WIT_AI_KEY = "4B3WB275TC2JTCSEWJPDZQZP6QWVK4CB"  # Wit.ai keys are 32-character uppercase alphanumeric strings
    try:
        audioText = recognizer.recognize_sphinx(audio);
        print("Wit.ai thinks you said " + audioText)
        # For every value in wordlist check if it is in the recognized text
        audioText = audioText.lower()
        for value in wordList:
            if(value["word"] in audioText):
                # Play the mp3 file
                print("Playing " + value["sound"])
                playsound(value["sound"])
                break
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))



r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some unrelated computations for 5 seconds
for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

# calling this function requests that the background listener stop listening
# stop_listening(wait_for_stop=False)

# do some more unrelated things
while True: time.sleep(0.1)  # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping
