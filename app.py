from Models.recognizer import Recognizer
import speech_recognition as sr
from playsound import playsound
import logging
import threading
import time

def start() :
    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    while True : 
        # print the result 
        guess = Recognizer(recognizer, microphone).recognize_speech_from_mic()
        # show the user the transcription
        if (format(guess["transcription"])!="None") : 
            print("You said: {}".format(guess["transcription"]))
            playsound('sounds/end.wav') 
        else : 
            print("Sorry I couldn't understand ...!")

if __name__ == "__main__" :
    # set the list of windows commands, maxnumber of guesses, and prompt limit
    CMDS = ["A", "B", "C"]
    # format the instructions string
    instructions = (
        "I'm thinking ...:\n"
        "{cmds}\n"
    ).format(cmds=', '.join(CMDS))
    # show instructions and wait 3 seconds before starting the game
    print(instructions)   
    trd=threading.Thread(target=start)
    trd.start()
    trd.join()
