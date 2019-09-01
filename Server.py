from AudioRecord import stream, closeStream, chunk
import socket
import signal
import sys
import time

def sigint_handler(signal, frame):
    try:
        closeStream()
    except:
        print('Unable to close Audio Stream')
        pass

    clientsocket.close()

    print('\nConnection closed')
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler) #Catch SIGINT


def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0' #Run on local network
port = 1240

s.bind((host, port))
s.listen(5)

print(f'Running Server in {getLocalIP()}:{port}')
print('Waiting for connection...')

clientsocket, adress = s.accept()
print(f'Connection from {adress} has been established')

stream.start_stream()
time.sleep(0.1)

while True:
    try:
        clientsocket.send(stream.read(chunk))
    except:
        closeStream()
        print('\nConnection closed by Client')
        break
