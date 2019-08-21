import socket

def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('8.8.8.8', 80))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0' #socket.gethostname()
port = 1234

s.bind((host, port))
s.listen(5)

print(f'Running Server in {getLocalIP()}:{port}')

while True:
    clientsocket, adress = s.accept()
    print(f'Connection from {adress} has been established')
    clientsocket.send(b'Welcome to the server!')
    clientsocket.close()
