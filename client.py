import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.45.5',55555))
message = s.recv(1024)
print(message.decode())