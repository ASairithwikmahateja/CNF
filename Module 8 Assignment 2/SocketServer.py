'''UDP socket server'''
import socket

'''Address and port of the server'''
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080       # Port to listen on (non-privileged ports are > 1023)

'''currency exchange rates'''
currency = {'Dollar_INR':{1:67},
            'INR_Dollar':{1:0.0149},
            'Dollar_Pounds':{1:0.75},
            'Pounds_Dollar':{1:1.3333},
            'Dollar_Yen':{1:113.41},
            'Yen_Dollar':{1:0.0088}
            }

'''responds to a clinet request and closes automatically after responding'''
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    data, addr = s.recvfrom(1024)
    result = 0

    data = data.decode()
    data = data.replace('From',"").replace(' To '," ").strip()
    data = data.split(" ")
    
    result += int(data[1]) * currency[data[0]+"_"+data[2]][1]
    
    result = str(round(result)).encode()
    
    s.sendto(result,addr)
