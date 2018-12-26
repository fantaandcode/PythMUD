#!/usr/bin/python

class checkInput:
	def checkInput(input):

		return_msg = ''
		return_sig = 0
		
		# parse the input and check for msg and signal to return
		if input.lower() == "exit" or input.lower() == "x":
			return_msg = "Exiting game."
			return_sig = 9999
		elif input.lower() == "help" or input.lower() == "h":
			return_msg = "Help text, this should not show up, however"
			return_sig = -1
		elif input.lower() == "look" or  input.lower() == "l":
			return_msg = "You take a look around."
			return_sig = 1
		elif input.lower() == "north" or  input.lower() == "n":
			return_msg = "You attempt to go through the northern exit."
			return_sig = 11
		elif input.lower() == "east" or  input.lower() == "e":
			return_msg = "You attempt to go through the eastern exit."
			return_sig = 12
		elif input.lower() == "south" or  input.lower() == "s":
			return_msg = "You attempt to go through the southern exit."
			return_sig = 13
		elif input.lower() == "west" or  input.lower() == "w":
			return_msg = "You attempt to go through the western exit."
			return_sig = 14
		else:
			return_msg = input + " is not a recognized command"
			return_sig = 0

		return (return_msg, return_sig)