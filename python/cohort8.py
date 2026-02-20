# # 8th October, 25.
# # print_statement 
# # print("Hello World!")
# # print("My name is Iyanu!")

# VARIABLES = ...
# # A variable is a container that stores value, or values in form of an arrays 
# # Variables - are containers that store data values
# # Note: A variable is declared the moment you assign a value to it.

# # e.g. 
# # name = "Iyanu"
# # print(name)

# # num = 5
# # print(num)

# # Naming of Variables
# # Rules for naming Python variables
# # A variable name must start a letter or an underscore character, not with numbers, special charaters or python keywords (for, else etc).

# """
# 1. Single word... 
# name = ""

# 2. Multi-words
# i. snake case
# ii. Camel case
# iii. Pascal case
# """   
# # i. snake case 
# python_class = ""
# name_of_restuarant = ""

# # ii. Camel case 
# pythonClass = ""
# nameOfRestuarant = ""

# # iii. Pascal case 
# PythonClass = "" 
# NameOfRestuarant = ""

# # iv. lower case 
# pythonclass = ""
# nameofrestuarant = ""


# # Concatenation, print and Input function, 
# # Concatenation is the joining or merging of "strings" together
# # # # Concatenation only work for strings
# # # # plus sign is used for concatenating

# name1 = "Josiah"  # Josiah is a value
# name2 = "Jimmy"
# # print("Welcome to SQI,", name1, "and", name2)
# # print("Welcome to SQI, " + name1 + " and " + name2)

# # INPUT Function: The fuction is used to receive an input or value from a user, for computer's usage. Data values are received as strings by default.
# # name3 = "Jamiu"
# # name3 = input("What is your name? ")
# # course = input("What is your course of study? ")
# # print("Welcome to SQI,", name3, ".\n My course of study is: ", course)

# """
# Write a program that generates brandname based on two user's information.. 
# Precisely, the name of the person and occupation....
# Note - It should be a single brandname. i.e. you will join the two user's information together.

# # Quick Task 
# # Pass a greeting message to a username which ought to be supplied by the user. 
# #  Output : "Hello Jibola, you are welcome to Python class."
# """

# # text = "Write a program that generates brandname based on two user's information.." 
# # print(len(text))

# # print("Lets perform some arithmetic operations\nMultiply your favourite number by 5")
# # num = input("What is your Favourite number? ")
# # print(int(num) * 5)

# # num = int(input("What is your Favourite number? "))
# # print(num * 5)


# # # Data types 
# # 1. Strings 
# # 2. Numbers: int and float
# # 3. Boolean: True and False 
# # 4. complex: 12j
# # 5. Arrays: list, tuple, set and Dictionary 
# # Casting  or Data Conversion

# # Write a simple calculation that, receives three numbers as user inputs. output: sum of the numbers, the multiplication of the first and second number, and the division of the multiplication result by the sum result..........

# # print("Submit your three numbers!")
# # number1 = input(">>>>>> ") 
# # number2 = input(">>>>>> ") 
# # number3 = input(">>>>>> ") 

# # s = int(number1) + int(number2) + int(number3)
# # print(f"Sum of all numbers: {s}")
# # m = int(number1) * int(number2)
# # print(f"Multiplication of {number2} and {number3}: {m}")
# # print(f"{m} / {s}: {m / s}")

# # # OR 
# # print(f"Sum of all numbers: {int(number1) + int(number2) + int(number3)}")
# # print(f"Multiplication of {number2} and {number3}: {int(number1) * int(number2)}")
# # print(f"{int(number1) * int(number2)} / {int(number1) + int(number2) + int(number3)}: {(int(number1) * int(number2)) / (int(number1) + int(number2) + int(number3))}")

# # 9th October, 2025
# # DataTypes 
# # 1. Strings/Character/Varchar - They are usally written within "" - quotes.
# language = "Python"
# lucky_no = "7"
# # print(type(language))

# # 2. Numeric types: integer (int), float, complex 
# # Arithmetic operations can be performed on numeric types 
# n1 = 7
# n2 = 7.32
# c1 = 12j

# # # # 3. Boolean types: bool (True, False)
# lang = True
# lang_no = False

# # print(lang)
# print(type(lang_no))

# # # 4. Array types --- Array collects morethan one value
# # Types of array: tuple, list, range : They are ordered

# array_tuple = "Python", "Java"  # tuple  
# # array_tuple = ("Python", "Java")
# # print(type(array_tuple))
# array_list = ["","Python", "Java"]
# # array_list = list("")

# array_list.append("Javascript")

# # print((array_list[0]))

# # # 5. Mapping type: Mapping key and value - They are dictionary(object)
# dict_new = {
#     "name":"Jimmy",
#     "age":30,
#     "hobbies":["Giannis","Coding"]
#     }

# # print(dict_new)
# # print(dict_new["hobbies"][0])

# # 6. Set type (it is also an array, it isn't sequencial) - set, frozenset.
# set_new = {"Python", "Java"}
# set_new = {"Python", "Java", "Python", "C++", "Go"}
# # print(set_new)

# # # 7. Binary types: bytes, bytearray, memoryview
# # print(bin(30))

# CONVERSION_of_Data_types = ... 
# """
# It is also called Casting 
# Casting is the changing of data type to another data type. e.g. str to int. 
# Constructors are used for conversions
# """ 
# # str to int 

# str1 = "89"

# print(int(str1))

# # int to str 

# # int to float 
# print(8*0.6)
# num = 8
# print(float(num))

# # From list to tuple
# array_tuple = "Python", "Java"
# array_tuple = list(array_tuple)
# array_tuple.append("Golang")
# # print(array_tuple)
# # print(type(array_tuple))

# array_tuple = tuple(array_tuple)
# print(type(array_tuple))
# print(array_tuple)

# """
# Assignment: You are going to purchase a car for 3M in 2024, but your delayed till 2025. Now the car has increased by 26%. Calculate the new price... 
# Expected Output: 
# 1. The car that was 3M last year, now cost ____, due to 26% increase.

# Let's say that federal Govt policy for managing inflation was success, at least there would have been 5% reduction in the price.
# WHat is the price of the Car at 5% deflation..



# """
# print("Solution to the assignment")
# print("")
# car_price = int(3000000)
# print(f'The new price of the car is now {int(car_price + 0.26 * car_price)}naira after the inflation')
# print(f'After the intervention of the federal government the new price of the car is {int((car_price + 0.26 * car_price)-(0.05*(car_price + 0.26 * car_price)))}naira following the 5% deflation ')

# #another alternative

# new_price = int(3000000 + 0.26 * 3000000)
# print(f'The new price of the car is now {new_price} naira after the inflation')
# inflation_price = int(new_price - (0.05*new_price))
# print(f'After the intervention of the federal government the new price of the car is {inflation_price} naira following the 5% deflation')  

# # Python has a set of built in methods that we can use on strings

# # 1. Capitalize()- converts the first character of the string to uppercase and the rest to lowercase
# # text = 'HELLO WORLD'
# # captext = text.capitalize()
# # print(captext)
# # print(text)

# # text = '123hello'
# # captext = text.capitalize()
# # print(captext)
# # print(text)

# # 2. Title() - Converts the first character of each word to uppercase and the remaining character to lowercase. The title() method considers a word as a sequence of alphanumeric characters separated by non-alphanumeric characters.

# # text = 'hello world'
# # text = 'hello-world'
# # text = 'python\'s world'
# # text = '3rd place'
# # titletext = text.title()
# # print(titletext)
# # print(text)

# # 3. count() - returns the number of non-overlapping occurence of a sub string in a string.
# # text = 'hello world'
# # text = 'ababab'
# # captext = text.count('o')
# # captext = text.count('Hello')
# # captext = text.count('ab')
# # print(captext)
# # print(text)

# # 4. startswith() - returns true if the string starts with the specified prefix, otherwise false
# # text = 'hello world'
# # captext = text.startswith('w')
# # captext = text.startswith('hello')
# # captext = text.startswith('hello world')
# # print(captext)
# # print(text)

# # 5. endswith() - returns rue if tthe string ends with the specified suffix, otherwise false
# # text = 'hello world'
# # captext = text.endswith('dl')
# # captext = text.endswith('world')
# # print(captext)
# # print(text)

# # 6. find()- returns the lowest index of the substring if found in the string. otherwise -1
# # text = 'hello world'
# # captext = text.find('z')
# # captext = text.find('hello')
# # captext = text.find('o',5)
# # print(captext)
# # print(text)

# # 7. index()- same thing with find, only difference is that it returns error, when substring not found 
# # text = 'hello world'
# # # captext = text.index('z')
# # captext = text.index('hello')
# # captext = text.index('o',5)
# # print(captext)
# # print(text)

# # text = '123hello'
# # captext = text.capitalize()
# # print(captext)
# # print(text)

# # #19. Create a string variable sentence with the value "the quick brown fox jumps over the 
# # # lazy dog". Capitalize the first letter of the string and 
# # # print the result.
# # name3 = "the quick brown fox jumps over the lazy dog"
# # capName3 = name3.capitalize()
# # print(capName3)
# # # 20. 	Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# # # the first letter of each word and print the result.
# # title = "to kill a mockingbird"
# # main_title = title.title()
# # print(main_title)
# # # 21. 	Create a string variable text with the value "hello world". Count the number of 
# # # occurrences of the letter 'o' and print the result.
# # word = "hello world"
# # counter = word.count("o")
# # print(counter)
# # # 22. 	Create a string variable filename with the value "document.txt". Check if the string 
# # # starts with "doc" and print the result.
# # file = "document.txt"
# # trueFile = file.startswith("doc")
# # print(trueFile)
# # # 23.	Create a string variable url with the value "https://www.example.com". Check if the 
# # # string ends with ".com" and print the result.
# # url = "https://www.example.com"
# # endUrl = url.endswith(".com")
# # print(endUrl)
# # 24.	Create a string variable phrase with the value "find the needle in the haystack". Find 
# # the position of the word "needle" and print the result.
# # phrase = "find the needle in the haystack"
# # find_phrase = phrase.find("needle")
# # print(find_phrase) 
# # 25.	Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# # format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# # Result. Bonus point if you can do it with the f-string and concatenation methods also.
# # name4 = "Alice"
# # name5 = "Wonderland"
# # salutation1 = "Hello, {}. Welcome to {}."
# # for_sal = salutation1.format("Alice", "Wonderland")
# # print(for_sal)
# # salutation2 = f"Hello, {name4}. Welcome to {name5}."

# # 26.	Create a string variable quote with the value "To be or not to be". Find the position 
# # of the word "not" and print the result.
# # quote = "To be or not to be"
# # find_qoute = quote.index("not")
# # print(find_qoute)
# # """  """

# # # Input fuction 
# # name = input("Enter your name : ")
# # print(f'Hello{name}')

# # age = input('Enter your age : ')
# # age = int(age)
# # getpass - for paassword, or pins, or other privacy-sensitive inputs, use the "getpass" module. 
# import getpass
# pin = getpass.getpass("Enter your pin : ")
# print(pin)



# name = input ("Enter your name : ")
# age = int(input("Enter your age : "))
# satifaction = input( "How satisfied are you with SQI service (1-5)? : ")
# feedback = input("Any additional feedback? : ")
# print(f'{name} is {age} years old, and rated us {satifaction}/5 and feedback was \'{feedback}\'.')



# Assignment
# income, rent, utilities, groceries, savings
# total_expenses (rent, utilities, grocieries), remianing income(income_totalexp_savings) - 
# calculated by you 
# be creative with you print statement.... 

#solution 
# income = input("How much is your income? : ")
# rent = input(" How much do you pay for rent? : ")
# utilities = input(" How much do you pay for utilities? : ")
# grocieries = input( " How much do you spend on groticoes")
# total_expenses = float(int(rent) + float(utilities) + float(grocieries))
# print(total_expenses)

# collections in python
# A collection is an item thst can store multiple values into a single variable
# there are 4 collections in python
# lists, tuple, dictionary and sets 

# list
# shopping_list = ['apples', 'milk', 'banana', 'bread']
# print(shopping_list)


# nested_list = [
#     ["Alice", "Bob"],
#     [10,20,30],
#     [True, False]
# ]

# print(nested_list[0][1], nested_list[1][2], nested_list[2][0])

# Collection II -- Dictionary 


# phone_book = {'Jimi':"08129283844",'Samuel':"07049876574", 'abayomi':"09184939367"}
# print(phone_book)

# print(phone_book['Samuel'])

# phone_book['Jimi'] = "090678889905"
# print(phone_book)

# thisdict = {"brand":"Ford","Model":"Mustang","Year":1964}
# x = thisdict["Model"]
# print(x)
# print(type(x))

# thisdict['colour'] = "red"
# thisdict["Year"] = 2005
# print(thisdict)


# nested dictionary- 

# cars = {

#     "Toyota": {
#         "Sedan":["Camry","Corolla","Avalon"],
#         "SUV":["RAV4","Highlander","4Runner"]
#     },
    
#     "Ford": {
#         "sedan": ["Fusion", "Taurus"],
#         "SUV": ["Escape", "Explorer", "Expedition"]
#     },

#     "BMW":{
#         "sedan": ["3 Series", "5 Series", "7 Series"],
#         "SUV": ["X1", "X3", "X5"]
#     }

# }
# print(cars)
# print(cars["BMW"]["sedan"][2])


# print(company["Engineering"][1])

# family = {
#     "parents":["John","Jane"],
#     "children":[
#         {"name":"Tom", "age":5},
#         {"name":"Lucy", "age":8} 
#     ]
# }
# print(family["children"][0]["age"])
# Collections in python  
# A collection is an item that can store mulitple values into a single variable 
# There are 4 collections in python 
# list, tuple, dictionary and sets 

# List 
# shopping_list = ['apples','milk','banana','bread','apples']

# print(shopping_list)

# print(shopping_list[-1])

# shopping_list[1] = 'milo'
# print(shopping_list)

# print(shopping_list[1:3])
# print(shopping_list[0:2])
# print(shopping_list[2:])

# shopping_list[1:3] = ['blackcurrant','watermelon','juice']
# print(shopping_list)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]

# .insert() - to insert a new list item without replacing any of the existing values.
# thislist.insert(1,'rice')
# print(thislist)

# print(len(thislist))
# print(type(thislist))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# list1 = ["abc", 34, True, 40, "male"]
# print(type(list1))

# tuple1 = ('apple','banana','cherry')
# print(tuple1)
# print(type(tuple1))

# m = list(tuple1)
# print(m)
# print(type(m))

# adding to a list item 
# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")

# print(thislist)

# extending a list 
# thislist = ["apple", "banana", "cherry",'apple']
# tropical = ["mango", "pineapple", "papaya"]

# thislist.extend(tropical)
# print(thislist)
# print(tropical)

# can accept other collections as well 

# removing list items 
# thislist.remove('apple')
# print(thislist)

# # removing by index - .pop()
# thislist.pop(1)
# print(thislist)

# thislist.pop()
# print(thislist)

# using the del keyword
# del - delete

# del thislist[3]
# print(thislist)

# clear() - used to empty the list   
# thislist.clear()
# print(thislist)

# Sorting list 
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)

# desending order 
# thislist.sort(reverse=True)
# print(thislist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse=True)
# print(thislist)

# sorting is case sensitive 
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# reversing a list - picking from end to start
# thislist.reverse()
# print(thislist)

# print(thislist[::-1])

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# Nested List 
# matrix = [[1,2,3],[4,5,6],[7,8,9]]

# print(matrix)
# print(matrix[2])
# print(matrix[2][0])

# nested_list = [
#     ["Alice", "Bob"],
#     [10, 20, 30],
#     [True, False]
# ]
# bob, 30, true

# Collection II -- Dictionary 

# phone_book = {'jimi':'081292838483','Samuel':'39393939928','jimi':'111222333444','abayomi':'39393939928'}
# print(phone_book)

# print(phone_book['Samuel'])

# phone_book['jimi'] = '111222333444'

# print(phone_book)

# accessing dictionary items 
# thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
# x = thisdict["model"]
# print(x)
# print(type(x))

# thisdict['colour'] = 'red'
# print(thisdict)

# using the .get method()- used to get the value assoicated with a key
# print(thisdict.get('model'))
# print(thisdict.get('shape','Not foundd'))

# The setdefault method
# # returns the value of the item with the specified key
# car = {"brand": "Ford", "model": "Mustang", "year": 1964}
# x = car.setdefault("color", "white")
# print(x)
# print(car)

# x = car.setdefault("brand", "Toyota")
# print(car)

# .values = this method will return a list of all the values in the dictionary
# print(car.values())

# .items - method will return each item in a dictionary as a tuple in a list. 
# print(car.items())

# .keys() - return a list of off the keys in the dict 
# print(car.keys())

# print('model' in car)

# .update - will update the dict with the items from the given argument.
# car.update({'year':2020,'model':'Cybertruck'})
# car.update(year=2024,brand='Forde',model_num = 223)
# print(car)

# Removing items -  there are several methods of removing items from a dict 
# car.pop('model_num')
# print(car)

# popitem()
# car.popitem()
# print(car)

# del car['brand']
# print(car)

# del car
# print(car)

# print(len(car))

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(type(thisdict))

# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# thisdict.clear()
# print(thisdict)

# .copy()
# m = thisdict.copy()
# print(m)

# cars = {
#     "Toyota": {
#         "Sedan": ["Camry", "Corolla", "Avalon"],
#         "SUV": ["RAV4", "Highlander", "4Runner"]
#     },
#     "Ford": {
#         "Sedan": ["Fusion", "Taurus"],
#         "SUV": ["Escape", "Explorer", "Expedition"]
#     },
#     "BMW": {
#         "Sedan": ["3 Series", "5 Series", "7 Series"],
#         "SUV": ["X1", "X3", "X5"]
#     }
# }

# print(cars)
# print(cars['Ford']['SUV'])

# Assignemnt
# Create a dictionary called students where:

# The key is the student’s name (string)

# The value is another dictionary with subjects and grades

# Example:

# students = {
#     "Alice": {"Math": 88, "Science": 92, "English": 85},
#     "Bob": {"Math": 75, "Science": 78, "English": 80}
# }


# Add a new student and their subjects/grades using dict.update().

# Update a student’s grade for a particular subject.

# Remove a student from the dictionary using .pop().

# Display all students and their grades in a formatted way.

# Find and display:

# The average grade for each student.

# The student with the highest average grade.

# Allow users to search for a student by name using .get().

# Allow users to add new subjects to existing students.

# Print all subjects offered (no duplicates) using dictionary methods.

# Tuple in python 

# tuple is one of the four collections in python
#  characterics of a tuple 
# mytuple = ("Horse", "Hare","Rabbit","Dog")

# # Tuple is ordered 
# # Tuple is immutable
# print(len(mytuple))
# print(type(mytuple))

# samuel = ["Adedeji", "Oritu", "Fabiyi"]
# sam = tuple(samuel)
# print(sam)
# print(type(sam))


# x = "apple","banana","cherry"
# y = list(x)
# y[1] = "Orange"
# x = tuple(y)
# print(x)
# print(type(x))

# Sets - is a collection that is unordered,mutable, unindexed and doesn't allow duplicate. 

# thsiset = {'apple', 'banana', 'cherry'}
# print(thsiset)
# thsiset.ad('Juice')
# print(thsiset)

# Condition and conditional statement - if else elif 

# the if statement
# x = 2
# if x > 3 :
#     dog = 6
#     cat = 9
#     print(cat + dog)
# print("No cat No dog")
# # Tuples in python 
# mytuple = ('horse','hare','rabbit','horse')

# print(mytuple)
# print(mytuple[0])
# mytuple[1] = 'dog'

# tuple_1 = "abc", 34, True, 40, "male"
# tuple()

# tuple with one item 
# m = ('bag',)
# print(m)
# print(type(m))

# x = ("apple", "banana", "cherry")

# # join two tuples 
# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# # multiply tuples 
# tuplea = tuple1 * 2
# print(tuplea)

# fruits = ('apple','banana','cherry')
# x,y,z = fruits
# print(x)

# # using asterisk * during unpacking 
# fruits = ('apple','banana','cherry','mango','orange','pineapple')
# x,*y = fruits
# print(x)
# print(y)

# a,*b,_ = fruits
# print(a)
# print(b)
# print(c)

# # using asterisk and underscore 
# colors = ("red", "green", "blue", "yellow")
# color1, color2, *_ = colors

# print(color1) 
# print(color2) 

# Sets - is a collection that is unordered, mutable, unindexed and doesnt allow duplicate.

# thisset = {'apple','banana','cherry',True,2,1}
# print(thisset)
# # print(thisset[0])
# thisset.add('juice')

# print(thisset)

# thisset = {'juice','mango',0,43,False}
# print(thisset)

# print(type(thisset))

# animals = ["rabbit", "hare", "horse"] # this is a list
# animals_set = set(animals) 
# print(animals_set) 

# # accessing set items 
# print('rabbit' in animals_set)

# adding set items - .add()
# thisset = {"apple", "banana", "cherry"}
# thisset.add('orange')
# print(thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = ["pineapple", "mango", "papaya"]
# thisset.update(tropical)
# print(thisset)

# Removing set items 
# thisset.remove('pineappl')
# print(thisset)

# thisset.discard('pineappl')
# print(thisset)

# thisset.pop()
# print(thisset)

# Joining set items 
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all 
# items EXCEPT the duplicates.

# union - The union() method returns a new set with all items from both sets.
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = [True, False, 1]
# # set3 = set1.union(set2,set3)

# set3 = set1 | set2 | set3
# print(set1)
# print(set2)
# print(set3)

# Intersection - only keep the duplicates, 
# The intersection() method will return a new set, that only contains the items that are present in both sets.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)

# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
# set3 = set1.intersection(set2)
# print(set3)

# set1.intersection_update(set2)
# print(set1)
# print(set2)

# Difference() -  The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)

# print(set1)

# Symmetric difference 
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.symmetric_difference_update(set2)

# print(set1)

# Condition and conditional statement - if else elif
# the if statement
# if (x > 3) {
#     print('X is greater than 3')
# }
# x = 5
# if x > 3:
#     print('X is greater than 3')
#     print(3+4)
#     print('We are in a python class')
#     print('3'+'4')

# print('Python is sweet')

# the elif statement - else if
# b = 25
# a = 25

# if b >= a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# elif b <= a:
#     print('b is less than a')

# the else keyword catches anything which isn't caught by the preceding conditions.
# a = 265
# b = 23

# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")


# You can also have an else without the elif e.g.:
# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# short hand if 
# If you have only one statement to execute, you can put it on the same line as the if statement.

# a = 2
# b = 330

# if a > b: print('a is greater than b')

# short hand if .. else
# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

# print('A') if a > b else print('B')

# a = 200
# b = 33
# c = 500

# if a > b and c > a:
#   print("Both conditions are True")

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

# a = 33
# b = 200
# if not a > b:
#     print("a is NOT greater than b")
# else:
#     print('Not greater than a')

# Nested if
# x = 35

# if x > 10:
#     print('Above 10')
#     if x > 20:
#         print('Above 20')
#         if x > 30:
#             print('Above 30')
#             if x > 40:
#                 print('Above 40')
#                 if x > 50:
#                     print('Above 50')
#                     if x > 60:
#                         print('Above 60')
#                     else:
#                         print('Not up to 60')
#                 else:
#                     print('Not up to 50')
#             else:
#                 print('Not up to 40')
#         else:
#             print('Not up to 30')
#     else:
#         print('Not up to 20')
# else:
#     print('Not up to 10')


# the pass statement - if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
# a = 33
# b = 200

# if b > a:
#     pass

# Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

# user = input('Please enter three numbers seperated by comma : ')
# '5,2,7'
# user_split = user.split(',')
# a,b,c = user_split
# a,b,c = int(a),int(b),int(c)

# if a > b > c:
#     print('Decreasing order!!!')
# elif a<b<c:
#     print('Increasing order!!!')
# else:
#     print('Neither')


# You have a single character variable ch supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.

# ch = input('Please enter a single character : ')
# vowels = 'aeiou'
# consonant = 'bcdfghjklmnpqrstvwxyz'

# if ch.lower() in vowels:
#     print('A vowel')
# elif ch.lower() in consonant:
#     print('A consonant')
# else:
#     print('Not an alphabet')

# apple.jpg.mp4

# Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# 	input from the user and prints the greatest number. Use conditional statements
# 	to determine which number is the greatest. Bonus point if you can do it without else 
# 	statements.


# Loops 
# loops in python 
# A loop in programming repeatedly executes a block of code as long as a specified condition is true. It allows for tasks to be performed multiple times without writing the same code repeatedly. Common types of loops include for loops, which iterate a set number of times, and while loops, which continue until a condition is no longer met.

# while (i = 0;i < 5;i++) {
#     print('Hello world')
# }
    
# Three requirments of a loop
# 1. Declaration (kinda optional)
# 2. Condition (absoultely complusory)
# 3. Increment or decrement value ()

# i = 1
# while i <= 5:
#     print('Hello worldd')
#     i += 1

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# The break statement - With the break statement, we can stop the loop even if the while condition is true
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break

# With the continue statement, we can stop the current iteration, and continue with the next:
# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


# With the else statement, we can run a block of code once when the condition no longer is true:

# Example:
# Print a message once the condition is false:

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# i = 1
# while i < 13:
#     print(f'5 X {i} = {5*i}')
#     i += 1

# i = 1
# while i < 11:
#     if i != 5:
#         print(i)
#     i += 1

# i = 0
# while i < 10:
#     print(1,end='')
#     i += 1

# print('I am a boy')
# print('This is a python class',end=',')
# print('we are learning coding')


# Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).

# user = int(input('Please give us a number : '))
# i = 0
# while user > 0:
#     print(user)
#     i += user
#     user -= 1
# else:
#     print(f'The sum of all numbers from your input up to 1 is {i}')

# import random

# rad = random.randint(1,20)
# attempt = 5
# while attempt > 0:
#     user = int(input('Enter your guess : '))
#     if user > rad:
#         print('Too high')
#     elif user < rad:
#         print('Too low')
#     else:
#         print('Correct!!!')
#         break
#     attempt -= 1
# else:
#     print(f'Attempt finished, please play again later, the number is actually {rad}')

# while True:
#     user = input('Please enter exit to quit the loop : ')
#     if user == 'exit':
#         print('Quitting!!!')
#         break
#     else:
#         print('Not correct')

# user = int(input('Please enter a number : '))
# i = 1
# while i < user/2:
#     print(i * 2)
#     i += 1

# while user > 0:
#     if user%2 == 0:
#         print(user)
#     user -= 1

# Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.

# vowel = 'aeiou'
# user = input('Please enter a word or sentence : ')
# i = 0
# counter = 0
# while i < len(user):
#     if user[i] in vowel:
#         counter += 1
#     i += 1
# else:
#     print(f'They are {counter} vowels in the word or statement above')
# Assignemnt 1 - do for every time 'j' appears in the user input

# Write a program that tracks the inventory of items in a store. The user should be able 
# 	to add or remove items and the program should display the current inventory after each
# 	operation. The program stops when the user decides to exit.
# 	The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
# 	Sample Input and Output:
# 	Enter operation (add/remove/exit): add
# Enter item: eggs
# Enter quantity: 10
# Current inventory: {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): remove
# Enter item: fish
# Enter quantity: 50
# Current inventory: {'eggs': 50, 'fish': 150, 'bread': 343, 'yam': 2}
# Enter operation (add/remove/exit): exit

# inv = {'eggs': 50, 'fish': 200, 'bread': 343, 'yam': 2}
# while True:
#     op = input('Enter operation (add/remove/exit) : ')
#     if op.lower() == 'add':
#         item = input('Enter item: ').strip()
#         quan = int(input('Enter quantity: '))
#         inv[item] += quan
#     elif op.lower() == 'remove':
#         item = input('Enter item: ').strip()
#         quan = int(input('Enter quantity: '))
#         inv[item] -= quan
#     elif op.lower() == 'exit':
#         print('Quitting!!!!')
#         break
#     else:
#         print('Didn\'t get that, enter valid operation')
#     print(f'Current Inventory : {inv}')





# For loops in python 
# In Python, for loops iterate directly over items of a sequence (like lists, tuples, or strings) or other iterable objects, making them more intuitive and flexible.

# lista = ['apple','banana','mango']

# for item in lista:
#     print(f'Item {item}')


# items = ("guitar", "keyboard", "drums", "microphone", "amp")
# for item in items:
#     print(f"Item: {item}")


# capitals = {'USA': 'Washington, D.C.', 'France': 'Paris', 'Japan': 'Tokyo', 'Australia': 'Canberra', 'Egypt': 'Cairo'}
# # for a in capitals:
#     print(a)

# for a in capitals.values():
#     print(a)

# for a,b in capitals.items():
#     print(f'Country : {a}\nCapital : {b}\n')

# my_string = "Python is fun!"
# for char in my_string:
#     print(f"Character: {char}")

# The break statement - With the break statement, we can stop the loop before it has looped through all the items

# Exit the loop when x is "stop":
# actions = ["run", "jump", "stop", "walk"]
# for x in actions:
#     print(x)
#     if x == "stop":
#         break


# actions = ["run", "jump", "stop", "walk"]
# for x in actions:
#     if x == "stop":
#         break
#     print(x)


# The continue statement - With the continue statement, we can stop the current iteration of the loop and continue with the next
# tasks = ["start", "process", "skip", "finish"]
# for x in tasks:
#     if x == "skip":
#         continue
#     print(x)


# The range function - to loop thorugh a set of code a specified number of times, we can use the range() function  
# x = range(1,10)
# print(x)
# print(type(x))

# for a in x:
#     print(a)

# for i in range(6):
#     print(i)

# for a in range(2,6):
#     print(a)

# The enumerate function 
# The enumerate function in Python adds a counter to an iterable and returns it as an enumerate object. This allows you to loop over the iterable and have access to both the index and the value of each item simultaneously. It's particularly useful in for loops when you need to track the index of items in a list, tuple, or other iterable.

# fruits = ['apple', 'banana', 'cherry']
# for i,f in enumerate(fruits,start=11):
#     print(f'{i}. {f}')
#     if i == 12:
#         break

# for - else - just like the while else, specifies a block of code to be executted when the lopp is finished

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")


# for x in range(6):
#     if x == 3: 
#         break
#     print(x)
# else:
#     print("Finally finished!")

# Nested loops - A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adj in adjectives:
#     for animal in animals:
#         print(adj, animal)


# # The pass statement
# for x in [0, 1, 2]:
#     pass

# List Comprehensions - List comprehensions in Python provide a concise way to create lists. They consist of brackets containing an expression followed by a for clause, and can also include optional if clauses to filter items. This approach reduces the need for traditional loops and makes the code more readable.

# cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Benin City"]
# newlist = []

# newlist = [x for x in cities]
# print(newlist)

# for i in cities:
#     if 'a' in i:
#         newlist.append(i)

# print(newlist)

# newlist1= [x for x in cities if 'a' in x]

# newlist = [expression for item in iterable if condition == True]

# The return value is a new list, leaving the old list unchanged.

# List comprehension Iterable 
# newlist = [x for x in range(1,11)]
# print(newlist)

# THe expression The expression is the current item in the iteration, but it is also the outcome, which you
# can manipulate before it ends up as a list item in the new list:

# languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
# newlist = [x.upper() for x in languages if 'a' in x]
# print(newlist)

# newlist = ['hello' for x in languages]
# print(newlist)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# newlist = [x if x != 'JavaScript' else 'Typescript' for x in languages]
# print(newlist)

# Set Comprehension Example:
# languages = ["Pythona", "Javaa", "C++a", "JavaScripta", "Rubya"]
# newset = {x.upper() for x in languages}
# print(newset)  


# # Dictionary Comprehension Example:
# language = ["Python", "Java", "C++", "JavaScript", "Ruby"]
# newdict = {x: len(x) for x in languages}
# print(newdict)  

# any() and all()
# any(): Returns True if at least one element in the iterable is True, otherwise False.
# all(): Returns True if all elements in the iterable are True, otherwise False.

# numbers = [1, 2, 3, 4, 5]
# result = any([x>5 for x in numbers])
# print(result)

# result2 = all([x>0 for x in numbers])
# print(result2)

# Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.

# for a in range(1,101):
#     if a %3 == 0 and a % 5 == 0:
#         print('Fizzbuzz')
#     elif a % 3 == 0:
#         print('Fizz')
#     elif a % 5 == 0:
#         print('Buzz')
#     else:
#         print(a)



#  18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# for i,a in enumerate(names,start=0):
#     print(f'{a} got grade {grades[i]}')


# Errors and Exception Handling in python
# Errors
# result = 10/0
# print(result)
