import socket		
import threading	 
import random
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)		 
print ("Socket successfully created")
port = 12345				
s.bind(('', port))		 
print ("Socket binded to %s" %(port) )
s.listen(5)	 
print ("Socket is listening")
connections = []	

def broadcast(pos,con): #function broadcasting the movements to everyone else in the network
    for conn in connections:
        if conn!=con:
                conn.send(pos)

def client(c,addr):
    print("Got connection from ", addr)
    connections.append(c)
    while True:
        data = c.recv(1024)
        broadcast(data,c) 
        time.sleep(0.5)

while True:
    c, addr = s.accept()
    thread1 = threading.Thread(target = client, args = (c, addr))
    thread1.start()

s.close()