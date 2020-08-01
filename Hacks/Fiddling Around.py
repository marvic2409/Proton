from cefpython3 import cefpython as cef
from sys import excepthook

global counter, readAttribute, readContent, readText
counter = 0

def bind( rA, rC, rT):
    globals()['readAttribute'] = rA
    globals()['readContent'] = rC
    globals()['readText'] = rT
    print('binding complete\n')

def msg_increment(counter = counter):
    globals()['counter'] += 1
    q = 'Button pressed ' + str(globals()['counter']) + ' times.'
    driver.ExecuteFunction("setAttribute", 'counter', 'id', 'scrap')
    driver.ExecuteFunction("setText", 'scrap', True, q)
#    print('text changed in element scrap') # @pain
#    driver.ExecuteFunction("setContent", 'scrap', False, '<br><em>' + q + '</em>')

    if globals()['counter'] % 3 == 0:
        globals()['readText'].Call(['scrap', 'scrap', 'scrap', 'scrap', 'scrap', 'scrap', 'scrap'], print)
excepthook = cef.ExceptHook
cef.Initialize()

bindings = cef.JavascriptBindings()
bindings.SetFunction('msg_inc', msg_increment)
bindings.SetFunction('bind', bind)
bindings.SetFunction('printpy', print)

driver = cef.CreateBrowserSync(url="file:///D:/Projects/GitHub/Proton/Hacks/uiTests.html" ,window_title="Fiddling Around")
driver.SetJavascriptBindings(bindings)

cef.MessageLoop()
cef.Shutdown()
