# What is this document?

This is where various interfaces are documented and modified till we reach a
working release at which point we'll cook up some proper (official)
documentation.

# What is an interface?

I'm pretty sure you  guys know already but for those of you who don't, a
interface is like a list of functions with the input/output they accept/give.
Now any amount of monkey-business can happen in the implementation but for the
user of that function/class, it now looks like a clean, beautiful and simple
group of classes/functions.

The second reason interfaces are designed is to simplify fixing of breakages -
lets say that your code scraps data of a website, because of website updates,
the code to scrap that same data changes drastically, as long as you can
implement the same interface (which in most cases is possible) for the new
updated code, you won't have to bother about searching around and fixing every
single reference to that particular function call (and the resulting changes of
other code to make sure that the new/updated function call works) making the
job of updating the code infinitely easier and less intimidating (especially in
the case of large codebases)

# The interfaces

## 01. Data Transfer Interface

Functions defined here:
- [setAttribute](#setAttribute)
- [setText](#setText)
- [setContent](#setContent)
- [readAttribute](#readAttribute)
- [readText](#readText)
- [readContent](#readContent)

<br> <br>

### setAttribute

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| id | str | The id assigned to the relevant html element |
| attribute | str | attribute to be set (case sensitive) |
| value | any | value of the attribute to be set |
| **RETURN** | - | nothing is returned |

<br> <br>

### setText

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| id | str | The id assigned to the relevant html element |
| toReplace | bool | `False` to append to current display-text, else `True` |
| value | str | The display-text to be set |
| **RETURN** | - | nothing is returned |

Make sure to replace python's `'\n'` with html's `<br>`

<br> <br>

### setContent

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| id | str | The id assigned to the relevant html element |
| toReplace | bool | `False` to append to current display-text, else `True` |
| value | str | html code to be added within the selected element |
| **RETURN** | - | nothing is returned |

<br> <br>

### readAttribute

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| id | str | The id assigned to the relevant html element |
| attribute | str | attribute to be set (case sensitive) |
| **RETURN** | str | value set to the selected attribute as a str |

<br> <br>

### readText

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| id | str | The id assigned to the relevant html element |
| **RETURN** | str | display-text of the selected element |

Make sure to switch html's `<br>` to python's `\n`

<br> <br>

### readContent

| Parameter | Type | Description |
| --------- | ---- | ----------- |
| id | str | The id assigned to the relevant html element |
| **RETURN** | str | html code within the selected element |

<br> <br>