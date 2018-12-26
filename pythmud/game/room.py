#!/usr/bin/python

import sys

class room():
	def __init__(self, ID, name, desc, items, exits):
		self.ID = ID
		self.name = name
		self.desc = desc
		self.items = items
		self.exits = exits
	
	def getName(self):
		return self.name

	def getID(self):
		return self.ID

	def getDesc(self):
		return self.desc

	def getItems(self):
		return self.items

	def getExits(self):		# array of exit objects, defined below
		return self.exits

	def addExit(self, direction, to_rID):
		#print("checking exits")
		#checking if there are duplicate exits
		for i in self.exits:
			#print("checking:", i.getDir())
			#print("attempt: ", direction)
			if i.getDir() == direction:
				print("There has been an error and there was an attempt to make an exit in a direction that already has one.")
		self.exits.append(exit(direction, to_rID))
		self.getExits()

class exit():	# exit object for a room
	def __init__(self, direction, to_room):
		self.direction = direction	# direction of exit
		self.to_room = to_room		# what room exit goes to
	def getDir(self):
		return self.direction
	def getToRoom(self):
		return self.to_room

class roomops:
	def newRoom(ID, name, desc, items, exits):	# create new room
		r = room(ID, name, desc, items, exits)
		print("Room", ID, "created.")
		return r