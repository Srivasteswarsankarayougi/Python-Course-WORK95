l = [12,9,3,4,5,10,2,4,5,2,4,5]
i=0
j = len(l)-1
while i<=j:
    if i == j :
        print(l[i])
    else:
        sum = l[i]+l[j]
        print(sum)
        i +=1
        j -=1

input from the user until it stops
bill = 0
while True:
    product = input("enter the product untill stop:")
    if product == 'STOP':
        print('Total bill:',bill)
        break
    price = int(input('enter the price'))
    Quantity = int(input('enter the quantity'))
    bill += price*Quantity

10
dict -> key(product) , val(price),quantity()
menu = {'product':'paneerpakoda','price':350,'quantity':30,
     'product':'paneerbiriyani','price':350,'quantity':30,
     'product':'palakpaneer','price':450,'quantity':20,
     'product':'chikenbiriyani','price':350,'quantity':30,
     'product':'paneerpepparfrybiriyani','price':350,'quantity':20,
     'product':'muttonbiriyani','price':450,'quantity':10


     }
bill = 0
while True:
    menu['product'] = input("enter the product untill stop:")
    if menu['product'] == 'STOP':
        print('Total bill:',bill)
        print('product:',menu['product'],'price:',menu['price'],'quantity:',menu['quantity'])
        print('THANKYOU')
        break
    menu['price'] = int(input('enter the price'))
    quantity = int(input('enter the quantity'))
    bill += price*quantity





  