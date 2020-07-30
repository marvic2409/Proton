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