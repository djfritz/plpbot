#!/usr/bin/env python

import pygame
from pygame.locals import *
import time
#import vlc
import sys
import threading
import socket

#vlc initialization
#p=vlc.MediaPlayer('./sample_mpeg4.mp4')
#p.play()

#command window
black = (0,0,0)
white = (255,255,255)

pygame.init()

size=width,height=640,391;screen=pygame.display.set_mode(size);pygame.display.set_caption("plpbot control window")

plp = pygame.image.load("plpbot.png").convert()
w = pygame.image.load("w.png").convert()
s = pygame.image.load("s.png").convert()
a = pygame.image.load("a.png").convert()
d = pygame.image.load("d.png").convert()
wa = pygame.image.load("wa.png").convert()
wd = pygame.image.load("wd.png").convert()
sd = pygame.image.load("sd.png").convert()
sa = pygame.image.load("sa.png").convert()

done=False
clock=pygame.time.Clock()

#socket
sock = socket.create_connection((sys.argv[1],1337))
header = chr(0x7f)
neutralL = chr(64)
neutralR = chr(192)
maxL = chr(127)
minL = chr(1)
maxR = chr(255)
minR = chr(128)
motorL = neutralL
motorR = neutralR

def comm_thread():
	while True:
		sock.sendall(str(header)+str(motorL)+str(motorR))
		time.sleep(.01)

#start the communication thread
thread_comm_thread = threading.Thread(target=comm_thread)
thread_comm_thread.setDaemon(True)
thread_comm_thread.setName("comm_thread")
thread_comm_thread.start()

while done==False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True

	screen.fill(black)

	#draw the screen contents
	screen.blit(plp,[0,0])

	clock.tick(20)

	keys = ""
	pygame.event.pump()
	key=pygame.key.get_pressed()
	dir_pos = [450,220]
	if key[pygame.K_w] and key[pygame.K_a]:
		screen.blit(wa,dir_pos)
		motorL = neutralL
		motorR = maxR
	elif key[pygame.K_w] and key[pygame.K_d]:
		screen.blit(wd,dir_pos)
		motorL = maxL
		motorR = neutralR
	elif key[pygame.K_s] and key[pygame.K_a]:
		screen.blit(sa,dir_pos)
		motorL = neutralL
		motorR = minR
	elif key[pygame.K_s] and key[pygame.K_d]:
		screen.blit(sd,dir_pos)
		motorL = minL
		motorR = neutralR
	elif key[pygame.K_w]:
		screen.blit(w,dir_pos)	
		motorL = maxL
		motorR = maxR
	elif key[pygame.K_s]:
		screen.blit(s,dir_pos)
		motorL = minL
		motorR = minR
	elif key[pygame.K_a]:
		screen.blit(a,dir_pos)
		motorL = minL
		motorR = maxR
	elif key[pygame.K_d]:
		screen.blit(d,dir_pos)
		motorL = maxL
		motorR = minR
	else:
		motorL = neutralL
		motorR = neutralR

#	font = pygame.font.Font(None, 25)	
#	text = font.render(keys,True,white)

#	screen.blit(text,[10,10])
	pygame.display.flip()

pygame.quit()
