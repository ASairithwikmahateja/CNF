from threading import Thread
import socket


def main2(server):
    data = b''
    while True:
        try:
            data = server.recv(1024)
        except:
            break
        if data:
            print('server response: '+str(data.decode()))
        else:
            break
    

host = '127.0.0.1'
port  = 5000
s = socket.socket()
s.connect((host, port))

def main():
    message = input('-->')
    while message != 'x':
        s.send(message.encode())
        message = input()
    s.close()

if __name__ == '__main__':
    t= Thread(target=main)
    t2=Thread(target=main2,args=(s,))
    t.start()
    t2.start()
    t.join()
    t2.join()