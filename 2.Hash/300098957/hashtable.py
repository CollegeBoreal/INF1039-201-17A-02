Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> book = dict()
>>> print book
SyntaxError: Missing parentheses in call to 'print'
>>> book["Apple"]=0.67
>>> print book
SyntaxError: Missing parentheses in call to 'print'
>>> SyntaxError: Missing parentheses in call to 'print'
SyntaxError: invalid syntax
>>> print book()
SyntaxError: invalid syntax
>>> 
>>> print(book)
{'Apple': 0.67}
>>> book["Milk"]=1.49
>>> print(book)
{'Apple': 0.67, 'Milk': 1.49}
>>> book["Milk"]=1.51
>>> print(book)
{'Apple': 0.67, 'Milk': 1.51}
>>> book['Milk']=0.45
>>> print(book)
{'Apple': 0.67, 'Milk': 0.45}
>>> 
