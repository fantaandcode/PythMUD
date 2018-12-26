#!/usr/bin/python

import textC as tC
import os

def printhelp():
	help_msg = [tC.gb("h") + "elp\treturns this message",
		"e" + tC.gb("x") + "it\texits the game",
		tC.gb("n") + "orth\tmoves north",
		tC.gb("e") + "ast\tmoves east",
		tC.gb("s") + "outh\tmoves south",
		tC.gb("w") + "est\tmoves west"
		]
	for i in help_msg:
		print(i)