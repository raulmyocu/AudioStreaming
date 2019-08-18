import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.gethostname()
port = int(input("Server Port"))

s.connect((server, port))

msg = s.recv(1024)
print(msg.decode("utf-8"))
