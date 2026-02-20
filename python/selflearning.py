# try: 
#     age = int(input("how old are you? : "))
#     print(f'you are {age} years old')
# except ValueError:
#     print("Invalid Input, Try again!!!")

# lines = []
# print("Enter multiple lines (type 'stop' to end):")
# while True:
#     line = input()
#     if line.lower() == 'stop':
#         break
#     lines.append(line)
# print("You entered:")
# print("\n".join(lines))


# # Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# # Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# # Bonus point if you can hide the password input from displaying on the screen as clear text.
# import getpass
# password = getpass.getpass("What is your password :")
# is_valid = len(password) >= 8 and len(password) <= 30
# print(f'It is {is_valid} that the password fulfils the criteria. ')


# # Write a Python program named `sum_of_two_digits.py` that takes a string as input from the user. The string will consist of exactly two digits (e.g., "23", "98", "09"). Your program should calculate and output the sum of these two digits.

# # Example:

# # For input "23", the program should output 5 i.e. (2 + 3).
# # For input "98", the program should output 17 i.e. (9 + 8).
# # For input "09", the program should output 9 i.e. (0 + 9).

# # Assume that the input will always be a string made up of
# # exactly two digits.
# two_digit = input(" Enter the two digit you want to add: (0-9): ")
# firstDigit = int(two_digit[0])
# secondDigit = int(two_digit[1])
# print(firstDigit+secondDigit)

# You have a variable `day` provided by user input which can be any day of the week 
# 	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# 	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
# day = input("What day is it today?? : ")
# weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# weekends = ["Saturday", "Sunday"]
# if day.title() in weekdays:
#     print("Weekday")
# elif day.title() in weekends:
#     print("Weekend")
# else:
#     print("Not a day of the week")

# n = int(input("no: ").strip())
# if n%2 == 1:
#     print("Weird")
# elif n%2 == 0 and n>=2 and n<=6:
#     print("Not weird")
# elif n%2 == 0 and n>=6 and n<=20:
#     print("Weird")
# elif  n%2 == 0 and n>20:
#     print("Not weird")

# a = int(input())
# b = int(input())
# print(a+b)
# print(a-b)
# print

# def is_leap(year):
#     leap = False
#     if year%100 == 0 and year%400 == 0 and year%4 ==0:
#         leap = True
#     return leap

# print(is_leap(2100))

# for a in range(2,6):
#    print(a)
# defining the class
# class bike():
#     name = ""
#     gear = 0
#     brake = False

# # create object of the class 
# bike1 = bike()
# bike2 = bike()

# bike2.gear = 4
# bike2.name = "BMX"
# bike1.name = "Mountain bike"
# bike1.gear = 11
# bike1.brake = True

# print(f'Name: {bike1.name}, Gear: {bike2.gear}, Brake: {bike2.brake}')

# 



# Let's create a class called room and def method to calculate the area of the room

# class room():
#     length = 0
#     breath = 0

#     def area(self):
#         print("Area of the room: ", self.length*self.breath)

# study_room = room()
# study_room.length = 50
# study_room.breath = 20

# # study_room.area()



# class House():
#     colour = "Red"
#     no_of_room = 4
#     type = ""

input("What is your Username?: ")
input("What is your password?: ")