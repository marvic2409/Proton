# What is this document?

Proton's purpose is ambitious. Proton's expectations equally so, but it won't
will/wish itself into existance. It requires vision and it requires work and
beyond all of that it requires ideas and it requires a plan.

This document (assuming that this project will pick up steam) is meant to
show, in broad strokes what we plan to do and how to get there.

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

It is excedingly hard to change attributes/variables livetime in JS from python
as you have to hardcode the attribute if using JS functions.

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

A better soultuion,

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
don't have to check the whole python object attribute thing. If consistant
abstraction is implimented so that class attributes aren't directly referenced
at any point (i.e. they are only manipulated via class methods), nothing like
what has been done for JS will be required, else yes. cefpython documentation
clearly states that though objects can be 'bound' to instances of cefpython's
browser so that it can be called from JS, in actuality, only the functions are
bound and not the whole object. So yeah, proper abstraction or you'll have a
bug on your hands.