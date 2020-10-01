import subprocess

print("Start recording...")
p = subprocess.Popen(("rec", "-q", "out2.mp3"))

input("Enter to stop: ")
p.terminate()
try:
    p.wait(timeout=1)
except subprocess.TimeoutExpired:
    p.kill()