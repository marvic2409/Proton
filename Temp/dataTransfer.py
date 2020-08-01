# Note, in python code, the 'id' parameter breaks naming convensions and is set
# as 'ID' because 'id' is one of pythons standard library functions.

class UnboundJavascript(Exception):
    pass

class Gateway(object):

    def __init__(self, driver):
        self._driver = driver
        self._dataMirror = {}
        self._jsBound = False

    def bind(self, setAttribute, setText, setContent):
        self._setAttribute = setAttribute
        self._setText = setText
        self._setContent = setContent

        self._jsBound = True
    
    def setAttribute(self, ID, attribute, value):
        if self._jsBound:
            self._setAttribute.Call(ID, attribute, value)
        else:
            raise UnboundJavascript
    
    def setText(self, ID, toReplace, value):
        if self._jsBound:
            self._setText.Call(ID, toReplace, value)
        else:
            raise UnboundJavascript

    def setContent(self, ID, toReplace, value):
        if self._jsBound:
            self._setContent.Call(ID, toReplace, value)
        else:
            raise UnboundJavascript