#!/usr/bin/env python

import sys
import socket
import time

sock = socket.create_connection(("127.0.0.1",1337))

s = chr(0x7f)
l = chr(192)
r = chr(64)

while True:
	sock.sendall(str(s)+str(l)+str(r))
	time.sleep(.1)	
