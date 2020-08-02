# imports
from cefpython3 import cefpython as cef
from sys import excepthook

import dataTransfer as dti

# random function to use as a callback
def testFunc():
    gateway.setAttribute('counter', 'altId', 'scrap')
    gateway.setText('scrap', ' hello', False)
    gateway.setContent('randomHolder', '<br> <input type="text" value="Your name">', False)

    printDM()

def printDM():
    print(gateway._dataMirror)
    print()

# Main code here
excepthook = cef.ExceptHook
cef.Initialize()

# Object Declarations
driver = cef.CreateBrowserSync(
    url="file:///D:\\Projects\\GitHub\\Proton\\Temp\\dataTransferTest.html",
    window_title="Fiddling Around")
gateway = dti.Gateway(driver)
bindings = cef.JavascriptBindings()

#update gateway, this will be done automatically in final release
gateway.updateMirror('scrap', 'innerText', 'This is the original Text.')

# Getting the python-js bindings ready
# tried this, bindings.SetObject('bind', gateway.bind)
# it doesn't work
bindings.SetObject('gateway', gateway)
bindings.SetFunction('pyPrint', printDM)
bindings.SetFunction('msg_inc', testFunc)

# BInding stuff
driver.SetJavascriptBindings(bindings)

# Running the super whimsical app
cef.MessageLoop()
cef.Shutdown()