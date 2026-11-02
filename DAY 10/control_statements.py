# product = input("enter the product:")
# best_seller = eval(input("enter the status:"))

# if best_seller:
#     print(f'{product} is best seller')



# #Write a program to check the battery percentage of a device and print the status of the battery.battery_percentage = int(input("Enter the battery percentage: "))
# battery_percentage = int(input("Enter the battery percentage: "))
# if battery_percentage < 20:
#     print(f'The battery is low: {battery_percentage}%', 'Charge your device soon.')


#Write a program to check the bill while raining and print the status of the bill.
bill = int(input("Enter the bill amount: "))
status = input("Is it raining?: ")
if status:
    bill += 30
    print(f'Extra delivery charge of 30 added to the bill')

print(f'The total bill amount is: {bill}')


# bill = int(input("Enter the bill amount: "))
# status = input("Is it raining?: ").strip().lower()
# if status == 'yes':
#     bill += 30
#     print(f'Extra delivery charge of 30 added to the bill')

# print(f'The total bill amount is: {bill}')