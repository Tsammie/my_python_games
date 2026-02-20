# try: 
#     while True:
#         age = int(input("how old are you? : "))
#         print(f'you are {age} years old')
#         break
# except ValueError:
#         print("Invalid Input, Try again!!!")



while True: 
    try:
        age = int(input("how old are you? : "))
        print(f'you are {age} years old')
        break
    except ValueError:
        print("Invalid Input, Try again!!!")


# Raising Custom Exception

