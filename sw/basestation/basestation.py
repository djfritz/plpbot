#!/usr/bin/env python

import serial
import sys
import socket
import time
import threading

class bs:
	def __init__(self, serial_t, sock_t):
		self.serial = serial_t
		self.socket = sock_t
		self._write_lock = threading.Lock()

	def sersock(self):
		while self.alive:
			try:
				data = self.serial.read(1)
				n = self.serial.inWaiting()
				if n:
					data = data + self.serial.read(n)
				if data:
					print(data)
				self._write_lock.acquire()
				try:
					self.socket.sendall(data)
				finally:
					self._write_lock.release()
			except socket.error, msg:
				break
		self.alive = False

	def sockser(self):
		while self.alive:
			try:
				data = self.socket.recv(3)
				if not data:
					break
				print(hex(ord(data[0])) + ' ' + hex(ord(data[1])) + ' ' + hex(ord(data[2])))
				self.serial.write(data)
			except socket.error, msg:
				sys.stderr.write("[e] sockser: %s\n" % msg)
				break
		self.alive = False

	def stop(self):
		if self.alive:
			self.alive = False
			self.thread_sersock.join()

	def start(self):
		self.alive = True
		self.thread_sersock = threading.Thread(target=self.sersock)
		self.thread_sersock.setDaemon(True)
		self.thread_sersock.setName("sersock")
		self.thread_sersock.start()
		self.sockser()

#open serial port
ser = serial.Serial(sys.argv[1],57600,timeout=1)
ser.port 	= sys.argv[1]
ser.baudrate 	= 57600 
ser.timeout 	= 1

try:
	ser.open()
except serial.SerialExceptio, e:
	sys.stderr.write("[e] could not open serial port %s: %s\n" % (ser.portstr, e))
	sys.exit(1)

#open socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',1337))
sock.listen(1)
while True:
	try:
		print("[i] waiting for connection...")
		connection, addr = sock.accept()
		print("[i] client %s connected" % (addr,))
		
		f = bs(ser, connection)
		f.start()
		#if we get here...
		f.stop()
	
		print("[w] disconnected")
		connection.close()
	except KeyboardInterrupt:
		break
	except socket.error, msg:
		sys.stderr.write("[e] socket error: %s" % msg)

print("[i] exit")

