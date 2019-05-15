import socket			 
import random
import time
import threading
import pygame, sys, time
from pygame.locals import *
pygame.init()
s = socket.socket()		 
port = 12345				
s.connect(('127.0.0.1', port))
ev=""

gamers = {} # Dictionary that contains as key the addr of client connection and value (x,y) coordinates
FPS=30
fpsClock=pygame.time.Clock()

width=700
height=450
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Animation')
background=pygame.image.load('underwater.jpg')

UP='up'
LEFT='left'
RIGHT='right'
DOWN='down'

sprite=pygame.image.load('fish.png')
spritex=200
spritey=130
direction=DOWN
def up():
    global spritex,spritey
    spritey-=5
def down():
    global spritex,spritey
    spritey+=5
def left():
    global spritex,spritey
    spritex-=5
def right():
    global spritex,spritey
    spritex+=5
def serve(s):
    global spritex,spritey
    while True:
        data = s.recv(1024)
        data=data.decode()
        print("Data="+data)   
        if data=="UP":
            up()
        if data=="DOWN":
            down()
        if data=="LEFT":
            left()
        if data=="RIGHT":
            right()
        pygame.display.update()
        fpsClock.tick(FPS)

        time.sleep(0.5)

thread1 = threading.Thread(target = serve, args = (s,))
thread1.start()

while True:
    DISPLAYSURF.blit(background,(0,0))

    DISPLAYSURF.blit(sprite,(spritex,spritey))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            ev="QUIT"
        if event.type == KEYDOWN:
            if (event.key == K_LEFT):
                left()
                ev="LEFT"
                s.send(ev.encode())
                
            elif (event.key == K_RIGHT):
                right()
                ev="RIGHT"
                s.send(ev.encode())
                
            elif (event.key == K_UP):
                up()
                ev="UP"
                s.send(ev.encode())
                
            elif (event.key == K_DOWN):
                down()
                ev="DOWN"
                s.send(ev.encode())
               

    pygame.display.update()
    fpsClock.tick(FPS)
    
   
s.close()