import speech_recognition as sr
import logging,threading,os,sys
from playsound import playsound

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
# Recognizer class
from api.recognizer import Recognizer


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

def main() :
    # set the list of windows commands, maxnumber of guesses, and prompt limit
    CMDS = ["A", "B", "C"]
    # format the instructions string
    instructions = (
        "I'm thinking ...:\n"
        "{cmds}\n"
    ).format(cmds=', '.join(CMDS))
    # show instructions 
    print(instructions)   
    trd=threading.Thread(target=start)
    trd.start()
    trd.join()

if __name__ == "__main__" :
    main()