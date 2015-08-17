global entry_string
global cascade_string


def getEntry(strList):
    entry_string = strList
    return
#def getCheck():
def getDiscovery(casStr):
    cascade_string = casStr
    return
def compileString(master):
    def _show(string):
        print (string)
    string = 'nmap' + entry_string + cascade_string
    testButton = Button(master, text='Show', command=(lambda data=string: _show(data)))
    testButton.pack(side=BOTTOM)
