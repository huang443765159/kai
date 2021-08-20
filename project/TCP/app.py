import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
client.settimeout(0.5)
client.connect_ex((host, port))
# a = client.gettimeout()
# print(a)
client.sendall(b'hello world')
data = client.recv(1024)
print(data)
client.close()
