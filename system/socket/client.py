# -*- utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8080))

s.sendall(b"Hello from the client!")
recv_data = s.recv(1024).decode('utf-8')
print(f"Received data: {recv_data}")
s.close()