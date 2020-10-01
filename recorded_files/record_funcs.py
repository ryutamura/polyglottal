import pyaudio
import wave

def record1():
    print('#' * 80)
    print("Speak into the mic")
    print('Press Ctrl+C to stop recording')

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
                    
    print("Start recording")
    
    frames = []
    
    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Done recording")
    except Exception as e:
        print(str(e))
        
    sample_width = p.get_sample_size(FORMAT)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open('./output1.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
	
    print("Result written to output1.wav")
    print('#' * 80)
	
def record2():
    print('#' * 80)
    print("Speak into the mic")
    print('Press Ctrl+C to stop recording')

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
                    
    print("Start recording")
    
    frames = []
    
    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Done recording")
    except Exception as e:
        print(str(e))
        
    sample_width = p.get_sample_size(FORMAT)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open('output2.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
	
    print("Result written to output2.wav")
    print('#' * 80)

def record3():
    print('#' * 80)
    print("Speak into the mic")
    print('Press Ctrl+C to stop recording')

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
                    
    print("Start recording")
    
    frames = []
    
    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Done recording")
    except Exception as e:
        print(str(e))
        
    sample_width = p.get_sample_size(FORMAT)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open('output3.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
	
    print("Result written to output3.wav")
    print('#' * 80)

def record4():
    print('#' * 80)
    print("Speak into the mic")
    print('Press Ctrl+C to stop recording')

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
                    
    print("Start recording")
    
    frames = []
    
    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Done recording")
    except Exception as e:
        print(str(e))
        
    sample_width = p.get_sample_size(FORMAT)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open('output4.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
	
    print("Result written to output4.wav")
    print('#' * 80)

def record5():
    print('#' * 80)
    print("Speak into the mic")
    print('Press Ctrl+C to stop recording')

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)
                    
    print("Start recording")
    
    frames = []
    
    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
    except KeyboardInterrupt:
        print("Done recording")
    except Exception as e:
        print(str(e))
        
    sample_width = p.get_sample_size(FORMAT)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    wf = wave.open('output5.wav', 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
	
    print("Result written to output5.wav")
    print('#' * 80)