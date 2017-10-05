Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> book = dict()
>>> book["apple"] = 0.67
>>> book["milk"] = 1.49
>>> book["avocado"] = 1.49
>>> print book
{'avocado': 1.49, 'apple': 0.67, 'milk': 1.49}
>>> print book["apple"] = 0.67
SyntaxError: invalid syntax
>>> book["apple"] = 0.67
>>> print book
{'avocado': 1.49, 'apple': 0.67, 'milk': 1.49}
>>> book["apple"] = 0.96
>>> print book
{'avocado': 1.49, 'apple': 0.96, 'milk': 1.49}
>>> 
