Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def quicksort (array):
       if len (array) < 2:
	  return array
       else:
          pivot = array[0]
          less = [i for i in array[1:] if i <= pivot]
          greater = [i for i in array[1:] if i > pivot]
          return quicksort (less) + [pivot] + quicksort (greater)

        
>>> print quicksort ([10, 5, 2, 3])
[2, 3, 5, 10]
>>> 
