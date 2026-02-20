# Functions 
# A function is a block of code that performs a specfic task.
# # Dividing a complex probelm into smaller chunks makes our progran easy to understand and reuse

# def greet():
#     print("Hello world")
# greet()

# print('This is a function class')
# print(9*6)
# greet()

# greet()

# def passw():
#     user_password = input("What is your password: ")
#     alpl = 'abcdefghijklmnopqrstuvwxyz'
#     alpu = alpl.upper()
#     digit = '1234567890'
#     spc = '!@#$%^&*()_+}{|?><'
#     a,b,c,d = False,False,False,False

#     for i in user_password:
#         if i in alpl:
#             a = True
#         elif i in alpu:
#             b = True
#         elif i in digit:
#             c = True
#         elif i in spc:
#             d = True
#     if len(user_password) > 8 and a and b and c and d:
#         print("Strong Password\nAccepted!!!")
#     else:
#         print('Not strong enough, Please try again!')



# def sqrt(num,base):
#     a = num**(1/base)
#     return a


# m = sqrt(9,2)
# y = sqrt(4,2)

# print(m*y)

def power(base, exponent = 2):
    print(f'power({base}, {exponent}) -> {base**exponent}')

power(4)

power(2,3)

power(9,2)

# Scenario: You need to check if a user's password is strong enough.

# Task: Write a program in a file named password_strength_checker.py that takes a string called password and prints True if the password is strong and False otherwise. A strong password:

# Is at least 8 characters long.
# Contains both uppercase and lowercase characters.
# Contains at least one digit.
# Contains at least one special character (e.g., !@#$%^&*()).

# Tip: Check for True or False for each condition of a strong password and chain the boolean results of each of them. If they are all True, the boolean chaining will result to True and result to False if there is at least one False.

# DO NOT USE REGEX.

# user_password = input('Please enter a password : ')
# alpl = 'abcdefghijklmnopqrstuvwxyz'
# alpu = alpl.upper()
# digit = '1234567890'
# spc = '!"£$%^&*()-_#~@'
# a,b,c,d = False,False,False,False

# for i in user_password:
#     if i in alpl:
#         a = True
#     elif i in alpu:
#         b = True
#     elif i in digit:
#         c = True
#     elif i in spc:
#         d = True

# if len(user_password) > 8 and a and b and c and d:
#     print('Strong Password\nAccepted!!!')
# else:
#     print('Not strong enough, please try again!')

# Functions 
# A function is a block of code that performs a specific task.
# Dividing a complex problem into smaller chunks makes our program easy to understand and reuse.

# def greet():
#     print('Hello world')

# greet()

# print('This is a function class')
# print(9*6)
# greet()

# greet()

# python function argument
# Arguments are inputs given to the function.

# def greet(name):
#     print(f'Hello {name}')

# greet('Kunle')
# greet('Yetunde')
# greet(9)

# greet('Jon ')

# def add_num(num1,num2):
#     print(num1+num2)

# add_num(2,4)

# Parameters vs Arguments 
# Parameters are the variables listed inside the parentheses in the function 
# definition. They act like placeholders for the data the function can accept when we call them. e.g num1, num2
    
# Arguments are the actual values that we pass to the function when we call it.
# Arguments replace the parameters when the function executes. e.g 2,4 from above

# The return statement 
# We return a value from the function using the return statement.

# def add_num(num1,num2):
#     a = num1 + num2
#     return a

# m = add_num(4,3)

# y = add_num(1,4) * 2
# print(m)
# print(y)

# The pass statement 
# It's typically used where code is planned but has yet to be written.

# def future_function():
#     pass

# Default arguments in functions 
# Python allows functions to have default argument values. Default arguments are used when no explicit values are passed to these parameters during a function call.

# def greet(name,message='Hello'):
#     print(f'{message} {name}')

# greet('Kunle','Goodmorning')
# greet('Mayowa')
