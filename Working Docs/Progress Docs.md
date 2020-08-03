# What is this document?

Proton's purpose is ambitious. Proton's expectations equally so, but it won't
will/wish itself into existence. It requires vision and it requires work and
beyond all of that it requires ideas and it requires a plan.

This document (assuming that this project will pick up steam) is meant to
show, in broad strokes what we plan to do and how to get there. For the most
part though, it will put on display the thoughts and work process as it
progresses through dev.

look through [Notes](Notes.md), [Core Values](Core%20Values.md) and
[Readme](../README.md)

# The Actual stuff

Get cefPython and figure out not how it works but how to use it and use it
well.

Explore ideas related to GUI frameworks:
- Declarative UI and alternatives [Declarative better]
- Widgets and alternatives [I don't think there are alternatives]
- Event handling for processing and visual flair - concurrency?
- How to design the UI? Html+css+js+python or python only or python+scripting?
- Bootstrap for components (at least initially?)
- Just about everything else you can think/stumble across

Considering just how hard it is to understand codebases (especially
open-source ones), a method of documentation, quality standards and
most importantly compartmentalization of code.

Also, do you use it as a tool or a library? and just how does electronjs get
the '.exe' to open not to an empty page but the designed UI?

New Problems:
- How to handle complex layouts?

# Problem update

It is exceedingly hard to change attributes/variables live-time in JS from
python as you have to hardcode the attribute if using JS functions.

```js
//for those of you who didn't get that,

function setattr(Id, attribute, value){
    document.getElementById(Id).attribute = value; //error
}

// this wont work simply because you have to hardcode the attribute reference.
// a.k.a document.getElementById(Id).innerHTML = value;
// or document.getElementById(Id).style = value;
// but not the generic '.attribute = value;'
```


I suggest a crappy work around (which i cooked up while writing this), use a
standardized JS function to make the attribute switchable. That is,

```html
<head>
    <script>
        function setToAttribute(attributeValue){
            document.getElementById('transientScript').innerText = 
            "function set(Id, value){document.getElementById(Id)." + 
            attributeValue + "=value;}"
        }
    </script>

    <-- more stuff here -->
</head>

<body>
    <script id="transientScript">
    </script>

    <-- more stuff here -->
</body>

```
 So then, you have a variable attribute approach

 ```js

// calling this

 setToAttribute('innerHTML')
 
// creates this within the originally empty script element
// tagged 'transientScript'

function set(Id, value){
     document.getElementById(Id).innerHTML = value;    
}

// so now calling set(Id, value) will set the desired attribute.
 ```

A better solution,

```js

function setAttribute(id, attribute, value) {
    document.getElementById(id).setAttribute(attribute, value);
}

function setContent(id, to_replace, value) {
    if (to_replace) {
        document.getElementById(id).innerHTML = value;
    } else {
        document.getElementById(id).innerHTML += value;
    }
}

function setText(id, to_replace, value) {
    if (to_replace) {
        document.getElementById(id).innerText = value;
    } else {
        document.getElementById(id).innerText += value;
    }
}

// Now almost every single detail of elements with id's can be changed as and
// when required through three function calls with almost all of the logic
// being implemented in python itself. no JS knowledge required.
```

I still have to check if python object attributes can be changed or weather
something akin to what has been done for JS must be done for python too.

It's about 13 hours since me last touching this project, and it seems that I
don't have to check the whole python object attribute thing. If consistent
abstraction is implemented so that class attributes aren't directly referenced
at any point (i.e. they are only manipulated via class methods), nothing like
what has been done for JS will be required, else yes. cefpython documentation
clearly states that though objects can be 'bound' to instances of cefpython's
browser so that it can be called from JS, in actuality, only the functions are
bound and not the whole object. So yeah, proper abstraction or you'll have a
bug on your hands.

# The next big problem - UI Scripting

One of the major requirements of Proton is to eliminate 100% the need for JS
knowledge and figuring our how to make the setting/editing values of just
about any element a big jump forwards. There is still the issue of reading
values out of an element and the much bigger problem of getting html out of
the way of UI declaration.

Well, reading stuff ends up complicated af (obviously, why is this not easy?)
The JS callback is executed only after the python function has run its course
(apparently) and JS return values are not ported to python.

So, when you call python from JS and JS values are set from python, it follows
that there is a way to port JS values to python in live time instead of waiting
for control-flow to be passed on, I can't find any mention of it in the
cefpython docs and will have to stackoverflow it tomorrow. Well, being a bit
of a let-down, I couldn't/can't let go of the problem, apparently, the JS
callback is run after python 'returns control', note that my notions my be
misplaced and wrong because I don't know the internal workings of cefpython.
This is just my general idea.

There is a workaround, but I abhor it. I'm noting it here any ways.

Let `read(id, attribute)` be a function in JS that executes a python callback
that sets `document.getElementById(id).getAttribute(attribute)` to a python
variable called, lets say `jsValue`. We call `read(id, attribute)` from
python but it doesn't execute till control is passed back to JS, so all the
code that utilizes `jsValue` is worthless, so the rest of the code - the stuff
that utilizes `jsvalue` is instead passed to a function called
`dummyFunctionWrapper` and control passes back to JS. JS now calls
`dummyFunctionWrapper` as a callback after setting `jsValue` so everything
works out now. But imposing a predetermined structure on somebody's code is a
sure method of confusion and also some horrible framework (gui or otherwise)

# The data reading problem's solution

There is a handy solution to the issue at hand. Apparently as the python-JS
communication is asynchronous, returning JS values to python synchronously can
be done by making a default python callback wrapper that can be called from JS
to return the value from JS (complicated and unclear af, ik. I'll implement it
and then simplify what I mean). This is a simplification of yesterdays idea
picked up from [samuelhwilliams/Eel](https://github.com/samuelhwilliams/Eel).

Ok, so one possible solution is to have all JS return functions take a
pyCallback argument, then calling `pyCallback(returnValue)` instead of
attempting to return a value. The reading of multiple values will lead
to unnecessary fragmentation of code (which is very bad), so a single
call to a read function will multiple Id's is what i have in mind.
Due to not having the required html/js/css knowledge and not having
BootstrapStudio installed at the moment, I'll have to stop for now
till tomorrow.

# The Solution (readValues)

For the input, textarea and select tags, the onchange attribute can be used
to call a function to update a mirror of that particular element's data on the
python side.

```html
<input id= "testBox" type="text" onchange="updateMirror(this.id, this.value);">
```

```python
mirror = {}

def updateMirror(id, value):
    mirror[id] = value

# more code here

# essentially, when ever you want to read data from the webpage, all you got to
# do now is...

def something():
    # blah, blah, blah

    v = mirror['textBox']
    print('contents of testBox are: ' + v)

    # more blah, blah, blah

```

So, in short, you can read data live only from input/select/textarea tags which
isn't really all that bad. The attribute changes and stuff have to be initiated
via the python side and hence a small modification of the JS and `updateMirror`
code will ensure that all changes to elements with id's will be tracked in the
python mirror.

The next step is to code a proper data exchange interface and hopefully a UML
Diagram to keep it company (MS Visio Pro, here I come...)

Well, with the Data Exchange Interface done, the next major issue to tackle is
the scripting. Considering that its a big issue unto itself, I don't think it
wise to continue documenting progress/ideas here, so I'm continuing this in a
different file - [Progress Docs2](Progress%20Docs2.md)