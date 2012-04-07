#!/usr/bin/env python

import pygame
from pygame.locals import *
import time
import sys
import threading
import socket
from ez430 import *

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
#sock = socket.create_connection((sys.argv[1],1337))
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
#thread_comm_thread = threading.Thread(target=comm_thread)
#thread_comm_thread.setDaemon(True)
#thread_comm_thread.setName("comm_thread")
#thread_comm_thread.start()

ez = False
if len(sys.argv) == 3:
	ez = True

#drive from a ti chronos watch?
ez_ser = None
if ez:
	ez_ser = ez_start()

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


	if ez:
		ez_data = ez_read(ez_ser)
		if ez_data != None:
			ez_x = ord(ez_data[0])
			ez_y = ord(ez_data[1])
			ez_z = ord(ez_data[2])

			print ez_x
			print ez_y
			print ez_z
			print "\n"

			ez_w = False
			ez_a = False
			ez_s = False
			ez_d = False

			if ez_x > 200 and ez_x < 250:
				ez_w = True
			if ez_x > 40 and ez_x < 100:
				ez_s = True
			if ez_y > 150 and ez_y < 230:
				ez_a = True
			if ez_y > 10 and ez_y < 100:
				ez_d = True

			if ez_w and not (ez_a or ez_d):
				screen.blit(w,dir_pos)
				motorL = maxL
				motorR = maxR
			if ez_s and not(ez_a or ez_d):
				screen.blit(s,dir_pos)
				motorL = minL
				motorR = minR
			if ez_a and not (ez_w or ez_s):
				screen.blit(a,dir_pos)
				motorL = minL
				motorR = maxR
			if ez_d and not(ez_w or ez_s):
				screen.blit(d,dir_pos)
				motorL = maxL
				motorR = minR
			if ez_w and ez_a:
				screen.blit(wa,dir_pos)
				motorL = neutralL
				motorR = maxR
			if ez_w and ez_d:
				screen.blit(wd,dir_pos)
				motorL = maxL
				motorR = neutralR
			if ez_s and ez_a:
				screen.blit(sa,dir_pos)
				motorL = neutralL
				motorR = minR
			if ez_s and ez_d:
				screen.blit(sd,dir_pos)
				motorL = minL
				motorR = neutralR


	# draw the TURBO MODE!
	if key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
		screen.blit(turbo,turbo_pos)

	font = pygame.font.Font(None, 25)	
	text = font.render(hex(ord(motorL)) + ' ' + hex(ord(motorR)),True,white)

	screen.blit(text,[10,10])
	pygame.display.flip()

pygame.quit()
