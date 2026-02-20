# Assignment number 1
# income, rent, utilities, groceries, savings -  input-in float
# total_expenses(rent,utilities,grocieries), remaining income(income-totalexp-savings) - calculated by you

# solution
income = float(input("what is your income? : "))
rent = float(input("How much is your rent? : "))
utilities = float(input("How much do you spend on utilities? : "))
groceries = float(input("How much do you spend on groceries? : "))
savings = float(input("How much did you save this? : "))
print(f"Your total expenses for the time being is {rent + utilities + groceries}naira")
print(f"the remaining income is {income -(rent + utilities + groceries)-savings}")


#Assignment number 2 
# Write a program that asks the user for their name and then greets them with their 
# name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.
# Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
# Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run or 121.
# Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. is_palindrome is either True or False.
# Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. is_valid is either True or False.
# Bonus point if you can hide the password input from displaying on the screen as clear text.
# Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.

# solution
userName = input("What is your name? : ")
print(f"Hello, {userName}!")
birthYear = int(input("What year were you born? : "))
currentYear = int(input("what year are we??"))
print(f"you are {currentYear - birthYear} years old today")
favouriteColor = input("What is your favourite color? : ")
print(f"your favourite color is {favouriteColor}")
# palindrome = input("input some text, let's check if it is a palidrome.")
weight = float(input("please, input your weight(in Kilograms) : ")) 
height = float(input("please, input your height(in meters) : "))
BMI = weight / (height ** 2)
print(f"Your BMI is {BMI} ")


#creating 3 madlib games 
# noun1 = input("input a noun : ")
# print("It is a game. Don't panick")
# noun2 = input("input a last name : ")
# print("The last naem sounds generic, love that!!!")
# adj1 = input("input any adjective relating to visit : ")
# print("Is that relating to visit??? [side eye***]")
# noun3 = input("input a pronoun : ")
# print("keep playing!!!!")
# noun4 = input("Input a noun please : ")
# print("Good of you, continue :) ")
# part1 = input("input a part of the body : ")
# print("Hmmmmmm. ")
# part2 = input("Another part of the body : ")
# print("why this???....")
# noun5 = input("input a plural noun ASAP : ")
# print("not fast enough but continue")
# noun6 = input("input a noun please : ")
# print("just right?? ehn weird person")
# noun7 = input("input a noun : ")
# print("weldone!!!")
# exc = input("input an Exclamation : ")
# print("exclamation nowwww!!!!, just continue")
# noun8 = input("a noun please : ")
# print("yeahhhhhhhh")
# noun9 = input("input a noun now!!! : ")
# print("don't get tired wait for the result")
# noun10 = input("another noun think ehn : ")
# print("you are mentally stable reaching here")
# verb1 = input("now a verb : ")
# print(";) ;) ;) ;) ;) ")
# noun11 = input("give me the second to the last noun : ")
# print("Good!!! you will love the result")
# adj2 = input("give me the second adjective in the game!!! : ")
# print("you are almost don no phor!!")
# noun12 = input("The last noun : ")
# print(f'''A one-act play to be performed by two {noun1} in this room.

# PATIENT: Thank you so very much for seeing me, Doctor {noun2}, On such {adj1} notice

# DENTIST: What is your problem, young {noun3}?

# PATIENT: I have a pain in my upper {noun4}, which is giving me a severe {part1}ache. 

# DENTIST: Let me take a look. Open your {part2} wide.
# Good. Now I'm going to tap your {noun5} with my {noun6}.

# PATIENT: Shouldn't you give me a/an{noun7}killer?

# DENTIST: It's not necessary yet. {exc}: I think I see a/an {noun8} in your upper {noun9}.

# PATIENT: Are you going to pull my {noun10} out?

# DENTIST: No. I'm going to {verb1} your tooth and put in a temporary {noun11}.

# PATIENT: When do I come back for the {adj2} filling?
    
# DENTIST: A day after I cash your {noun12}.''')