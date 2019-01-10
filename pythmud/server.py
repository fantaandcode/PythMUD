#!/usr/bin/python

import socket
import sys

HOST = socket.gethostname()		# get local machine name
PORT = 8888						# arbitrary non-privileged port

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

# bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print("Bind failed. Error: " + str(msg))
	sys.exit()

print("Socket bind complete")

# start listening on socket
s.listen(10)
print("Socket now listening")

# now keep talking with client
while True:
	c, addr = s.accept()
	c.send("Connected".encode())
	data_as_string = c.recv(1024).decode('utf-8')
	print(data_as_string)
	if data_as_string.lower() == 'exit':
		print("Closing connection")
		c.close()