#write a program to verify the pin

pin  = 1234  # predefined pin
 # user input for pin
for i in range(5):
    epin = int(input("Enter your pin: ")) 
    if epin == pin:
        print("Pin verified successfully!")
        break
    else:
        print("Incorrect pin. Please try again.")

else:
    print("You have exceeded the maximum number of attempts. Please try again later.")



#example2 
l = [2,4,6,7,24,90,24,45,34,56,40]
search = int(input("Enter the number to search: "))
for i in range(len(l)):
    if l[i] == search:
        print("Number found at index:", i)
        break
else:
    print("Number not found.")


enumerate function
l = [2,4,6,7,24,90,24,45,
34,56,40]

for i in enumerate(l):
    print(i)

c = "codegnan"

for i in enumerate(c):

    print(i[0], i[1])

c = {"k1":"v1","k2":"v2","k3":"v3"}
for i in enumerate(c):
    print(i[0],i[1],c[i][1])