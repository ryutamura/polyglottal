import urllib.request
from pydub import AudioSegment
from pydub.playback import play
# Download an audio file
# urllib.request.urlretrieve("https://tinyurl.com/wx9amev", "metallic-drums.wav")
# Load into PyDub
# loop = AudioSegment.from_wav("metallic-drums.wav")
def play_audio():
    audio_snippit = AudioSegment.from_wav('./recorded_files/testout1.wav')
    loop7 = audio_snippit * 7
    play(loop7)
    
# loop2 = loop * 2
# heyloop10 = heyloop * 10
# Play the result
# play(heyloop10)
# play(loop2)
# length = len(loop2)
# Download another loop
# urllib.request.urlretrieve("https://tinyurl.com/yx3k5kw5", "beat.wav")
# Load into PyDub
# beat = AudioSegment.from_wav("beat.wav")
# Mix with our original loop
# mixed = beat.overlay(loop, loop=True)
# play(mixed)
# play_audio()
play_audio()