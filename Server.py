import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1236

s.bind((host, port))
s.listen(5)

while True:
    clientsocket, adress = s.accept()
    print(f"Connection from {adress} has been established")
    clientsocket.send(b'Welcome to the server!')
    clientsocket.close()
