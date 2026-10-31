Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = ["23,54,5,6,2,6,34,24"]
>>> l
['23,54,5,6,2,6,34,24']
>>> l.extend(76,87,5,36,7,35,)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l.extend(76,87,5,36,7,35,)
TypeError: list.extend() takes exactly one argument (6 given)
>>>  l.extend("76,87,5,36,7,35")
 
SyntaxError: unexpected indent
>>> l.extend("76,87,5,36,7,35")
>>> l
['23,54,5,6,2,6,34,24', '7', '6', ',', '8', '7', ',', '5', ',', '3', '6', ',', '7', ',', '3', '5']
>>>  l.extend(76,87,5,36,7,35)
 
SyntaxError: unexpected indent
>>> l.extend(76,87,5,36,7,35)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    l.extend(76,87,5,36,7,35)
TypeError: list.extend() takes exactly one argument (6 given)
>>> l = ["12,23,13,134,64,656,75,44,53,245,657,57"]
>>> l
['12,23,13,134,64,656,75,44,53,245,657,57']
>>> l.pop()
'12,23,13,134,64,656,75,44,53,245,657,57'
>>> l
[]
>>> l = [12,23,13,134,64,656,75,44,53,245,657,57]
>>> l
[12, 23, 13, 134, 64, 656, 75, 44, 53, 245, 657, 57]
>>> l.pop()
57
>>> l
[12, 23, 13, 134, 64, 656, 75, 44, 53, 245, 657]
>>> l.pop(5)
656
>>> l.remove(134)
>>> l
[12, 23, 13, 64, 75, 44, 53, 245, 657]
>>> del l(3)
SyntaxError: cannot delete function call
>>> del l(3)
SyntaxError: cannot delete function call
>>> l
[12, 23, 13, 64, 75, 44, 53, 245, 657]
>>> del l (3)
SyntaxError: cannot delete function call
>>> [12, 23, 13, 64, 75, 44, 53, 245, 657][12, 23, 13, 64, 75, 44, 53, 245, 657]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    [12, 23, 13, 64, 75, 44, 53, 245, 657][12, 23, 13, 64, 75, 44, 53, 245, 657]
TypeError: list indices must be integers or slices, not tuple

>>> l.clear()
>>> l
[]
>>> # shallow copy and deep copy
>>> l = [23,42,53,23,53,68,56,887,789,35]
>>> l
[23, 42, 53, 23, 53, 68, 56, 887, 789, 35]
>>> l.count(53)
2
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    l.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> l,index(68)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l,index(68)
NameError: name 'index' is not defined
>>> l.index(68)
5
>>> sorted(l)
[23, 23, 35, 42, 53, 53, 56, 68, 789, 887]
>>> l.reverse()
>>> l
[35, 789, 887, 56, 68, 53, 23, 53, 42, 23]
>>> l.sort(reverse = True)
>>> l
[887, 789, 68, 56, 53, 53, 42, 35, 23, 23]
>>> a =[1,2,3]
>>> a
[1, 2, 3]
>>> c  = a
>>> c
[1, 2, 3]
>>> c.append(12)
>>> a
[1, 2, 3, 12]
>>> c
[1, 2, 3, 12]
>>> a.append(11)
>>> a
[1, 2, 3, 12, 11]
>>> c
[1, 2, 3, 12, 11]
>>> a is c
True
>>> b.copy(a)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    b.copy(a)
NameError: name 'b' is not defined
>>> b = a.copy()
>>> b
[1, 2, 3, 12, 11]\
>>> b.append(14)
>>> b
[1, 2, 3, 12, 11, 14]
>>> a
[1, 2, 3, 12, 11]
>>> l
[887, 789, 68, 56, 53, 53, 42, 35, 23, 23]
>>> any(l)
True
>>> all(l)
True
>>> l.append(0)
>>> l
[887, 789, 68, 56, 53, 53, 42, 35, 23, 23, 0]
>>> any(l)
True
>>> all(l)
False
>>> k = [0,0.0,' ']
>>> k
[0, 0.0, ' ']
>>> any(k)
True
>>> k = (0,0.0,'')
>>> k
(0, 0.0, '')
>>> any(k)
False
>>> all(k)
False
>>> k.append(12)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    k.append(12)
AttributeError: 'tuple' object has no attribute 'append'
>>> k.append(12)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    k.append(12)
AttributeError: 'tuple' object has no attribute 'append'
>>> k.append[12]
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    k.append[12]
AttributeError: 'tuple' object has no attribute 'append'
>>> k = [0,12,3,0]
>>> k
[0, 12, 3, 0]
>>> type(k)
<class 'list'>
>>> k
[0, 12, 3, 0]
>>> any(k)
True
>>> all(k)
False
>>> l
[887, 789, 68, 56, 53, 53, 42, 35, 23, 23, 0]
>>> sum(l)
2029
>>> # immu , ordered,duplicates,hetrogenous,fix
>>> t = ()
>>> type(t)
<class 'tuple'>
>>> t = (1,2,34,5)
>>> t = tuple((1,2,3,4,5))
>>> t
(1, 2, 3, 4, 5)
>>> type(t)
<class 'tuple'>
>>> t = 1,2,3,4,5
>>> t
(1, 2, 3, 4, 5)
>>> t =(6)
>>> t
6
>>> t = (6,)
>>> t
(6,)
>>> t = (1,2,3,4,5)
>>> t
(1, 2, 3, 4, 5)
>>> type(t)
<class 'tuple'>
>>> a,b,c,d,e = (t)
>>> a
1
>>> b
2
>>> c
3
>>> d
4
>>> e
5
>>> t = t = (1,1.2,'gpraveen',[1,2,3,4,5],{1,2,3,4})
>>> t
(1, 1.2, 'gpraveen', [1, 2, 3, 4, 5], {1, 2, 3, 4})
>>> len(3)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    len(3)
TypeError: object of type 'int' has no len()
>>> len[3]
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    len[3]
TypeError: 'builtin_function_or_method' object is not subscriptable
\
>>> 
>>> 
>>> a= (1,2,3,4)
>>> b= (3,4,5,6)
>>> a + b
(1, 2, 3, 4, 3, 4, 5, 6)
>>> a*2
(1, 2, 3, 4, 1, 2, 3, 4)
>>> a
(1, 2, 3, 4)
>>> t
(1, 1.2, 'gpraveen', [1, 2, 3, 4, 5], {1, 2, 3, 4})
>>> t[2]
'gpraveen'
>>> t[-1]
{1, 2, 3, 4}
>>> t[ ::-1]
({1, 2, 3, 4}, [1, 2, 3, 4, 5], 'gpraveen', 1.2, 1)
>>> t
(1, 1.2, 'gpraveen', [1, 2, 3, 4, 5], {1, 2, 3, 4})
>>> t[1:3]
(1.2, 'gpraveen')
>>> t[0: :2]
(1, 'gpraveen', {1, 2, 3, 4})
>>> t
(1, 1.2, 'gpraveen', [1, 2, 3, 4, 5], {1, 2, 3, 4})
>>> 1 in t
True
>>> 0 in t
False
>>> True not in t
False
>>> l = (1,2,3,4,5,6,7,8,9,10,11,12,13)
>>> type(l)
<class 'tuple'>
>>> len(l)
13
>>> sorted(l)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
>>> max(l)
13
>>> min(l)
1
>>> l.count(1)
1
>>> l.index(5)
4
\
>>> l.index(10)
9
>>> l [::-1]
(13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
>>> l[1:11]
(2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
>>> l [4:10]
(5, 6, 7, 8, 9, 10)
>>> sum(l)
91
>>> any(l)
True
>>> all(kl)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    all(kl)
NameError: name 'kl' is not defined
>>> all(0)
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    all(0)
TypeError: 'int' object is not iterable
>>> all(l)
True
>>> l.append(0)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    l.append(0)
AttributeError: 'tuple' object has no attribute 'append'
>>> s = {}
>>> type(s)
<class 'dict'>
>>> s = set()
>>> type(S)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined
>>> type(s)
<class 'set'>
>>> s= {1,2,3,4,5}
>>> type(s)
<class 'set'>
>>> s
{1, 2, 3, 4, 5}
>>> # unorderd,unique,mutable,not allow duplicates, hetrogenous(with conditons.dynamic)
>>> s = {90,78,56,84,1,1,43,898}
>>> type*( l = ["12,23,13,134,64,656,75,44,53,245,657,57"] l = ["12,23,13,134,64,656,75,44,53,2
							    
SyntaxError: invalid syntax
>>> type(s\)
     
SyntaxError: unexpected character after line continuation character
>>> type(s)
<class 'set'>
>>> s
{1, 898, 84, 56, 90, 43, 78}
>>> s.add(2)
>>> s
{1, 898, 2, 84, 56, 90, 43, 78}
>>> s.add(2.2)
>>> s
{1, 898, 2, 2.2, 78, 84, 90, 43, 56}
>>> s.(2+3j)
SyntaxError: invalid syntax
>>> s.add(2+3j)
>>> s
{1, 898, 2, 2.2, (2+3j), 78, 84, 90, 43, 56}
>>> s.add("str")
>>> s
{1, 898, 2, 2.2, (2+3j), 78, 84, 90, 'str', 43, 56}
>>> s.add((1,2,3))
>>> s
{1, 898, 2, 2.2, (2+3j), 78, 84, 90, 'str', 43, (1, 2, 3), 56}
>>> s.add(True)
>>> s
{1, 898, 2, 2.2, (2+3j), 78, 84, 90, 'str', 43, (1, 2, 3), 56}
>>> s
{1, 898, 2, 2.2, (2+3j), 78, 84, 90, 'str', 43, (1, 2, 3), 56}
>>> s.add(False)
>>> s
{False, 1, 898, 2, 2.2, (2+3j), 78, 84, 90, 'str', 43, (1, 2, 3), 56}
>>> # in cannot add dic ,set
>>> a = {8,1,4,6}
>>> b = {4,5,6,7,8,9}
>>> 4 in a
True
>>> 7 not in a
True
>>> a
{8, 1, 4, 6}
>>> b
{4, 5, 6, 7, 8, 9}
>>> a | b
{1, 4, 5, 6, 7, 8, 9}
>>> a & b
{8, 4, 6}
>>> a- b
{1}
>>> 5.subset(a)
SyntaxError: invalid syntax
>>> a.isdijoint(b)
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    a.isdijoint(b)
AttributeError: 'set' object has no attribute 'isdijoint'
>>> a.isdisjoint(b)
False
>>> a ^ b
{1, 5, 7, 9}
>>> a.issubset(b)
False
>>> {8} .issubset(a)
True
>>> {100,99}.issubject(a)
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    {100,99}.issubject(a)
AttributeError: 'set' object has no attribute 'issubject'
>>> {100,99}.issubset(a)
False
>>> {1,2,3,4,5,6,7,8,9,10}.issuperset(a)
True
>>> 