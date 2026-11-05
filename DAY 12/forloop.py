#looping can be done in str list and tuple and dictionary and set
#syntax of for loop
#for i in sequence:
#    body of for loop


#example of for loop
s = "sunny"
for i in s:
    print(i)

#example 2
a = input("Enter a word: ")
for i in a:
    if i in 'aeiouAEIOU':
        print(i, "is a vowel")

#list example
l = [1, 2, 3, 4, 5]
for i in l:
    print(i)

#program to print even numbers 
l = list(map(int, input("enter the numbers: ").split()))
for i in l:
    if i%2 == 0:
        print(i, "is even")

#tuple example
t = tuple(map(int, input("enter the numbers:").split()))
for i in t:
    print(i)

#program to sum of numbers in tuple
sum  = 0
t = tuple(map(int , input("enter the tuple numbers:").split()))
for i in t:
    sum += i
print("sum of the tuple", sum)

#set example
#a program to print maximum number in set
s = set(map(int, input("enter the numbers:").split()))

max_num = 0
for i in s:
    if i > max_num:
        max_num = i
print("maximum number in set is:", max_num)


#dictionary example
marks = {'maths': 90, 'science': 80, 'english': 70 , 'computer': 95, 'social': 85, 'hindi': 75}
for i in marks:
    print(i, ":", marks[i])


# marks = dict(map(str, input("enter the subject and marks:").split()))
sum  = 0
for i in marks:
    sum += marks[i]

print("sum of marks is:", sum)

#Range fuction
# range(start, stop(end+1), step)
# range(0, 10, 1)

for i in range(1, 11):
    print(i)

for i in range(20,1,-1):
    print(i)

for i in range(2, 108, 2):
    print(i)

# #to print the table of a number
n = int(input("enter your number: "))
for i in range (1,20):
    print(f"{n}*{i} = {n*i}")

c = input("enter the string: ")
for i in range(len(c)):
    print(c[i],i, end = " ")

# #we should use the range value if there any need of rang value in the loop otherwise we can use the for loop directly on the string or list or tuple or set or dictionary   

# #input: sunny
# # output: s0u1n3y4 remove the repeated characters and print the index of the character in the string
s = input("enter the string: ")
for i in range(len(s)):
    if s[i] is not s[i-1]:
        print(s[i], i, end = " ")        



l = list(map(int, input("enter the numbers: ").split()))
sum_index = 0
for i in range(len(l)):
    if l[i] % 2 == 0:
        sum_index += i
print(f"The sum of the index of even numbers in the list is: {sum_index}")

t = tuple(map(int, input("enter the numbers: ").split()))
product_index = 1
for i in range(len(t)):
    if t[i] % 2 != 0:
        product_index *= i
print(f"The product of the index of odd numbers in the tuple is: {product_index}")




# #break and continue statement
for i in range(1, 11):
    if i == 5:
        break
    print(i)


for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#pass statement
#to define a block of code that does nothing, we can use the pass statement. 
# It is used as a placeholder for future code. When the pass statement is executed, 
# nothing happens, but you avoid getting an error when empty code is not allowed.  

for i in range(1, 11):
    if i == 5:
        pass
    print(i)

if True:
    pass 
