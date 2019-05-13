import socket			 
import random
import time
s = socket.socket()		 
port = 12345				
s.connect(('127.0.0.1', port))
while True:
    x,y = random.randint(1,101),random.randint(1,101)
    st = str(x)+'.'+str(y)
    s.send(st)
    time.sleep(2)
    print(x,y)
s.close()