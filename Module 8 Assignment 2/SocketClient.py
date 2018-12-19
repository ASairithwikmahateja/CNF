'''UDP client Socket'''
import socket

'''ip and port of server'''
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 8080       # The port used by the server

'''Requests the server for the data and closes automatically after the result'''
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'From Dollar 10 To INR')
    data = s.recv(1024)
    print(data.decode())