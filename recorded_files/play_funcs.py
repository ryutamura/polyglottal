from pydub import AudioSegment
from pydub.playback import play

def play_audio1():
    audio_snippit = AudioSegment.from_wav('output1.wav')
    higher_volume = audio_snippit + 10
    play(higher_volume)

def play_audio2():
    audio_snippit = AudioSegment.from_wav('output2.wav')
    higher_volume = audio_snippit + 10
    play(higher_volume)   

def play_audio3():
    audio_snippit = AudioSegment.from_wav('output3.wav')
    higher_volume = audio_snippit + 10
    play(higher_volume)

def play_audio4():
    audio_snippit = AudioSegment.from_wav('output4.wav')
    higher_volume = audio_snippit + 10
    play(higher_volume)

def play_audio5():
    audio_snippit = AudioSegment.from_wav('output5.wav')
    higher_volume = audio_snippit + 10
    play(higher_volume)