Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
book = dict()
>>> book
{}
>>> 
>>> book["apple"] = 0.67
>>> book["milk"] = 1.49
>>> book["avocado"] = 1.49
>>> print book
SyntaxError: Missing parentheses in call to 'print'
>>> book = dict()
>>> book["apple"] = 0.67
>>> book["milk"] = 1.49
>>> book["avocado"] = 1.49
>>> print book
SyntaxError: Missing parentheses in call to 'print'
>>> book = dict()
>>> book["apple"] = 0.67
>>> book["milk"] = 1.49
>>> book["avocado"] = 1.49
>>> print(book)
{'apple': 0.67, 'milk': 1.49, 'avocado': 1.49}
>>> 
