import socket
import threading
import sys

def Rec(s):
    while True:
        data = s.recv(1024).decode()
        if not data:
            continue
        if data == 'ATTENDANCE-SUCCESS':
            print(data)
            sys.exit()
        else:
            print(data)
            

def main():

    hostaddress = '192.168.56.1'
    portno = 8080
    s = socket.socket()

    s.connect((hostaddress, portno))
    
    print('Server connected')

    s.send(input().encode())
    threading.Thread(target = Rec, args  = (s,)).start()
    while True:
        s.send(input().encode())

if __name__ == "__main__":
    main()