import base64

from cefpython3 import cefpython as cef
from sys import excepthook

htmlCode = '''
<html>

<head>
    <script>
        function setText(Id, value) {
            document.getElementById(Id).innerText = value;
        }

    </script>
</head>

<body>
    <h1 id="counter">Button pressed 0 times.</h1>

    <a href=# onclick="msg_inc()">
        <div style="background-color: chocolate; align-self: center; justify-self: center; height: 50px; width: 50px;">
        </div>
    </a>
</body>

</html>
'''

def html_to_data_uri(html):
    # This function is called in two ways:
    # 1. From Python: in this case value is returned
    # 2. From Javascript: in this case value cannot be returned because
    #    inter-process messaging is asynchronous, so must return value
    #    by calling js_callback.
    html = html.encode("utf-8", "replace")
    b64 = base64.b64encode(html).decode("utf-8", "replace")
    ret = "data:text/html;base64,{data}".format(data=b64)
    
    return ret

global counter
counter = 0

def msg_increment(counter = counter):
    globals()['counter'] += 1
    q = 'Button pressed ' + str(globals()['counter']) + ' times.'
    driver.ExecuteFunction("setText", 'counter', q)


excepthook = cef.ExceptHook
cef.Initialize()

bindings = cef.JavascriptBindings()
bindings.SetFunction('msg_inc', msg_increment)

driver = cef.CreateBrowserSync(url=html_to_data_uri(htmlCode) ,window_title="Fiddling Around")
driver.SetJavascriptBindings(bindings)

cef.MessageLoop()
cef.Shutdown()
