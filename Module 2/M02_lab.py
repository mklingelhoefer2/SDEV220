# Mark Klingelhoefer
# M02_lab.py
# This app will take a student's name and GPA and 
# return whether or not they've made the Dean's List 
# and the honor roll

while True:
    first_name = input("Please enter first name:\n")
    last_name = input("Please enter last name: (type 'ZZZ' to quit program)\n")
    if last_name == 'ZZZ':
        break
    else:
        gpa = input("What is your GPA?\n")
        if float(gpa) >= 3.5:
            print(("{first_name} {last_name} has made the Dean's list.".format(firstName = first_name.capitalize(), lastName = last_name.capitalize())))
        if float(gpa) >= 3.25:
            print(("{first_name} {last_name} has made the honor roll.".format(firstName = first_name.capitalize(), lastName = last_name.capitalize())))