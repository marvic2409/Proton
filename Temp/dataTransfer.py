# Note, in python code, the 'id' parameter breaks naming conventions and is set
# as 'ID' because 'id' is one of pythons standard library functions.
#
# This file works in conjunction with the dataTransfer.js file, the working
# of this system of reading/writing/editing data on CEF livetime requires
# that an instance of the Gateway class be bound to the CEF browser instance.

class ProtonException(Exception): pass

class UnboundJavascript(ProtonException): pass

class Gateway(object):

    def __init__(self, driver):
        self._driver = driver
        self._dataMirror = {}
        self._jsBound = False
    
    # Behind the Scenes functions

    def bind(self, setAttribute, setText, setContent):
        self._setAttribute = setAttribute
        self._setText = setText
        self._setContent = setContent

        self._jsBound = True

        # This is for final production (ideally)
        #
        # bindings = cef.JavascriptBindings()
        # bindings.SetObject('gateway', gateway)
        # driver.SetJavascriptBindings(bindings)
    
    def updateMirror(self, ID, property, value):
        if ID not in self._dataMirror.keys():
            self._dataMirror[ID] = {}
        
        self._dataMirror[ID][property] = value

    # DTI interface

    def setAttribute(self, ID, attribute, value):
        if self._jsBound:
            self._setAttribute.Call(ID, attribute, value)
        else:
            raise UnboundJavascript
        
        self.updateMirror(ID, attribute, value)
    
    def setText(self, ID, displayText, toReplace = True):
        if self._jsBound:
            self._setText.Call(ID, displayText, toReplace)
        else:
            raise UnboundJavascript

        if toReplace:
            self.updateMirror(ID,'innerText', displayText)
        else:
            cText = self.readText(ID)
            self.updateMirror(ID, 'innerText', cText + displayText)

    def setContent(self, ID, htmlCode, toReplace = True):
        if self._jsBound:
            self._setContent.Call(ID, htmlCode, toReplace)
        else:
            raise UnboundJavascript

        if toReplace:
            self.updateMirror(ID, 'innerHTML', htmlCode)
        else:
            cHtml = self.readContent(ID)
            self.updateMirror(ID, 'innerHTML', cHtml + htmlCode)
    
    def readAttribute(self, ID, attribute):
        if ID not in self._dataMirror.keys():
            self._dataMirror[ID] = {}
        
        if attribute not in self._dataMirror[ID].keys():
            self._dataMirror[ID][attribute] = ''

        return self._dataMirror[ID][attribute]
    
    def readText(self, ID):
        if ID not in self._dataMirror.keys():
            self._dataMirror[ID] = {}
        
        if 'innerText' not in self._dataMirror[ID].keys():
            self._dataMirror[ID]['innerText'] = ''

        return self._dataMirror[ID]['innerText']
    
    def readContent(self, ID):
        if ID not in self._dataMirror.keys():
            self._dataMirror[ID] = {}
        
        if 'innerHTML' not in self._dataMirror[ID].keys():
            self._dataMirror[ID]['innerHTML'] = ''

        return self._dataMirror[ID]['innerHTML']