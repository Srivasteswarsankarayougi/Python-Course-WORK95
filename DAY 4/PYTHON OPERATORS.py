OPERATORS
a = 12
b = 112
a+b
124
a-b
-100
a*b
1344
a**b
7384133797593879188991495862550756538467726049485655326421674303972301981707930955969882576921871896160099115453179232256
''' ** refers to power''''
SyntaxError: unterminated string literal (detected at line 1)
''' ** refers to power'''
' ** refers to power'
a/b
0.10714285714285714
a//b
0
9/2
4.5
9//2
4
'''// remmoves the decimal part'''
'// remmoves the decimal part'
9%2
1
'''% it gives the reminder'''
'% it gives the reminder'
a*b
1344
-----------------------------------------------------------------------------------------------
COMPARISION OPERATORS

a=10
b=10
a>b
False
a<b
False

a==b
True
a>=b
True
a<=b
True

a!=b
False

-----------------------------------------------------------------------------------------------------
ASSIGNMENT OPERATORS
b = 12

b +=2
b
14
b -= 2
b
12
b *= 2
b
24
b /= 2
b
12.0
b //=2
b
6.0
b = 122
b //=2
b
61
-----------------------------------------------------------------------------------------------------
LOGICAL OPERATORS
a = 12
b = 23
a%2 == 0 and a>10
True

b%2 == 0 and a>10
False
a%2 == 0 or a>10
True
b%2 == 0 and a>10
False
not a%2 == 0 and a>10
False
not b%2 == 0 and a>10
True
-----------------------------------------------------------------------------------------------------------
''' MEMBERSHIP OPERATORS'''
' MEMBERSHIP OPERATORS'

st list tuple set dict
SyntaxError: invalid syntax
s = 'pyhton'
'p' in s
True
'd' in s
False
'p' not in s
False
'd' not in s
True

list = [1,2,3,4]
'1' in s
False
'1' in list
False

2 in ist
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    2 in ist
NameError: name 'ist' is not defined. Did you mean: 'list'?
2 in list
True
1 in list
True

tuple = (1,2,3,4)
1 in tuple
True
2 in tuple
True


set = {1,2,3,4}
1 in set
True


dict = {1:11,2:22,3:33}
1 in dict
True
22 in dict
False
''' it only find the keyword'''
' it only find the keyword'
----------------------------------------------------------------------------------------------------------------------------------

'''identity operators'''
'identity operators'
''' IT cheac for the memeory alloacation if the memeory allocation is same it wil return true'''
' IT cheac for the memeory alloacation if the memeory allocation is same it wil return true'
l = [1,2,34,56]
m = [1,2,34,56]

l==m
True
l is mm
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    l is mm
NameError: name 'mm' is not defined. Did you mean: 'm'?
l is m
False
''' is is used to check whether the memeory locations (id) is same are not in above exampe the l and m have same elements but difff list so it shows flase'''
' is is used to check whether the memeory locations (id) is same are not in above exampe the l and m have same elements but difff list so it shows flase'
n = m
n
[1, 2, 34, 56]
n is m
True
''' is is used to check whether the memeory locations (id) is same are  in above exampe the n and m have same elements and mmemeory'''
' is is used to check whether the memeory locations (id) is same are  in above exampe the n and m have same elements and mmemeory'
