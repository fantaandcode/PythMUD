#!/usr/bin/python

import socket
import sys
from utils.textC import textC as tC

print("Starting server...")
# create socket
#try:
#	psock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#except socket.error as err:
#	print("Socket creation failed with error %s", err)

# create socket
try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
	print("Socket creation failed with error %s", err)

# bind psock and listen for output from server
#psock.bind(('', 0))
#psock.listen(10)
#print("Psock listening...")

# connect sock to connect to server and 
host_port = 8888

try:
	host_ip = socket.gethostname()
except socket.gaierror:
	print("There was an error resolving the host")
	sys.exit()

# call socket with server's IP address and port to initiate connection to server
sock.connect((host_ip, host_port))

# get socket information
s_peername = sock.getpeername()
s_sockname = sock.getsockname()

#p_sockname = psock.getsockname()

print("sock peer:", s_peername)
print("sock name:", s_sockname)
#print("psock nme:", p_sockname)

data = sock.recv(1024)
data_as_string = data.decode("utf-8")

print("Received: \n" + data_as_string)

player_in = input(tC.gb('> '))

sock.send(player_in.encode())