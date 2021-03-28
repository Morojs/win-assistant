from helpers.audio_segment import AudioSegmentProcess
from api.wolframAlpha import alpha


class Interact:
    # TEST
    def __init__(self, input):
        self.intext = input
        print(input)

    def request_process(self):
        AudioSegmentProcess(alpha.get_answer(self.intext)).play()
        return True
