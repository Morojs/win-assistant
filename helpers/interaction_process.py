from helpers.audio_segment import AudioSegmentProcess
class Interact() : 
    # TEST
    def __init__(self,input) :
        self.intext=input

    def request_process(self) :
        AudioSegmentProcess("doing well thank you").play()
        return True