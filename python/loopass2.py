# Exercise 2
# Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7


# vowel = "aeiou"
# consonant = "bcdfghjklmnpqrstvwxyz"
# user = input("Input : ")
# i = 0
# counter1 = 0
# counter2 = 0
# while i < len(user):
#     if user[i].lower() in vowel:
#         counter1+=1
#     elif user[i].lower() in consonant:
#         counter2+=1
#     i+=1
# print(f"vowel: {counter1}")
# print(f"consonant: {counter2}")

# Exercise 3
# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

# user = int(input("Input : "))
# i = 0 
# while i < 13: 
#     print(f"{user} x {i} = {user*i}")
#     i += 1


# Exercise 5
# Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# user = input("Input: ")
# ok = user.split(",")
# output=[]
# for x in ok:
#     if x not in output:
#         output.append(x)
# print(f"Output: {output}")

# Exercise 7
# Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# 	Output: 20

# user = input("Input: ")
# user_split = user.split(",")
# integer_user = [int(s) for s in user_split]
# a = integer_user[0]
# for u in integer_user:
#     if u > a:
#         a = u
# print(a)

# Exercise 8
# Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)

# n = int(input("Input :  "))
# total = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         total+=i
# print(total)


# Exercise 9
# Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1

# text = input("Input: ")

# freq={}

# for char in text:
#     if char in freq:
#         freq[char] += 1
#     else:
#         freq[char] = 1
# for char, count in freq.items():
#     print(f"{char}:{count}")