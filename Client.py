import AudioPlay
import socket
import signal
import sys

def sigint_handler(signal, frame):
    try:
        AudioPlay.closeStream()
    except:
        print('Unable to close Audio Stream')
        pass

    s.close()

    print('\nConnection closed')
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler) #Catch SIGINT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '0.0.0.0' #input("Server: ")
port = 1240 #int(input("Server Port: "))

s.connect((server, port))
print(f'Connected to {server} in port {port}.')

while True:
    data = s.recv(2048)

    if data:
        AudioPlay.playData(data)
    else:
        AudioPlay.closeStream()
        s.close()
        print('Connection closed by Server.')
        break
