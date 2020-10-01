import pyaudio
import wave




def record():
    print('#' * 80)
    print("Please speak word(s) into the microphone")
    print('Press Ctrl+C to stop the recording')

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
    
    wf = wave.open('../output5.wav', 'wb')
    wf.setnchannels(CHANNELS)
    # sample_width, frames = record()
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
	
    print("Result written to output1.wav")
    print('#' * 80)
	# return sample_width, frames	
record()
# def record_to_file(file_path):
# 	wf = wave.open(file_path, 'wb')
# 	wf.setnchannels(CHANNELS)
# 	sample_width, frames = record()
# 	wf.setsampwidth(sample_width)
# 	wf.setframerate(RATE)
# 	wf.writeframes(b''.join(frames))
# 	wf.close()

# if __name__ == 'test5':
# 	print('#' * 80)
# 	print("Please speak word(s) into the microphone")
# 	print('Press Ctrl+C to stop the recording')
	
# 	record_to_file('output1.wav')
	
# 	print("Result written to output1.wav")
# 	print('#' * 80)