Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1myvar = 100
SyntaxError: invalid decimal literal
>>> a= 0
>>> a,b,c = 10
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a,b,c = 10
TypeError: cannot unpack non-iterable int object
>>> clear
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> del shell
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    del shell
NameError: name 'shell' is not defined. Did you mean: 'help'?
>>> a = 10
>>> b = 20
>>> a=b=c=20
>>> a
20
>>> b
20
>>> c
20
>>> a,b,c = 10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b = b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a
NameError: name 'a' is not defined
