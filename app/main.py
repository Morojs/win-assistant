import threading, os, sys

PACKAGE_PARENT = ".."
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
# Recognizer class
import speech_recognition as sr
from playsound import playsound
from api.recognizer import Recognizer
from helpers.audio_segment import AudioSegmentProcess
import parse.lark_parser as parser


def start():

    while True:
        # create recognizer and mic instances
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        api_response = Recognizer(recognizer, microphone).recognize_speech_from_mic()
        format_response = format(api_response["transcription"])
        # show the user the transcription
        if format_response != "None":
            response = parser.main(format_response)
            # print the result
            print("You said:" + format_response + " response " + str(response))
            # play what you said
            AudioSegmentProcess("You said: " + format_response).play()
        else:
            AudioSegmentProcess("Sorry I couldn't understand ...!").play()


def start():
    # set the list of windows commands
    CMDS = ["CREATE", "OPEN", "DELETE", "MAKE", "READ"]
    # format the instructions string
    instructions = ("I'm thinking ...:\n" "{cmds}\n").format(cmds=", ".join(CMDS))
    # show instructions
    print(instructions)
    trd = threading.Thread(target=start)
    trd.start()


if __name__ == "__main__":
    start()