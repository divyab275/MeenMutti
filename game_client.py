import socket			 
import random
import time
import threading
s = socket.socket()		 
port = 12345				
s.connect(('127.0.0.1', port))

gamers = {} # Dictionary that contains as key the addr of client connection and value (x,y) coordinates

def serve(s):
    while True:
        data = s.recv(1024)
        details = data.split('/')
        coordinates = (details[1],details[2])
        gamers[details[0]] = coordinates

thread1 = threading.Thread(target = serve, args = (s,))
thread1.start()

while True:
    x,y = random.randint(1,101),random.randint(1,101)
    st = str(x)+'/'+str(y)
    s.send(st)
    time.sleep(5)
    print(gamers)
    #print(x,y)
s.close()