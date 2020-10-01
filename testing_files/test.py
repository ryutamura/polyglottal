import pyaudio

a = pyaudio.PyAudio()

hostAPICount = a.get_host_api_count()
print("Host API Count = " + str(hostAPICount))

for cnt in range(hostAPICount):
    print(a.get_host_api_info_by_index(cnt))

    