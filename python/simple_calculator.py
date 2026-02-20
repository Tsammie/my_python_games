def greetings():
    print("Welcome to the Simple Calculator")
greetings()
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num2 - num1

def mutiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num1 == 0: 
        return "Undefined"
    elif num2 == 0:
        return 0
    else:
        return num2/num1

while True: 
    userselecting = input('''Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
''')
    if userselecting == "5":
        print("Exiting.....")
        break

    num1 = int(input("first_number: "))
    num2 = int(input("second_number: "))
    if userselecting == "1":
        print(addition(num1,num2))
    elif userselecting == "2":
        print(subtraction(num1, num2))
    elif userselecting == "3":
        print(mutiplication(num1,num2))
    elif userselecting == "4":
        print(division(num1,num2))
    else:
        print("incorrect Entry")
    
    