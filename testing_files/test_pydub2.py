import urllib.request
from pydub import AudioSegment
from pydub.playback import play
# Download an audio file
# urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")
# Load into PyDub
# loop = AudioSegment.from_wav("metallic-drums.wav")
def play_audio2():
    audio_snippit = AudioSegment.from_mp3("out2.mp3")
    play(audio_snippit)
    