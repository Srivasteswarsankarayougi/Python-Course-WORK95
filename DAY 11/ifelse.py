#write a program for the password verification using if else statement
data = ('admin@gmail.com', 'admin123')

gmail = input("Enter your email: ")
password = input("Enter your password: ")

if (gmail, password) == data:
    print("Login successful!")
else:
    print("Invalid email or password.")

#write a program to check if the number is even or odd using if else statement
number = int(input("Enter a number: "))
if number % 2 ==0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


#write a program to check whether the seat is booked or avaialable using if else statement
seats = {
    'A1': "available",
    'A2': "booked",
    'A3': "available",
    'A4': "booked",
    'A5': "available",
    'A6': "booked",
    'A7': "available",
}

seat_number = input("Enter the seat number (e.g., A1, A2, A3): ")
if seat_number in seats and seats[seat_number] == "available":
    seats[seat_number] = "booked"
    print(f"Seat {seat_number} is booked successfully.")
    print(seats)

else:
    print(f"Seat {seat_number} is not available for booking.")


# #write a program whether the items are available if available then print the items and if not available then print the message "item is not available"
items = {
    'item1': "DOSA",
    'item2': "IDLI",
    'item3': "VADA",
    'item4': "POHA"
}

item_name = input("Enter the item name (e.g., DOSA, IDLI, VADA, POHA): ")
if item_name in items.values():
    print(f"{item_name} is available.")




else:
    print("Item is not available.")


#write a programm to check the product is available or not if available then print the product and if not available then print the message "product is not available"
products = {
    'laptop': {'price': 50000, 'quantity': 10},
    'mobile': {'price': 20000, 'quantity': 20},
    'tablet': {'price': 15000, 'quantity': 15},
    'headphones': {'price': 2000, 'quantity': 30},
    'keyboard': {'price': 1000, 'quantity': 25}
}

item = input("Enter the product name (e.g., laptop, mobile, tablet, headphones, keyboard): ")
if item in products and products[item]['quantity'] > 0:
    print(f'{item} is available. price: {products[item]["price"]}')

else:
    print("Product is not available.")


