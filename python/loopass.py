# # Exercise 1 
# i = 1
# while i < 6:
#     print(i)
#     i += 1
# # Exercise 2
# i = 0 
# while i < 3:
#     print("Hello")
#     i += 1
# # Exercise 3 
# i = 1
# while i <= 5:
#     print(i*2)
#     i += 1
# # Exercise 4
# i = 5
# while i >= 1 :
#     print(i)
#     i-=1
# # Exercise 5
# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1
# # Exercise 6
# user = int(input("a number : "))
# i = 0 
# while i < user:
#     print("*"*user)
#     i += 1
# # Exercise 7
# user = int(input("enter a number : "))
# i = 0 
# m = 1
# while i < user: 
#     print("*"* m)
#     i+=1
#     m+=1
# # Exercise 8 
# user = int(input("where should the countdown start? : "))
# i = user
# while i >= 1:
#     print(i)
#     i-=1
# print("GO!")

# # Exercise 9 
# i = 0 
# while i <10:
#     print(1, end= "")
#     i+=1

# # Exercise 10 
# i = 1
# while i <= 12:
#     print(3 * i)
#     i += 1



# # CLasswork
# user = int(input("Enter a number : "))
# i = 0
# while user > 0:
#     print(user)
#     i += user
#     user -= 1
# else: 
#     print(f'THe sum of all numbers from your input up to 1 is {i}')

# classwork2
import random
# # user = 80
# usera = input("Guess a number")
# attempt = 0 
# while attempt < 5:
#     usera = int(input("Guess a number"))
#     if usera > user:
#         print("too high")
#     elif usera < user: 
#         print("too low")
#     else:
#         print("This is the number")
#         break
#     attempt += 1
# else: 
#     print(f'Attempt finished, please play again later, the number is {user}')

# Classwork 3 
# user = input("enter the word : ")
# num_of_word = int(len(user))
# while num_of_word > 0:
#     print(user[num_of_word - 1], end="")
#     num_of_word -= 1

# # Classwork 4 
# password = "secret"
# while True:
#     user = input("please input your password : ")
#     if user == password:
#         print("Correct Password")
#         break
#     else: 
#         print("try again")
# Classwork 5

# user = int(input("input an integer : "))
# i = user
# while i > 0:
#     if i %2 == 0:
#         print(i)
#     i -=1

# Print the numbers of "J" in the sentence

# j = 'j'
# user = input('Please enter a word or sentence : ')
# i = 0
# counter = 0
# while i < len(user):
#     if user[i] in j:
#         counter += 1
#     i += 1
# else:
#     print(f'They are {counter} (j) in the word or statement above')


# number 1 # Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.

# userb = int(input("Enter the base: "))
# usere = int(input("Enter the exponent: "))
# result = 1
# counter = 0 
# while counter < usere:
#    result = result * userb
#    counter += 1
# print(f"{userb} raised to the power of {usere} is {result}")

# number 2 
# Write a program that takes comma-separated integers from the user, converts that
# 	to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
#       Use the min() function.
# integer = input("comma separated integers : ")
# integer_split = integer.split(",")
# integer_tuple = tuple(integer_split)
# n = 1
# while n <= len(integer_tuple):
#     i = integer_tuple[len(integer_tuple)- n] 
#     if i > integer_tuple[len(integer_tuple)- n]:
#         print(i)
#     n+=1

# NUmber 3
# Write a program that takes a string input from the user and uses a while loop to count
# 	the occurrences of each character, storing the counts in a dictionary.
# 	Sample Input:
# 	Enter a string: Hello
# 	Sample Output:
# 	{‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}

# j = 'j'
# user = input('Please enter a word or sentence : ')
# i = 0
# counter = 0
# while i < len(user):
#     if user[i] in j:
#         counter += 1
#     i += 1
# else:
#     print(f'They are {counter} (j) in the word or statement above')

# ASS1
# while True: 
#     userd = input("Do you want to continue. (Yes/No) : ")
#     if userd == "yes":
#         userb = int(input("What is your balance? : "))
#         usera = int(input("Enter the amount you want to withdraw? : "))
#         if userb > 0 and usera < userb:
#             print(f"Remaining balance: {userb - usera}")
#         else: 
#             print("Insufficent Balance")
#             break 
#     else: 
#         print("Thank you for banking with us")
#         break

# ASS2
# Write a program that simulates a grocery store checkout. The user should enter the prices of items until they decide to stop. The program should calculate and display the total cost.
# i = 0
# price = float(input("Enter item price: "))
# i+=price


# while True:
#     items = input("Enter another item? (yes/no)")
#     if items.lower() == "yes":
#         price = float(input("Enter item price: "))
#         i+=price
#     elif items.lower() == "no":
#         print(f"Total cost: {i} ")
#         break
#     else:
#         print("I didn't quite get that, try again!!!")

    
# for i in range(3,31,3):
#     print(i)

# cities = ["Lagos", "Abuja", "Kano", "Ibadan", "benin city"]
# newlist = []
# # for c in cities:
# #     newlist.append(c)
    
# # print(newlist)

# # newlist = [x for x in cities]
# # print(newlist)
# newlist = [x for x in cities if x != "Lagos"]
# print(newlist)

# # List comprehension Iterable
# sam = [x for x in range(1,11) if x%2 == 0]
# print(sam)

