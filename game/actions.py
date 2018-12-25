#!/usr/bin/python

def move(direction, playerRoom, roomList):
	for i in roomList:
		if i.getID() == playerRoom:
			for j in i.getExits():
				if j.getDir() == direction:
					return j.getToRoom()