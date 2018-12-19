'''TCP socket server'''
import socket

'''socket port and host'''
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8080       # Port to listen on (non-privileged ports are > 1023)


'''currency conversions data'''
currency = {'Dollar_INR':{1:67},
            'INR_Dollar':{1:0.0149},
            'Dollar_Pounds':{1:0.75},
            'Pounds_Dollar':{1:1.3333},
            'Dollar_Yen':{1:113.41},
            'Yen_Dollar':{1:0.0088}
            }


'''Waits for client request and closes the socket automatically'''
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            result = 0
            if not data:
                break 
            else:
                data = data.decode()
                data = data.split(" ")
                
                result += int(data[2]) * currency[data[1]+"_"+data[4]][1]
                
                result = str(round(result)).encode()
                
            conn.sendall(result)
