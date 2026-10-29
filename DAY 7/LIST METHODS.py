Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'''
STRING TESTING METHODS
''''
SyntaxError: unterminated string literal (detected at line 3)
s = 'python programing'
s.startswith('p')
True
s.startswith('o')
False
s.startswith('pyt')
True
s.endsswith('ing')
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.endsswith('ing')
AttributeError: 'str' object has no attribute 'endsswith'. Did you mean: 'endswith'?
s.endswith('ing')
True
s.endswith('g')
True
's'islower()
SyntaxError: invalid syntax
's'.islower()
True
'u'.isupper()
False
'code@'.isalpha()
False
'code'.isalpha()
True
'code1123'.isalnum()
True
'code1123@'.isalnum()
False
'code'.isalnum()
True
''.isspace()
False
' '.isspace()
True
'   code'isspace()
SyntaxError: invalid syntax
'   code'.isspace()
False
'myval'.isidentifier()
True
s
'python programing'
s.istitle()
False
t = 'Code'
t
'Code'
s.istitle()
False
t.istitle()
True
'1234'.isdecimal()
True
'1234'.isdigit()
True
'0.2112'isdigit()
SyntaxError: invalid syntax
'0.2112'.isdigit()
False
'0.2112'.isdecimal()
False
'''-----------------------------------------------------------------------------------------------'''
'-----------------------------------------------------------------------------------------------'
'a b c d'.split()
['a', 'b', 'c', 'd']
'a,b,c,d'.split()
['a,b,c,d']
'a,b,c,d'.split(',')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']

'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
s="""
hello
world
python
"""
s
'\nhello\nworld\npython\n'
s.splitlines()
['', 'hello', 'world', 'python']
l = ['a','b','c']

'-'.join(l)
'a-b-c'
'@'.join(l)
'a@b@c'
'$'.join(l)
'a$b$c'
''join(l)
SyntaxError: invalid syntax

''.join(l)
'abc'
'''join is used to convert the list to string'''
'join is used to convert the list to string'
s = 'a-b-c-d'
s
'a-b-c-d'
s.partition('b')
('a-', 'b', '-c-d')
'python.py'.partition('.')
('python', '.', 'py')
'python.py'.rpartition('.')
('python', '.', 'py')
'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
s = "Café"
s.encode()
b'Caf\xc3\xa9'

b'Caf\xc3\xa9'.decode()
'Café'
'''---------------------------------------------------------------------------------------'''
'---------------------------------------------------------------------------------------'
'''list '''
'list '
l=[]
l=list()
l=[1,2,3]
l=list([11,2,3,4])
l
[11, 2, 3, 4]
type(l)
<class 'list'>
#list is mutable and ordered and hetorogenous and dynamic in nature
l =[1,1,1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['

l =[1,1,1,1,1]
l
[1, 1, 1, 1, 1]
#---------------------------------------------#LISTMETHODS-----------------------------------------------------
[1,2,3]+[4,3,5]
[1, 2, 3, 4, 3, 5]
[1,2,3]*5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l=['python','java','c','mysql','flask','fastapi','aws']
l[o]
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    l[o]
NameError: name 'o' is not defined
l[0]
'python'
l[1]
'java'
l[2]
'c'
l[3]
'mysql'
l[4]
'flask'
l[5]
'fastapi'
l[66]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    l[66]
IndexError: list index out of range
l[-2]
'fastapi'
l[-1]
'aws'
#---------------------slicling-----------------------
ll
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    ll
NameError: name 'll' is not defined. Did you mean: 'l'?
l
['python', 'java', 'c', 'mysql', 'flask', 'fastapi', 'aws']
l[:3]
['python', 'java', 'c']

l[:-3]
['python', 'java', 'c', 'mysql']
l[-3:0]
[]
l[2:5]
['c', 'mysql', 'flask']

l[1::2]
['java', 'mysql', 'fastapi']

l[::-2]
['aws', 'flask', 'c', 'python']

l[-3:-6]
[]
l[-3:-6:1]
[]
l[-3:-6:-1]
['flask', 'mysql', 'c']
l
['python', 'java', 'c', 'mysql', 'flask', 'fastapi', 'aws']
'c'in l
True
'python' in ll
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    'python' in ll
NameError: name 'll' is not defined. Did you mean: 'l'?
'python' in l
True
#----------list Methods------------------------------------------

l
['python', 'java', 'c', 'mysql', 'flask', 'fastapi', 'aws']
len(l)
7
sorted(l)
['aws', 'c', 'fastapi', 'flask', 'java', 'mysql', 'python']
max(l)
'python'
min(l)
'aws'
#max is for max characters,miin is for min charectors
#list is the mutable data type it means we can add or del in the same memory location
l
['python', 'java', 'c', 'mysql', 'flask', 'fastapi', 'aws']
id(l)
2801199843072
s = ['c++','docker']
s
['c++', 'docker']
l[1]=s[2]
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    l[1]=s[2]
IndexError: list index out of range
l[3]=s[1]
l
['python', 'java', 'c', 'docker', 'flask', 'fastapi', 'aws']
l[2]=c++
SyntaxError: invalid syntax
>>> l[2]='c++'
>>> l
['python', 'java', 'c++', 'docker', 'flask', 'fastapi', 'aws']
>>> l[3]='mysql'
>>> l
['python', 'java', 'c++', 'mysql', 'flask', 'fastapi', 'aws']
>>> l.appened(1,2,3)
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    l.appened(1,2,3)
AttributeError: 'list' object has no attribute 'appened'. Did you mean: 'append'?
>>> l.append(2,3,4)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    l.append(2,3,4)
TypeError: list.append() takes exactly one argument (3 given)
>>> l
['python', 'java', 'c++', 'mysql', 'flask', 'fastapi', 'aws']
>>> #append is used to add an element and th end of the list
>>> l.append('b')
>>> l.append('b')
... 
>>> l.append('c')
>>> l
['python', 'java', 'c++', 'mysql', 'flask', 'fastapi', 'aws', 'b', 'b', 'c']
>>> #extend iis used to add multiple elements at the end of the list
>>> l.extend(1,2,3)
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    l.extend(1,2,3)
TypeError: list.extend() takes exactly one argument (3 given)
>>> l.extend([1,2,3])
>>> l
['python', 'java', 'c++', 'mysql', 'flask', 'fastapi', 'aws', 'b', 'b', 'c', 1, 2, 3]
>>> #insert is used to add the element at particular index
>>> l
['python', 'java', 'c++', 'mysql', 'flask', 'fastapi', 'aws', 'b', 'b', 'c', 1, 2, 3]
>>> linsert(2,'c')
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    linsert(2,'c')
NameError: name 'linsert' is not defined
>>> l.insert(2,'c')
>>> l
['python', 'java', 'c', 'c++', 'mysql', 'flask', 'fastapi', 'aws', 'b', 'b', 'c', 1, 2, 3]
