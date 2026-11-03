# #write a proggram for weekend planner using ifelif ladder
# print("Welcome to the Weekend Planner!")
# budget = float(input("Enter your budget for the weekend: "))

# print("you can go for the following activities based on your budget:", end=" ")
# if budget >20000:
#     print("You can go for a trip.")

# elif budget >10000:
#     print("You can go for a resort.")

# elif budget >5000:
#     print("You can go for a movie.")    

# elif budget >2000:
#     print("You can go for a dinner.")

# elif budget >1000:
#     print("You can go for a picnic.")

# else:
#     print("You can stay at home and relax.")


#write a program to check the marks of a student and print the grade using if elif ladder

data  = {
    'sunny' : {'status': True, 'python': 85, 'mysql': 90, 'fastapi': 80},
    'bunny' : {'status': True, 'python': 75, 'mysql': 80, 'fastapi': 70},
    'chinnu' : {'status': True, 'python': 65, 'mysql': 70, 'fastapi': 60},
    'dinesh' : {'status': True, 'python': 55, 'mysql': 60, 'fastapi': 50},
    'soumya shree' : {'status': False, 'python': None, 'mysql': None, 'fastapi': None},

}

name = input("Enter the student's name: ")
if name in data:
    if data[name]['status']:
        total_marks = data[name]['python'] + data[name]['mysql'] + data[name]['fastapi']
        average_marks = total_marks / 3
        if average_marks >= 90:
            print(f"{name}Congratulations! You have scored an A grade with an average of {average_marks}.")
        elif average_marks >= 80:
            print(f"{name}Congratulations! You have scored a B grade with an average of {average_marks}. keep it up")
        elif average_marks >= 70:
            print(f"{name}Congratulations! You have scored a C grade with an average of {average_marks}. work hard to improve your grades.  ")
        elif average_marks >= 60:
            print(f"{name}Congratulations! You have scored a D grade with an average of {average_marks}. you need to work hard to improve your grades.")    
        elif average_marks >= 40:
            print(f"{name}Congratulations! You have scored an E grade with an average of {average_marks}. better luck next time. you need to work hard to improve your grades.  ")
        else:
            print(f"{name} you are failed for the exams. bring your parents to the school for further discussion.   ")

    else:
        print(f"{name} is absent for the exams. bring your parents to the school for further discussion.   ")

else:
    print(f"{name} is not found in the records. please check the name and try again.")