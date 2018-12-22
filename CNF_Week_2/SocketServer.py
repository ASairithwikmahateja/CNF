# importing socket module
import socket
#  importing threading module
import threading
#  importing csv module
import csv

s = socket.socket()

ipaddress = '192.168.56.1'
portno = 8080

s.bind((ipaddress, portno))

s.listen()

file = open("data.csv", "r")
reader = csv.reader(file)

def Rec(client):
    while True:
        msg  = client.recv(1024).decode()
        if msg == '':
            continue
        reply = msg.split(" ")
        print(reply)
        user = reply[1].strip()
        Ques = ''
        Answ = ''
        if reply[0] == 'MARK-ATTENDANCE':
            reply = ''
            for line in reader:
                if line[0].strip() == user:
                    Ques = line[1]
                    Answ = line[2]
                    Text = 'SECRETQUESTION-' + line[1]

            if Text == '':
                client.send('ROLLNUMBER-NOTFOUND'.encode())
            else:
                client.send(Text.encode())
                Answer = client.recv(1024).decode().split(" ")

                if Answer[0] == 'SECRETANSWER':
                    Result = True
                    while True:
                        if Answer[1] == str(Answ):
                            Result = False
                            client.send('ATTENDANCE-SUCCESS'.encode())
                        else:
                            client.send('ATTENDANCE FAILURE'.encode())
                            client.send(Ques.encode())
                            Answer = client.recv(1024).decode().split(" ")


while True:
    client, addr = s.accept()
    threading.Thread(target = Rec, args  = (client,)).start()
