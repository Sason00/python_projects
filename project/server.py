import socket
import pyaudio

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

chunk = 1024      # Each chunk will consist of 1024 samples
sample_format = pyaudio.paInt16      # 16 bits per sample
channels = 1      # Number of audio channels
fs = 44100        # Record at 44100 samples per second
time_in_seconds = 1

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def list_devices():
    p2 = pyaudio.PyAudio()
    device_count = p2.get_device_count()
    for i in range(0, device_count):
        info = p2.get_device_info_by_index(i)
        print("Device {} = {}".format(info["index"], info["name"]))
    print(p2.get_default_output_device_info())
        
list_devices()

p = pyaudio.PyAudio()  # Create an interface to PortAudio
stream = p.open(channels = 2,
                format=sample_format,
                rate = fs // 2, # somehow when it's normal it 2 times faster
                frames_per_buffer = chunk,
                output=True,
                input=False,
                output_device_index=3)




while True:
    data, addr = sock.recvfrom(1024*10) # buffer size is 1024 bytes
    print(data)
    input()
    stream.write(data)
    