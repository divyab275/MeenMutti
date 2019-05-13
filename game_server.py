import socket		
import threading	 
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
print ("Socket successfully created")
port = 12345				
s.bind(('', port))		 
print ("socket binded to %s" %(port) )
s.listen(5)	 
print ("socket is listening")
connections = []	

def broadcast(pos):
    for conn in connections:
        conn.send(pos)

def client(c,addr):
    print("Got connection from ", addr)
    conn.append(c)
    while True:
        data = c.recv(1024)
        broadcast(data)

while True:
    c, addr = s.accept()
    thread1 = threading.Thread(target = client, args = (c, addr))
    thread1.start()

s.close()