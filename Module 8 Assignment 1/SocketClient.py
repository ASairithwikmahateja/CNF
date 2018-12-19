'''tcp client socket '''
import socket


'''Host and port to connect'''
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080       # The port used by the server


'''client making request and closes automatically after the responce arrived'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'From Dollar 10 To INR')
    data = s.recv(1024)

print(data.decode())