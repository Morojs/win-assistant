import tempfile
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

class AudioSegmentProcess() :
    def __init__(self,text) :
        self.text=text
        self.tempWavFile = tempfile.TemporaryFile(suffix="wav")
        self.tts=gTTS(text,lang='en')
        self.write_to_bytes()
        self.song=self.audio_converter()
    
    def write_to_bytes(self) : 
        self.tts.write_to_fp(self.tempWavFile)
        self.tempWavFile.seek(0)

    def audio_converter(self,cvAudio='') : 
        AudioSegment.converter=r"D:\\workspace\\current-workspace\\github\\ffmpeg-4.3.2-2021-02-20-full_build\\ffmpeg-4.3.2-2021-02-20-full_build\\bin\\ffmpeg.exe"
        song = AudioSegment.from_file_using_temporary_files(self.tempWavFile)
        return song
    
    def play(self) :
        play(self.song)