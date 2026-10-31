Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 31-10-2026
>>> s= {1,23,45,45,64,34,56,36,75,23,32}
>>> s
{64, 1, 34, 32, 36, 75, 45, 23, 56}
>>> s
{64, 1, 34, 32, 36, 75, 45, 23, 56}
>>> s
{64, 1, 34, 32, 36, 75, 45, 23, 56}
s
>>> 
>>> s
{64, 1, 34, 32, 36, 75, 45, 23, 56}
>>> sorted(s)
[1, 23, 32, 34, 36, 45, 56, 64, 75]
>>> len(s)
9
>>> sum(s)
366
>>> any(s)
True
>>> all(s)
True
>>> max(s)
75
>>> min(s)
1
>>> s
{64, 1, 34, 32, 36, 75, 45, 23, 56}
>>> s.pop(34)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.pop(34)
TypeError: set.pop() takes no arguments (1 given)
>>> s.append(2)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.append(2)
AttributeError: 'set' object has no attribute 'append'
>>> s.add(26)
>>> s
{64, 1, 34, 32, 36, 75, 45, 23, 56, 26}
>>> s.update({10,20,30})
>>> s
{64, 1, 34, 32, 36, 10, 75, 45, 20, 23, 56, 26, 30}
>>> s.pop()
64
>>> s
{1, 34, 32, 36, 10, 75, 45, 20, 23, 56, 26, 30}
>>> s.remove(30)
>>> s
{1, 34, 32, 36, 10, 75, 45, 20, 23, 56, 26}
>>> s.remove(32)
>>> a
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> s
{1, 34, 36, 10, 75, 45, 20, 23, 56, 26}
>>> s.discard(10)
>>> s
{1, 34, 36, 75, 45, 20, 23, 56, 26}
>>> s.remove(10)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    s.remove(10)
KeyError: 10
>>> s.discard(20)
>>> s
{1, 34, 36, 75, 45, 23, 56, 26}
>>> s.clear()
>>> s
set()
>>> s
set()
>>> s
set()
s
>>> 
>>> s
set()
>>> 4
4
>>> a ={21,31,41,51,22,33,}
>>> b = a
>>> a
{33, 51, 21, 22, 41, 31}
>>> b
{33, 51, 21, 22, 41, 31}
>>> b.add(0)
>>> a
{0, 33, 51, 21, 22, 41, 31}
>>> b
{0, 33, 51, 21, 22, 41, 31}
>>> c.copy(a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    c.copy(a)
NameError: name 'c' is not defined
>>> c = a.copy()
>>> c
{0, 33, 51, 21, 22, 41, 31}
>>> c.add(12)
>>> c
{0, 33, 51, 21, 22, 41, 12, 31}
>>> a
{0, 33, 51, 21, 22, 41, 31}
>>> s
set()
>>> # dixtionary
>>> d = ()
>>> type(b)
<class 'set'>
>>> d = {}
>>> type(b)
<class 'set'>
>>> d = {1:2,2:3}
>>> type(d)
<class 'dict'>
>>> # mut dyn ord het,uk
>>> d
{1: 2, 2: 3}
>>> d ={ }
>>> d[1] = 'int'
>>> d
{1: 'int'}
>>> d[1.1] = 'float'
>>> d
{1: 'int', 1.1: 'float'}
>>> d['str'] = 'str'
>>> d
{1: 'int', 1.1: 'float', 'str': 'str'}
>>> d[2+2j] = ''
>>> d[2+2j] = 'complex'
>>> d
{1: 'int', 1.1: 'float', 'str': 'str', (2+2j): 'complex'}
>>> d[False] = '
SyntaxError: EOL while scanning string literal
>>> d[False] = 'bool'
>>> d
{1: 'int', 1.1: 'float', 'str': 'str', (2+2j): 'complex', False: 'bool'}
>>> d[1,2,3,4] = 'lis'
>>> d
{1: 'int', 1.1: 'float', 'str': 'str', (2+2j): 'complex', False: 'bool', (1, 2, 3, 4): 'lis'}
>>> d[{1:2,2:3}] = 'dict'
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    d[{1:2,2:3}] = 'dict'
TypeError: unhashable type: 'dict'
>>> d.clear()
>>> d
{}
>>> d[1] = 1
>>> d[2] = 2.1
>>> d[3] = 23+3j
>>> d[4] = 'str'
>>> d[5] = [1,2]
>>> d[6] = (1,2)
>>> d[7] = {1,2}
>>> d[8] = {1:2,2:3}
>>> d[9] = False
>>> d
{1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False}
>>> {1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False}d.get
SyntaxError: invalid syntax
>>> 
>>> d[2]
2.1
>>> d[8]
{1: 2, 2: 3}
>>> d
{1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False}
>>> d.get(12)
>>> d
{1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False}
>>> d.get(8)
{1: 2, 2: 3}
>>> d
{1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False}
>>> d.get(18,'Key is not there')
'Key is not there'
>>> 'str' in d
False
>>> 1 in d
True
>>> [1,2] in d
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    [1,2] in d
TypeError: unhashable type: 'list'
>>> 2.1
2.1
>>> [2.1] in d
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    [2.1] in d
TypeError: unhashable type: 'list'
>>> 9 in d
True
>>> d
{1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False}
>>> # modification, update
>>> d[5] = 25
>>> d
{1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: 25, 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False}
>>> d[12] = 20
>>> d
{1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: 25, 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False, 12: 20}
>>> d[11] = 100
>>> d[12] = 200
>>> d
{1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: 25, 6: (1, 2), 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False, 12: 200, 11: 100}
>>> d.update({15:500,`6:600})
SyntaxError: invalid syntax
>>> d.update({15:500,6:600})
>>> d
{1: 1, 2: 2.1, 3: (23+3j), 4: 'str', 5: 25, 6: 600, 7: {1, 2}, 8: {1: 2, 2: 3}, 9: False, 12: 200, 11: 100, 15: 500}
>>> d.popitem
<built-in method popitem of dict object at 0x000002D96C534A40>
>>> d.popitem()
(15, 500)
>>> d.popitem()
(11, 100)
>>> d.pop(2)
2.1
>>> d.pop(7)
{1, 2}
>>> d.del(7)
SyntaxError: invalid syntax
>>> del (7)
SyntaxError: cannot delete literal
>>> del d[7]
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    del d[7]
KeyError: 7
>>> d
{1: 1, 3: (23+3j), 4: 'str', 5: 25, 6: 600, 8: {1: 2, 2: 3}, 9: False, 12: 200}
>>> del d[4]
>>> d
{1: 1, 3: (23+3j), 5: 25, 6: 600, 8: {1: 2, 2: 3}, 9: False, 12: 200}
>>> d.clear()
>>> d
{}
>>> type(d)
<class 'dict'>
>>> d
{}
>>> d = {1: 1, 3: (23+3j), 4: 'str', 5: 25, 6: 600, 8: {1: 2, 2: 3}, 9: False, 12: 200}
>>> d
{1: 1, 3: (23+3j), 4: 'str', 5: 25, 6: 600, 8: {1: 2, 2: 3}, 9: False, 12: 200}
>>> d.keys()
dict_keys([1, 3, 4, 5, 6, 8, 9, 12])
>>> d.values()
dict_values([1, (23+3j), 'str', 25, 600, {1: 2, 2: 3}, False, 200])
>>> d.items()
dict_items([(1, 1), (3, (23+3j)), (4, 'str'), (5, 25), (6, 600), (8, {1: 2, 2: 3}), (9, False), (12, 200)])
>>> len(d)
8
>>> min()d
SyntaxError: invalid syntax
>>> min(d)
1
>>> max(d)
12
>>> sorted(d)
[1, 3, 4, 5, 6, 8, 9, 12]
>>> a = {1:1,2:2,3:3}
>>> b = a
>>> a
{1: 1, 2: 2, 3: 3}
>>> b
{1: 1, 2: 2, 3: 3}
>>> c = a.copy()
>>> c
{1: 1, 2: 2, 3: 3}
>>> a
{1: 1, 2: 2, 3: 3}
>>> c[4] = 4
>>> c
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3}
>>> a
{1: 1, 2: 2, 3: 3}
>>> d = dict.fromkeys(['a','b','c','d','e'],0)
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
>>> d.setdefault('a')
0
>>> d.setdefault('h')
>>> 
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None}
d
>>> 
>>> d.setdefault('c',1)
0
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None}
>>> s = frozenset({1,2,3,4,5})
\
>>> s
frozenset({1, 2, 3, 4, 5})
>>> type(s)
<class 'frozenset'>
>>> len(s)
5
>>> min(s)
1
>>> max(s)
5
>>> 