#!/usr/bin/python

from utils.textC import textC as tC
import os

class helpMsg:
	def printhelp():
		help_msg = [tC.gb("h") + "elp\treturns this message",
			"e" + tC.gb("x") + "it\texits the game",
			"",
			tC.gb("l") + "ook\tlooks around",
			tC.gb("n") + "orth\tmoves north",
			tC.gb("e") + "ast\tmoves east",
			tC.gb("s") + "outh\tmoves south",
			tC.gb("w") + "est\tmoves west"
			]
		for i in help_msg:
			print(i)