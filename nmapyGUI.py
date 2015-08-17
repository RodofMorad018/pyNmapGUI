"""
_______________________________________________________________
nmapyGUI.py

AUTHOR(S): Nicholas Moradi		nicholasmoradi@yahoo.comm

PURPOSE- Module creates class object. Object is supposed to get data from Entry
            and Drop Down menus once user has input data. Data is sent to a
            string compilation module to develop string ready to be executed.
_______________________________________________________________
"""

#BEGIN IMPORTS
from tkinter import *
from sys import platform as _platform
from pathfind import getPath
from stringCompilation import getEntry, getDiscovery, compileString
#END IMPORTS

#GLOBAL STATIC VARIABLES
""" Used in order to create fields and drop down menus """
fields = ['IP Address']
host_opts = ["-sL", "-sn", "-Pn", "--traceroute"]
#END GLOBAL

class App:
    def __init__(self, master):
      frame = Frame(master)
      frame.pack()
      self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
      self.button.pack(side=RIGHT)
      self.slogan = Button(frame, text="Hello", command=self.write_slogan)
      self.slogan.pack(side=LEFT)
      self._createMenu(master)
      entries = self._createFields(master)
      self._getFields(master, entries)
      self._createCasade(master)
    def write_slogan(self):
      print ("Tkinter is easy to use!")
    def _createMenu(self, master):
      menu = Menu(master)
      master.config(menu=menu)
      filemenu = Menu(menu)
      menu.add_cascade(label="File", menu=filemenu)
      filemenu.add_command(label="Exit", command=master.quit)
      helpmenu = Menu(menu)
      menu.add_cascade(label="Help", menu=helpmenu)
      helpmenu.add_command(label="About")
      return
    def _createFields(self, master):
      entries = []
      for field in fields:
        row = Frame(master)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
      return entries
    def _getFields(self, master, entries):
      stringList = []
      for entry in entries:
        field = entry[0]
        text = entry[1].get()
        #print('%s: "%s"' % (field, text))
        stringList.append(entry[1].get())
      getEntry(stringList)
      #master.bind('<Return>', (lambda event, data=entries: getEntry(data)))
      #testButton = Button(master, text='Show', command=(lambda data=entries: getEntry(data)))
      #testButton.pack(side=BOTTOM)
      return
    def _createCasade(self, master):
      master.title("Host Discovery Options")
      var = StringVar(master)
      var.set(host_opts[0])
      label = Label(master, text='Host Discovery Options').pack(side=LEFT)
      options = OptionMenu(master, var, *host_opts)
      options.pack(side=RIGHT)
      getDiscovery(var.get())
      return
    #def _executeString():
