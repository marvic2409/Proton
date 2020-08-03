# What is this file?

This file is a continuation of '[Progress Docs.md](Progress%20Docs.md)', its
been put into a new file because, here on, were going to tackle the scripting
language. I think it better to split up the work instead of cramming it into a
single file.

# A Scripting Concept

## Concept 01
```css
grid: 5x5

menuBar: 1.1 - 1.5 {
    menu: freeSize {
        displayText: File
    }
    menu: freeSize {
        displayText: Edit
    }
    menu: freeSize {
        displayText: View
    }
    menu: freeSize {
        displayText: Terminal
    }
    menu: freeSize {
        displayText: Help
    }
}

sideBar: 2.1 - 5.1 {
    grid: 7X1

    icon: 1.1 - 1.1 {
        id: fileTool
    }
    icon: 1.2 - 1.2 {
        id: searchTool
    }
    icon: 1.3 - 1.3 {
        id: gitTool
    }
    icon: 1.4 - 1.4 {
        id: testTool
    }
}

textArea: 2.2 - 5.5 {
    id: codeZone
}
```

## Concept 02
```js
body (grid = 5x5, componentDictionary = standard) {

    menuBar (position = r1) {

        menu (id = File, displayText = File,  grid = freeSize) {
            
            option (onClick = 'newFile();') {

                row () {

                    col (displayText = New File)

                    col (displayText = Ctrl + N)

                }
            }

            option (onClick = 'openFile();') {

                row () {

                    col (displayText = Open File)

                    col (displayText = Ctrl + O)

                }
            }

            breakRule ()

            // More options here
        }

        menu (id = Edit, displayText = Edit) {

            // Options here
        }
        
        menu (id = View, displayText = View) {

            // Options here
        }

        
        menu (id = Help, displayText = Help) {

            // Options here
        }

    }

    sideMenu (position = r2c1 - r5c1) {

        button (position = r2c1, id = FileTools, onclick = 'display("fileTools");') {

            icon (src = 'files tools.jpg')
        }

        // More buttons
    }

    textArea (position = r2c2 - r5c5, onLiveUpdate = 'colorCode();')

    // These are the displays for the Tools menus
    sideMenu (id = FileToolsMenu, visibility = false) {

        // More declarative UI here.
    }

}
```

Well, concept 02 seems better, the code style is very similar to html, details
being declared in `()` instead of within the html tag itself and the contents
of a tag being declared by `{}` instead of being placed b/w the opening and
closing tag. Now it'll all be absolutely worthless if I can't standardize the
settable properties, reduce repeat code and sort out the positioning/sizing.

<br><br>

For positioning/sizing:
- relative positioning/sizing
- absolute positioning/sizing
- free sizing

<br><br>

For reducing repeat code:
- create a standard shorthand notation for repeat code. This should ideally
allow setting of 1 or 2 values that vary from repeat code unit to the next
- Templates for commonly used code blocks

<br><br>

For standardization of settable properties:
- Figure out just what properties are exposed. Note styling is part of
'properties'

<br><br>

To settle in with Proton's core values:
- A generic 'componentDictionary' explorer

<br><br>

As to componentDictionaries:
- they map component names to the corresponding html and  group components
into Templates
- Isn't a predefined shorthand notation limiting flexibility?
- Ideally, you'd use descriptive Template/Template-sub-component names but
won't freedom of naming (shifting b/w Dictionaries) add to complexity?

Apart from the language design itself, I still have to write the interpreter,
and the Interpreter has to be able to accommodate the use of multiple
componentDictionaries while simultaneously interacting with a Gateway object to
update the dataMirror (see [DataTransfer.py](../Temp/DataTransfer.py)), do I
let the interpreter work on an 'interface system' or a 'read
componentDictionary' system?