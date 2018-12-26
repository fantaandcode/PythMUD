#!/usr/bin/python

import os
import subprocess
import sys

# local imports
from game.checkInput import checkInput
from game.room import room
from game.room import exit
from game.room import roomops

from utils.textC import textC as tC
from utils.helpMsg import helpMsg

# get terminal size
rows, columns = subprocess.check_output(['stty', 'size']).decode().split()

room_list = []			# list of room IDs
messageLog = []			# log of messages
max_message_len = int(columns)	# max length of a message
mL_show_length = 10		# showed messages
mL_max_length = 100		# max stored messages

spacer = '=' * max_message_len	# normal spacer

class main():
	player_rID = 1
	mL_to_print = 0

	def __init__(self):
		print("initing")
		main.room_load(self)
		os.system('clear')
		main.main_loop(self)

	def room_load(self):	# currently only in testing, using a predefined room layout, not from a file for now
		print("Loading rooms")
		room_list.append(roomops.newRoom(1, "Test room", "Testing room's description.", [], []))
		room_list[0].addExit("south", 2)
		room_list.append(roomops.newRoom(2, "Test room 2", "Testing room 2's description.", [], []))
		room_list[1].addExit("north", 1)

	def main_loop(self):
		print("\n" * int(rows))
		print(spacer)
		while True:
			player_in = input(tC.gb('> '))

			if player_in == '':
				print("Please input a command.")
			else:
				main.signal_handling(self, player_in)

	def signal_handling(self, player_in):
		# -1 is reserved for help
		# 0 is reserved for unrecognized input
		# 1  - 10 are reserved for room interaction
		# 11 - 20 are reserved for room traversal
		# 9999 is reserved for exiting game
		ret = checkInput.checkInput(player_in)
		messageLog.append(ret[0])
		
		if ret[1] == -1:
			helpMsg.printhelp()
			print(spacer)
		elif ret[1] == 0:
			print(messageLog[-1])
			print(spacer)
		elif ret[1] == 1:	# look
			for i in room_list:
				if i.getID() == self.player_rID:	# get description of room and exits
					# print("rID, pID:", i.getID(), player_rID)	# room's ID and player's current ID, just to make sure they match
					messageLog[-1] += "\n" + i.getDesc()	# print description
					if len(i.getExits()) == 0:
						messageLog[-1] += "\nThere are " + tC.gb("no") + " exits in this room."
					elif len(i.getExits()) == 1:
						messageLog[-1] += "\nThere is an exit to the " + tC.gb(i.getExits()[0].getDir()) + "."
					elif len(i.getExits()) == 2:
						messageLog[-1] += "\nThere are exits to the " + tC.gb(i.getExits()[0].getDir()) + " and " + tC.gb(i.getExits()[1].getDir()) + "."
					else:
						messageLog[-1] += "\nThere are exits to the "
						for j in i.getExits():
							if j == i.getExits()[-1]:
								messageLog[-1] += "and " + tC.gb(j.getDir()) + "."
							else:
								messageLog[-1] += tC.gb(j.getDir())
			print(messageLog[-1])
			print(spacer)
		elif ret[1] == 11:	# north
			new_room = main.move(self, 'north')
			self.player_rID = new_room
			print(spacer)
		elif ret[1] == 12:	# east
			new_room = main.move(self, 'east')
			self.player_rID = new_room
			print(spacer)
		elif ret[1] == 13:	# south
			new_room = main.move(self, 'south')
			self.player_rID = new_room
			print(spacer)
		elif ret[1] == 14:	# west
			new_room = main.move(self, 'west')
			self.player_rID = new_room
			print(spacer)
		elif ret[1] == 9999:
			print(messageLog[-1])
			print(spacer)
			sys.exit()

		self.mL_to_print += 1

	def move(self, direction):	# move action
		for i in room_list:
			if i.getID() == self.player_rID:
				for j in i.getExits():
					if j.getDir() == direction:
						messageLog[-1] += "\nYou go through the " + tC.gb(direction + "ern") + " exit."
						print(messageLog[-1])
						return j.getToRoom()
					else:
						messageLog[-1] += "\nThere is " + tC.gb("no") + " exit to the " + tC.gb(direction) + "."
						print(messageLog[-1])
						self.mL_to_print += 1
						return self.player_rID

main()