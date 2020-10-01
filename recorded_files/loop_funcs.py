from pydub import AudioSegment
from pydub.playback import play

def loop1():
    audio_snippit = AudioSegment.from_wav('output1.wav')
    higher_vol = audio_snippit + 10
    loop7 = higher_vol * 7
    play(loop7)

def loop2():
    audio_snippit = AudioSegment.from_wav('output2.wav')
    higher_vol = audio_snippit + 10
    loop7 = higher_vol * 7
    play(loop7)

def loop3():
    audio_snippit = AudioSegment.from_wav('output3.wav')
    higher_vol = audio_snippit + 10
    loop7 = higher_vol * 7
    play(loop7)

def loop4():
    audio_snippit = AudioSegment.from_wav('output4.wav')
    higher_vol = audio_snippit + 10
    loop7 = higher_vol * 7
    play(loop7)

def loop5():
    audio_snippit = AudioSegment.from_wav('output5.wav')
    higher_vol = audio_snippit + 10
    loop7 = higher_vol * 7
    play(loop7)