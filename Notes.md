# The thing in a nutshell

Of prime importance is the tutorial.py file under examples. Note to self, all
the magic is in binding objects and the 'External' class defined near the
bottom. The whole shifty-mind fuck series of function calls to/from
python/js to each other start in JS calling the 'test_multiple_callbacks'
method of the 'External' object passed to the browser instance (i guess?
confusing buisness this is). External is actually a verry crappy, misleading,
confusing name for a class/variable, he (cztomczak) did a good job of variables
everywhere else, wonder what happened here.

The jumping (passing) of functions (read objects if required) between JS and
python is mindbendingly confusing but not entirely impossible to grasp. It is
of primary interest to handle this confusing difficulty immediately, once this
is handled, it’s only a matter of providing a one-sided approach to reading
and updating data on the webpage side alongside a method to design the UI
without any significant html/css skills without loss of flexibility.

For many, if I get to that point, a UI editor should be welcome and can be
readily based of BootstrapStudio. Secondly, the sporadic development of
cefpython is a sad sight but at least as of now, not an issue because the
primary aim of Proton is to utilize CEF as a flexible GUI rendering platform
and not to expose CEF bindings to python for what ever task you might have at
hand, though cztomczak claims that cefpython3 v66 is electron for python, the
ease of use it provides and its in-general super broad application make it a
possible electron for python - which is the aim of Proton, either ways the
man deserver fair credit for handling cefpython almost singlehandedly.
