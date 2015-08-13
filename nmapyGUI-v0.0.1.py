from tkinter import *
from sys import platform as _platform
from pathfind import getPath
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame,
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=RIGHT)
    self.slogan = Button(frame,
                         text="Hello",
                         command=self.write_slogan)
    self.slogan.pack(side=LEFT)
  def write_slogan(self):
    print ("Tkinter is easy to use!")

if _platform == "linux" or _platform == "linux2":
    f_location = getPath(_platform)# linux
elif _platform == "darwin":
    f_location = getPath(_platform)
#elif _platform == "win32":
   # Windows
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Exit", command=root.quit)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")
app = App(root)
root.mainloop()
