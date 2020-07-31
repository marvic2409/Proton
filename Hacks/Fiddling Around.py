import base64

from cefpython3 import cefpython as cef
from sys import excepthook

global counter
counter = 0

def msg_increment(counter = counter):
    globals()['counter'] += 1
    q = 'Button pressed ' + str(globals()['counter']) + ' times.'
    driver.ExecuteFunction("setAttribute", 'counter', 'id', 'scrap')
    driver.ExecuteFunction("setText", 'scrap', False, '<br><em>' + q + '</em>')
#    driver.ExecuteFunction("setContent", 'scrap', False, '<br><em>' + q + '</em>')


excepthook = cef.ExceptHook
cef.Initialize()

bindings = cef.JavascriptBindings()
bindings.SetFunction('msg_inc', msg_increment)

driver = cef.CreateBrowserSync(url="file:///D:/Projects/GitHub/Proton/uiTests.html" ,window_title="Fiddling Around")
driver.SetJavascriptBindings(bindings)

cef.MessageLoop()
cef.Shutdown()
