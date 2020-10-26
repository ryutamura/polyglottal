from pydub import AudioSegment
from pydub.playback import play

def play_preset1():
    audio_snippit = AudioSegment.from_mp3('./Nuthin-But-A-G-Thang.mp3')
    lower_volume = audio_snippit - 10
    play(lower_volume)

def play_preset2():
    audio_snippit = AudioSegment.from_mp3('fo_shizzle.mp3')
    lower_volume = audio_snippit + 10
    play(lower_volume)

def play_preset3():
    audio_snippit = AudioSegment.from_mp3('weed.mp3')
    lower_volume = audio_snippit + 10
    play(lower_volume)

def play_preset4():
    audio_snippit = AudioSegment.from_mp3('oh_yea.mp3')
    lower_volume = audio_snippit + 10
    play(lower_volume)

def play_preset5():
    audio_snippit = AudioSegment.from_mp3('airhorn.mp3')
    higher_volume = audio_snippit + 10
    play(higher_volume)
