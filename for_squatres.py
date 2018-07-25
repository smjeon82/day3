Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> int('123')
123
>>> float('1.234')
1.234
>>> str(1234)
'1234'
>>> int(123)
123
>>> name='test'
>>> name.index('t')
0
>>> name.index('s')
2
>>> len(name)
4
>>> import sys
>>> sys.maxsize
9223372036854775807
>>> import random
>>> random.randit(1,10)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    random.randit(1,10)
AttributeError: module 'random' has no attribute 'randit'
>>> random.randint(1,10)
10
>>> random.randint(1,10)
8
>>> random.randint(1,10)
6
>>> random.randint(1,10)
10
>>> random.randint(1,10)
3
>>> import calendar
>>> calendar.monthcalendar(2018,7)
[[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]
>>> calendar.month(2018, 7)
'     July 2018\nMo Tu We Th Fr Sa Su\n                   1\n 2  3  4  5  6  7  8\n 9 10 11 12 13 14 15\n16 17 18 19 20 21 22\n23 24 25 26 27 28 29\n30 31\n'
>>> calendar.month(2018, 7, w=7, l=7)
'                       July 2018\n\n\n\n\n\n\n  Mon     Tue     Wed     Thu     Fri     Sat     Sun\n\n\n\n\n\n\n                                                    1\n\n\n\n\n\n\n    2       3       4       5       6       7       8\n\n\n\n\n\n\n    9      10      11      12      13      14      15\n\n\n\n\n\n\n   16      17      18      19      20      21      22\n\n\n\n\n\n\n   23      24      25      26      27      28      29\n\n\n\n\n\n\n   30      31\n\n\n\n\n\n\n'
>>> calendar.month(2018, 7)
'     July 2018\nMo Tu We Th Fr Sa Su\n                   1\n 2  3  4  5  6  7  8\n 9 10 11 12 13 14 15\n16 17 18 19 20 21 22\n23 24 25 26 27 28 29\n30 31\n'
>>> calendar.monthcalendar(2018,7)
[[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> math.kwlist
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    math.kwlist
NameError: name 'math' is not defined
>>> math.list
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    math.list
NameError: name 'math' is not defined
>>> mystring='this is a string'
>>> mystring
'this is a string'
>>> mystring="this is a string"
>>> mystring
'this is a string'
>>> print(mystring)
this is a string
>>> mystrings='''hello
this is Jeon
how are you?
'''
>>> mystring
'this is a string'
>>> mystrings
'hello\nthis is Jeon\nhow are you?\n'
>>> print(mystrings)
hello
this is Jeon
how are you?

>>> print(mystring.title())
This Is A String
>>> print(mystring)
this is a string
>>> print(mystring.upper())
THIS IS A STRING
>>> print(mystring.lower())
this is a string
>>> upper_mystring=mystring.upper()
>>> print(upper_mystring)
THIS IS A STRING
>>> calendar.month(2018, 7)
'     July 2018\nMo Tu We Th Fr Sa Su\n                   1\n 2  3  4  5  6  7  8\n 9 10 11 12 13 14 15\n16 17 18 19 20 21 22\n23 24 25 26 27 28 29\n30 31\n'
>>> print(calendar.month(2018, 7))
     July 2018
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30 31

>>> print(upper_mystring.lower())
this is a string
>>> print(mystring+", python is good")
this is a string, python is good
>>> new_string=mystring+", python is good"
>>> print(new_string)
this is a string, python is good
>>> number=10
>>> print(number)
10
>>> number
10
>>> print("number="+str(number))
number=10
>>> mystring*2
'this is a stringthis is a string'
>>> lang=' python  '
>>> lang
' python  '
>>> lang.lstrip()
'python  '
>>> lang.rstrip()
' python'
>>> lang.strip()
'python'
>>> lang=' py thon  '
>>> lang.strip()
'py thon'
>>> num1=10
>>> num2=20
>>> num1+num2
30
>>> num1*num2
200
>>> num1**num2
100000000000000000000
>>> num1?num2
SyntaxError: invalid syntax
>>> num1/num2
0.5
>>> num1%num2
10
>>> num1>num2
False
>>> num1==num2
False
>>> num1<num2 and num1!=0
True
>>> num1<num2 and not num1!=0
False
>>> fruits=['apple','banana
	    
SyntaxError: EOL while scanning string literal
>>> fruits=['apple','banana','mango']
	    
>>> fruits.index(1)
	    
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    fruits.index(1)
ValueError: 1 is not in list
>>> fruits.index(mango)
	    
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    fruits.index(mango)
NameError: name 'mango' is not defined
>>> fruits.index('mango')
	    
2
>>> test
	    
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    test
NameError: name 'test' is not defined
>>> fruits[0]
	    
'apple'
>>> fruits[-1]
	    
'mango'
>>> fruits[-2]
	    
'banana'
>>> print('I like "+fruits[0])
	  
SyntaxError: EOL while scanning string literal
>>> print('I like "+fruits[0]')
	  
I like "+fruits[0]
>>> print('I like "+fruits[0])
	  
SyntaxError: EOL while scanning string literal
>>> print('I like '+fruits[0])
	  
I like apple
>>> print('I like '+fruits[0].title())
	  
I like Apple
>>> fruits.append('melon')
	  
>>> fruits
	  
['apple', 'banana', 'mango', 'melon']
>>> fruits.insert(0,'strawberry')
	  
>>> fruits
	  
['strawberry', 'apple', 'banana', 'mango', 'melon']
>>> del fruits[1]
	  
>>> fruits
	  
['strawberry', 'banana', 'mango', 'melon']
>>> fruits.pop()
	  
'melon'
>>> fruits
	  
['strawberry', 'banana', 'mango']
>>> fruits.remove('banana')
	  
>>> fruits
	  
['strawberry', 'mango']
>>> fruits.append('apple')
	  
>>> fruits.insert(1,'orange')
	  
>>> 
	  
>>> fruits
	  
['strawberry', 'orange', 'mango', 'apple']
>>> fruits.sort()
	  
>>> fruits
	  
['apple', 'mango', 'orange', 'strawberry']
>>> fruits(reverse=True)
	  
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    fruits(reverse=True)
TypeError: 'list' object is not callable
>>> fruits.sort(reverse=True)
	  
>>> fruits
	  
['strawberry', 'orange', 'mango', 'apple']
>>> sorted(fruits)
	  
['apple', 'mango', 'orange', 'strawberry']
>>> len(fruits)
	  
4
>>> len('test')
	  
4
>>> len(mystrings)
	  
32
>>> len('  ')
	  
2
>>> 
======== RESTART: C:/Users/512-11/Desktop/Python_src_Jeon/for_list.py ========
My Last Name is Kim
My Last Name is Lee
My Last Name is Park
My Last Name is Shin
The End...
>>> 
==== RESTART: C:/Users/512-11/Desktop/Python_src_Jeon/for_number_list.py ====
10
20
45
76
68
>>> 
==== RESTART: C:/Users/512-11/Desktop/Python_src_Jeon/for_number_list.py ====
10
20
45
76
68
>>> 
==== RESTART: C:/Users/512-11/Desktop/Python_src_Jeon/for_number_list.py ====
10
20
45
76
68
>>> 
==== RESTART: C:/Users/512-11/Desktop/Python_src_Jeon/for_number_list.py ====
1
2
3
4
5
6
7
8
9
10
>>> 
==== RESTART: C:/Users/512-11/Desktop/Python_src_Jeon/for_number_list.py ====
1
2
3
4
5
6
7
8
9
10
11
>>> 
==== RESTART: C:/Users/512-11/Desktop/Python_src_Jeon/for_number_list.py ====
1
3
5
7
9
11
>>> range(1,5)
	  
range(1, 5)
>>> print(range(1,5))
	  
range(1, 5)
>>> list(range(1,5))
	  
[1, 2, 3, 4]
>>> 
