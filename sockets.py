import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.45.4',55555))
s.listen()

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    client.send("예우니까 연결했넹".encode())
    client.close()