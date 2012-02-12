#!/usr/bin/env python

import pygame
from pygame.locals import *
import time
import sys
import threading
import socket

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
turbo = pygame.image.load("turbo.png").convert()
dir_pos = [450,220]
turbo_pos = [414,1]
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

#low gear
low_maxL = chr(96)
low_maxR = chr(224)
low_minL = chr(32)
low_minR = chr(160)

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
	if key[pygame.K_w] and key[pygame.K_a]:
		screen.blit(wa,dir_pos)
		if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
			motorL = neutralL
			motorR = maxR
		else:
			motorL = neutralL
			motorR = low_maxR
	elif key[pygame.K_w] and key[pygame.K_d]:
		screen.blit(wd,dir_pos)
		if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
			motorL = maxL
			motorR = neutralR
		else:
			motorL = low_maxL
			motorR = neutralR
	elif key[pygame.K_s] and key[pygame.K_a]:
		screen.blit(sa,dir_pos)
		if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
			motorL = neutralL
			motorR = minR
		else:
			motorL = neutralL
			motorR = low_minR
	elif key[pygame.K_s] and key[pygame.K_d]:
		screen.blit(sd,dir_pos)
		if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
			motorL = minL
			motorR = neutralR
		else:
			motorL = low_minL
			motorR = neutralR
	elif key[pygame.K_w]:
		screen.blit(w,dir_pos)
		if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
			motorL = maxL
			motorR = maxR
		else:
			motorL = low_maxL
			motorR = low_maxR
	elif key[pygame.K_s]:
		screen.blit(s,dir_pos)
		if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
			motorL = minL
			motorR = minR
		else:
			motorL = low_minL
			motorR = low_minR
	elif key[pygame.K_a]:
		screen.blit(a,dir_pos)
		if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
			motorL = minL
			motorR = maxR
		else:
			motorL = low_minL
			motorR = low_maxR
	elif key[pygame.K_d]:
		screen.blit(d,dir_pos)
		if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
			motorL = maxL
			motorR = minR
		else:
			motorL = low_maxL
			motorR = low_minR
	else:
		motorL = neutralL
		motorR = neutralR

	# draw the TURBO MODE!
	if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
		screen.blit(turbo,turbo_pos)

	font = pygame.font.Font(None, 25)	
	text = font.render(hex(ord(motorL)) + ' ' + hex(ord(motorR)),True,white)

	screen.blit(text,[10,10])
	pygame.display.flip()

pygame.quit()
