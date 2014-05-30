#!/usr/bin/env python

import socket

s = None

def connect(host, port):
	global s
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))

def close():
	global s
	s.close()

def send(msg):
	global s
	print msg
	#s.send(msg + "\n")

def turn_on(name):
	send('set %s on ' % name)

def turn_off(name):
	send('set %s off ' % name)

def set_value(name, value):
	send('set %s value %d' % (name,int(value/2.55)))

if __name__ == '__main__':
	import time
	FHEM_HOST = 'saallicht'
	FHEM_PORT = 7072
	connect(FHEM_HOST,7072)
	turn_off('K62_Buehne_EA')
	time.sleep(10)
	set_value('K62_Buehne_Wert',10)
	close()

