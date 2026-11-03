This are the numeric data types
a = 2
type(a)
<class 'int'>
b = 3.22
type(b)
<class 'float'>

c = 2+6j

c
(2+6j)

type(c)
<class 'complex'>

SEQUENCEAL DATA TYPES

STRING - It is the collection of char 
S = "Codegnan"
type(s)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    type(s)
NameError: name 's' is not defined. Did you mean: 'S'?
type(S)
<class 'str'>

-------------------------------------


l = [1,2,3,4]
l
[1, 2, 3, 4]
type(l)
<class 'list'>


l = [1,2.3,"code",2+3j]

l
[1, 2.3, 'code', (2+3j)]

id(l)
1626312840000
l
[1, 2.3, 'code', (2+3j)]
l.append(12)
l
[1, 2.3, 'code', (2+3j), 12]
l(id)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l(id)
TypeError: 'list' object is not callable
id(l)
1626312840000


l.update(12)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    l.update(12)
AttributeError: 'list' object has no attribute 'update'
l.pop(12)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    l.pop(12)
IndexError: pop index out of range
l.pop(3)
(2+3j)
l
[1, 2.3, 'code', 12]

-----------------------------------------------------
t = (1,2,3,4)
type(t)
<class 'tuple'>
t.append(1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    t.append(1)
AttributeError: 'tuple' object has no attribute 'append'
t.pop(2)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    t.pop(2)
AttributeError: 'tuple' object has no attribute 'pop'
t = (1,22,33)
t
(1, 22, 33)

-------------------------------------------------------
set = {2,23,34,34.4}
unodered,mutable
set
{34.4, 2, 34, 23}
type(set)
<class 'set'>
set = {2,2,2,2}
set
{2}


-----------------------------------------------------------
d = {name:"sunny" , age:"22" , num:9052521}
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d = {name:"sunny" , age:"22" , num:9052521}
NameError: name 'name' is not defined
NameError: name 'name' is not defined
SyntaxError: invalid syntax
d = {"name":"sunny" , "age":22 , "num" : 902227374}
d
{'name': 'sunny', 'age': 22, 'num': 902227374}
d(name)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    d(name)
NameError: name 'name' is not defined
d("name")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    d("name")
TypeError: 'dict' object is not callable

------------------------------------------------------------

