Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    s
NameError: name 's' is not defined
s = 'pyhton'
s
'pyhton'
p = ''
p
''
s
'pyhton'
t = 'programming'
s+t
'pyhtonprogramming'
t*3
'programmingprogrammingprogramming'
s*7
'pyhtonpyhtonpyhtonpyhtonpyhtonpyhtonpyhton'
'x'*3
'xxx'
c83
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    c83
NameError: name 'c83' is not defined
c*8
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    c*8
NameError: name 'c' is not defined
'o'+s+p*3
'opyhton'
'o'+s+t*3
'opyhtonprogrammingprogrammingprogramming'
s = 'sankarayougisrivasteswar'
a
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a
NameError: name 'a' is not defined
s
'sankarayougisrivasteswar'
s[0]
's'
s[1]
'a'
s[12]
's'
s[-12]
's'
s[13]
'r'

s[23]
'r'

s[-1]
'r'
s[-2]
'a'

s[0:-2]
'sankarayougisrivastesw'
s[1:0}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s[1:0]
''
s[1::-2}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
s[1::-2]
'a'
'''
SLICING
-------
S[START VALLUE : END VALUE:STEP]
'''
'\nSLICING\n-------\nS[START VALLUE : END VALUE:STEP]\n'
s = 'python java flask'
s
'python java flask'
s[0:6}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['

s[0:6]
'python'
s[6:10]
' jav'
s[6;11]
SyntaxError: invalid syntax
s[6:11]
' java'
s[5:0]
''
s[5:0:-1]
'nohty'

s[6:0:-1]
' nohty'
s[6:-1:-1]
''
s[6:0:-2]
' ot'
s[6::-1]
' nohtyp'
s[::-2]
'kafaa otp'
s[::1]
'python java flask'
'''MEMBERSHIP '''
'MEMBERSHIP '
s
'python java flask'
'pyhton' in s
False
'python' in s
True
'java' in s
True
'flask' in s
True
'c++' not in s
True
'java' not in s
False
len(s)
17
'''
ascii value and char'''
'\nascii value and char'
ord a
SyntaxError: invalid syntax
ord ('a')
97
ord('a')
97
ord ( )
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    ord ( )
TypeError: ord() takes exactly one argument (0 given)
ord(' ')
32
ord('+')
43
char(10)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    char(10)
NameError: name 'char' is not defined. Did you mean: 'chr'?
char('110')
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    char('110')
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(10)
'\n'
chr(22)
'\x16'
chr(110)
'n'
chr(97)
'a'
chr(65)
'A'
s
'python java flask'
min(s)
' '
sorted(s)
[' ', ' ', 'a', 'a', 'a', 'f', 'h', 'j', 'k', 'l', 'n', 'o', 'p', 's', 't', 'v', 'y']
s
'python java flask'
s.upper
<built-in method upper of str object at 0x00000148B18C2830>
s.upper()
'PYTHON JAVA FLASK'
s.lower()
'python java flask'
s.swapcase()
'PYTHON JAVA FLASK'
s.title()
'Python Java Flask'
s.capitilize()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.capitilize()
AttributeError: 'str' object has no attribute 'capitilize'. Did you mean: 'capitalize'?
s.capitalize()
'Python java flask'
txt = "Hello, And Welcome To My World!"
txt.casefold()
'hello, and welcome to my world!'
s.center(40,'-')
'-----------python java flask------------'
s.center(40,'***')
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s.center(40,'***')
TypeError: The fill character must be exactly one character long
s.center(40,'#')
'###########python java flask############'
s.ljust(40,'{')
'python java flask{{{{{{{{{{{{{{{{{{{{{{{'
s.rjust(40,'{')
'{{{{{{{{{{{{{{{{{{{{{{{python java flask'
1
1
000
0
0001
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
'1'zfill(5)
SyntaxError: invalid syntax
'1'.zfill(5)
'00001'

''' FINDING METHODS'''
' FINDING METHODS'
S
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    S
NameError: name 'S' is not defined. Did you mean: 's'?
s
'python java flask'
s.find('y')
1
s.find('z')
-1
s.find('a')
8
s.rfind('a')
14
s.index('a')
8

s.rindex('a')
14
s.lindex('a')
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    s.lindex('a')
AttributeError: 'str' object has no attribute 'lindex'. Did you mean: 'index'?
>>> s.count('a')
3
>>> s.count('p')
1
>>> s.count('z')
0
>>> s.count('e')
0
>>> s.count('h')
1
>>> '''
... strip operation'''
'\nstrip operation'
>>> '''it is used to remove the spaces from starting and end '''
'it is used to remove the spaces from starting and end '
>>> p = '        code karo mera     bhaai     '
>>> p
'        code karo mera     bhaai     '

>>> s.strip()
'python java flask'
>>> p.strip()
'code karo mera     bhaai'
>>> s.rstrip()
'python java flask'
>>> p.rstrip()
'        code karo mera     bhaai'
>>> p.lstrip()
'code karo mera     bhaai     '
>>> 'code karo mera     bhaai     '
'code karo mera     bhaai     '
>>> '''REPLACE AND TRANSLAT FUCTIONS'''
'REPLACE AND TRANSLAT FUCTIONS'
>>> 
>>> s
'python java flask'
>>> s.replace('p','l')
'lython java flask'

>>> s.maketrans('apkqs','12345')
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
>>> s.translate(s.maketrans('apkqs','12345'))
'2ython j1v1 fl153'
