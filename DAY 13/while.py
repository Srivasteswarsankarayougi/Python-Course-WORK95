l = [1,2,0,0,0,0,0,3,5,6,7]
while 0 in l:
    l.remove(0)
print(l)

i=1
while i<11:
    print(i)
    i +=1


#print even numbers from 1to100
i = 2
while i<101:
    print(i)
    i +=2


#how to iterate the string
a = 'python programmin'
i = 0
while i <len(a):
    print(i,a[i])
    i += 1

a = [1,3,5,6,7,8]
i = 0

while i<len(a):
    print(i,a[i])
    i += 1

# input codegnan
# output cn oa dn eg

c = 'codegnan'
i = 0
j = len(c)-1

while i<=j:
    print(c[i],c[j])
    i += 1
    j -= 1


c = 'pythonprogramming'
i = 0
j = len(c)-1

while i<=j:
    if i==j:
        print(c[i])
    else:
     print(c[i],c[j])
    i += 1
    j -= 1

