from pydub import AudioSegment
from pydub.playback import play

def play_preset1():
    audio_snippit = AudioSegment.from_mp3('./Nuthin-But-A-G-Thang.mp3')
    lower_volume = audio_snippit - 10
    play(lower_volume)

def play_preset2():
    audio_snippit = AudioSegment.from_mp3('./Nas-Is-Like.mp3')
    lower_volume = audio_snippit - 10
    play(lower_volume)

def play_preset3():
    audio_snippit = AudioSegment.from_mp3('Nas-NY-State-Of-Mind.mp3')
    lower_volume = audio_snippit - 10
    play(lower_volume)

def play_preset4():
    audio_snippit = AudioSegment.from_mp3('The-6th-Sense.mp3')
    lower_volume = audio_snippit - 10
    play(lower_volume)
