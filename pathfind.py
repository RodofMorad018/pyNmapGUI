"""
_______________________________________________________________
pathfind.py

AUTHOR(S): Nicholas Moradi		nicholasmoradi@yahoo.comm

PURPOSE- Module detects default installation of nmap based on
			the platform of the operating system. Returns nmaps
			file location as a string
_______________________________________________________________
"""

import os
from os import *
def getPath(os_type):
	plist = []
	if os_type == 'linux' or 'linux2':
		file_path = "/usr/bin/"
	if os_type == 'darwin':
		file_path = "/usr/local/bin/"
	for root, dirs, files in os.walk(file_path, topdown=False):
		for name in files:
			if name.endswith("xnmap"):
				#print(os.path.join(root,name))
				plist.append(os.path.join(root,name))
			elif name.endswith("nmap"):
				plist.append(os.path.join(root,name))
	for programs in plist:
		if "xnmap" or "nmap" in programs:
			file_location = programs
			print(file_location)
			return file_location
			break
		else:
			print ("Couldn't find Nmap")
