INPUT AND OUTPUT
ut and output

str input()

int -int(input())

float-float(input())

list of str
input().split() 

list of int
list(map(int,input().split()))

list of float-
list(map(float, input().split()))

tuple of str
tuple(input().split())

tuple of int
tuple (map(int, input().split()))

tuple of float-
tuple(map(float,input().split()))

set of str
set(input().split())

set of int
set(map(int,input().split()))

set of float-
set(map(float,input().split()))




STRING IS THE DEFULT INPUT
--------------------------
a = input("enter the name:")
enter the name:srivasteswar
a
'srivasteswar'
a = input('')
dkjj
a
'dkjj'
---------------------------------------------------------------------------------
STRING TO INTEGER


a = int(input())
a
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: 'a'
a = int(input())
2222

a
2222
a = int(input())
ssbib
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: 'ssbib'

-------------------------------------------------------------------------
FLOAT INPUT
a = float(input())
3333
a
3333.0

-------------------------------------------------------------------------
LIST OF str
a = list(input("enter the list:"))
         
enter the list:2333383
a
         
['2', '3', '3', '3', '3', '8', '3']

a = list(input("enter the list:"))
         
enter the list:22 333 44 5 5
a
         
['2', '2', ' ', '3', '3', '3', ' ', '4', '4', ' ', '5', ' ', '5']

---------------------------------------------------
LIST OF INT
a = list(input("enter the list:").split())
         
enter the list:23 444  333 33 
a
         
['23', '444', '333', '33']
a  = int(list(input("enter the list:").split()))
         
enter the list:23 22 222
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a  = int(list(input("enter the list:").split()))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a = list(map(int,input().split()))
         
2326726
a
         
[2326726]
a = list(map(int,input().split()))

         
232 2262 27272
a
         
[232, 2262, 27272]
-------------------------------------------------
a = list(map(float,input().split()))
         
235 25 26 
a
         
[235.0, 25.0, 26.0]


a = tuple(input("enter the tuple:"))
         
enter the tuple:22 2626 772
a
         
('2', '2', ' ', '2', '6', '2', '6', ' ', '7', '7', '2')
a = tuple(input("enter the tuple:").split())
         
enter the tuple:242 2622 272
a
         
('242', '2622', '272')
a  = tuple(map(int,input("eneter the tuplr").split()))
         
eneter the tuplr2729 229 2729
a
         
(2729, 229, 2729)
a  = tuple(map(float,input("eneter the tuplr").split()))
         
eneter the tuplr242 76673 2862
a
         
(242.0, 76673.0, 2862.0)



---------------------------------------------------------------------------------------------
MULTIPUL INPUTS
a,b,c = list(map(int,input("eneter the list").split()))
email,password = input().split()

eval FUNCTION
-------------
the eval function is used when we want to give input in specffic datatype

SYNTAX
a = eval(input())
2222

a = 2222


a = eval(input())
         
233.5
a
         
233.5

------------------------------------------------------------------------------------------

OUTPUT FUNCTION
a= 12
         
b = 2
         
c = "codegnan"
         
print(a,b,c)
         
12 2 codegnan
print("a=",a,"b=",b,"c=",c)
         
a= 12 b= 2 c= codegnan
print("a=",a,"b=",b,"c=",c ,sep='')
         
a=12b=2c=codegnan
print("a=",a,"b=",b,"c=",c,sep='-->',end='MC')
         
a=-->12-->b=-->2-->c=-->codegnanMC
'''F function'''
         
'F function'
print(f'a={a} b={b} c={c})
      
SyntaxError: unterminated string literal (detected at line 1)
print(f'a={a} b={b} c={c}')
      
a=12 b=2 c=codegnan

print('a=%d b=%d c=%s' %(a,b,c))
      
a=12 b=2 c=codegnan
print('a={} b={} c={}'format(a,b,c))
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('a={} b={} c={}',format(a,b,c))
      
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    print('a={} b={} c={}',format(a,b,c))
TypeError: format expected at most 2 arguments, got 3
print('a={} b={} c={}'.format(a, b, c))

a=12 b=2 c=codegnan
