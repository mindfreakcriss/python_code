# -*- utf-8 -*-

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
s.listen(5)

print("Server is listening on port 8080...")

conn, addr = s.accept()
print(f"Connection from {addr} has been established!")

recv_data = conn.recv(1024).decode('utf-8')
print(f"Received data: {recv_data}")

s.close()