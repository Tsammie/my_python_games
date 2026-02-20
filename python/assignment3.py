# Question 6
record = ("Jane", (32, "Manager"), ["HR", "Finance"])
name, details,position = record
print(name)
print(details[0])
print(position[0]) 

# Question 7
triplet = ("one", "two", "three")
first_variable, second_variable, third_variable = triplet
print(second_variable)

#Question 8
info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
product_num, categories, date = info
print(categories[0],"\n",date[2])

# Question 9 
nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
print(nested_tuple[2][0])

# Question 10
inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
one , two , three = inventory
print(two[1])

# Project 1 
# Create a Python program that manages a small student gradebook.

# The program should:

# 1. Ask the user how many students are in the class.


# 2. For each student:

# Ask for their name.

# Ask for 3 test scores (numeric inputs).


# 3. Store the data in a dictionary, where:

# The key is the student’s name.

# The value is a tuple containing the 3 scores.


# 4. After collecting all data:

# Display each student’s average score.

# Find and print:

# The student with the highest average

# The student with the lowest average

# Example Output:

# How many students? 3

# Enter name: Alice
# Enter 3 scores separated by space: 78 85 90

# Enter name: Bob
# Enter 3 scores separated by space: 60 70 65

# Enter name: Carol
# Enter 3 scores separated by space: 95 92 98

# --- Class Summary ---
# Alice -> Average: 84.33
# Bob -> Average: 65.00
# Carol -> Average: 95.00

# Top Student: Carol (95.00)
# Lowest Student: Bob (65.00)

no_of_student = input("How many students are in your class? : ")
name1 = input("Enter name : ")
score1 = input("Input 3 test scores of each students seperated with a commma : ")
score_list1 = score1.split(",")
score_tuple1 = tuple(score_list1)
name2 = input("Enter name : ")
score2 = input("Input 3 test scores of each students seperated with a commma : ")
score_list2 = score2.split(",")
score_tuple2 = tuple(score_list2)
name3 = input("Enter name : ")
score3 = input("Input 3 test scores of each students seperated with a commma : ")
score_list3 = score3.split(",")
score_tuple3 = tuple(score_list3)

print(score_tuple1)
print(score_tuple2)
print(score_tuple3)

result = {
    name1:score_tuple1 , 
    name2:score_tuple2 , 
    name3:score_tuple3
}
print(result)

print("Class Summary")

average1 = (int(result[name1][0]) + int(result[name1][1])+  int(result[name1][2]))/3
average2 = (int(result[name2][0]) + int(result[name2][1])+  int(result[name2][2]))/3
average3 = (int(result[name3][0]) + int(result[name3][1])+  int(result[name3][2]))/3

dict_aver = (average1, average2, average3)
max_aver = max(dict_aver)
min_aver = min(dict_aver)

print(f"{name1} -> Average: {average1:.2f}")

print(f"{name2} -> Average: {average2:.2f}")

print(f"{name3} -> Average: {average3:.2f}")

if max_aver == average1: print(f'Top Student: {name1} ({average1:.2f})')
elif max_aver == average2: print(f'Top Student: {name2} ({average2:.2f})')
else: print(f'Top Student: {name3} ({average3:.2f})')

if min_aver == average1: print(f'Lowest Student: {name1} ({average1:.2f})')
elif min_aver == average2: print(f'Lowest Student: {name2} ({average2:.2f})')
else: print(f'Lowest Student: {name3} ({average3:.2f})')



