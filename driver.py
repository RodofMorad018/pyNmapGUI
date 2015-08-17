"""
_______________________________________________________________
driver.py

AUTHOR(S): Nicholas Moradi		nicholasmoradi@yahoo.comm

PURPOSE- Driver for the inital creation of the GUI. First checks for the default
            location of nmap. If OS is supported continue
_______________________________________________________________
"""

#BEGIN IMPORTS
from tkinter import *
from sys import platform as _platform
from pathfind import getPath
from nmapyGUI import App
#END IMPORTS



if _platform == "linux" or _platform == "linux2":
    f_location = getPath(_platform)# linux
elif _platform == "darwin":
    f_location = getPath(_platform)
else:
    return
#elif _platform == "win32":
   # Windows


root = Tk()
app = App(root)
root.mainloop()
