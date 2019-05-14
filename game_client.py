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
def serve(s):
    global spritex,spritey
    while True:
        data = s.recv(1024)
        data=data.decode()
        print("Data="+data)   
        if data=="UP":
            spritey-=5
        if data=="DOWN":
            spritey+=5
        if data=="LEFT":
            spritex-=5
        if data=="RIGHT":
            spritex+=5
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
                spritex-=5
                ev="LEFT"
                s.send(ev.encode())
                #sprite=pygame.image.load('RED.BMP')
            elif (event.key == K_RIGHT):
                spritex+=5
                ev="RIGHT"
                s.send(ev.encode())
                #sprite=pygame.image.load('RED.BMP')
            elif (event.key == K_UP):
                spritey-=5
                ev="UP"
                s.send(ev.encode())
                #sprite=pygame.image.load('RED.BMP')
            elif (event.key == K_DOWN):
                spritey+=5
                ev="DOWN"
                s.send(ev.encode())
                #sprite=pygame.image.load('RED.BMP')

    pygame.display.update()
    fpsClock.tick(FPS)
    
    #print(gamers)
    #print(x,y)
s.close()