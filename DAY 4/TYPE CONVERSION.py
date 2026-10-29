TYPE CONVERSTIONS


Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 112
a
112
float(a)
112.0
complex(a)
(112+0j)
str(a)
'112'

list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True

a = 12.3
int(a)
12
complex(a)
(12.3+0j)
str(a)
'12.3'
list(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(a)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(a)
TypeError: 'float' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(a)
TypeError: 'float' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(a)
TypeError: 'float' object is not iterable
bool(a)
True


a = 1+17j
a
(1+17j)
type(a)
<class 'complex'>
int(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
str(a)
'(1+17j)'
list(a)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list(a)
TypeError: 'complex' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tuple(a)
TypeError: 'complex' object is not iterable

set(a)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    set(a)
TypeError: 'complex' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    dict(a)
TypeError: 'complex' object is not iterable
bool(a)
True


s = "eswar"
int(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'eswar'
d = "000111"
int(d)
111
float(s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'eswar'
float(d)
111.0
complex(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
complex(d)
(111+0j)
list(s)
['e', 's', 'w', 'a', 'r']
list(d)
['0', '0', '0', '1', '1', '1']
tuple(s)
('e', 's', 'w', 'a', 'r')
set(s)
{'e', 'a', 's', 'r', 'w'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True


list = [1,2,3,4,5]

int(list)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    int(list)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(list)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    float(list)
TypeError: float() argument must be a string or a real number, not 'list'
complex(list)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    complex(list)
TypeError: complex() first argument must be a string or a number, not 'list'
str(list)
'[1, 2, 3, 4, 5]'
set(list)
{1, 2, 3, 4, 5}
tuple(list)
(1, 2, 3, 4, 5)
bool(list)
True



tuple = (1,2,3,4)

int(tuple)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int(tuple)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
list(tuple)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    list(tuple)
TypeError: 'list' object is not callable
str(tuple)
'(1, 2, 3, 4)'
set(tuple)
{1, 2, 3, 4}
list(tuple)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    list(tuple)
TypeError: 'list' object is not callable
dict(tuple)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    dict(tuple)
TypeError: cannot convert dictionary update sequence element #0 to a sequence


bool(tuple)
True
c = (1,2,3,4)
tuple(c)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    tuple(c)
TypeError: 'tuple' object is not callable
list(c)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    list(c)
TypeError: 'list' object is not callable


c = (1, 2, 3, 4)
print(tuple(c))
print(list(c))
SyntaxError: multiple statements found while compiling a single statement


set = {1122,22,2,3}
type(set)
<class 'set'>


------------------------------------------------------------------------------

int - flo,com,str,boo
float - int,com,str,bool
com - str,bool
str - all expect dic
list - str,tuple,set,bool
tuple - same as above
set - same as above
dic - str,list,tuple,set,bool
bol-int,float,complex

