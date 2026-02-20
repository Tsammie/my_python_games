# # Question 1
# a = int(input("enter numbers"))
# b = int(input("enter numbers"))
# if a > 0 and b > 0: 
#     print ("a and b are both positive")
# elif a > 0 or b > 0: 
#     print("only one is positive")
# else:
#     print("neither is positive")

# # Question 3
# text = input("Please input text only : ")
# if text == text[::-1]:
#     print("Is a palindrome")
# else :
#     print("Not a palindrome")

# # Question 4
# x = input("input a character : ")
# y = input("input a character : ")
# z = input("input a character : ")
# if x == y == z:
#     print("All same")
# elif x == y or x == z or y == z:
#     print("Two are equal")
# else:
#     print("All different")

# # Question 5
# angle_1 = input("Input an angle")
# angle_2 = input("Input an angle")
# angle_3 = input("Input an angle")
# if angle1 > 0 or angle2 > 0 or angle3 > 0 and angle_1 + angle_2 + angle_3 == 180:
#     print("Valid triangle")
# else: 
#     print("Invalid triangle")

# # Question 7
# color = input("Input three colors, seperate by commas : ")
# color_split = color.split(",")
# color_1,color_2,color_3 = color_split
# primaryColor = {"red", "yellow", "blue"}
# if color_1.lower() in primaryColor  and color_2.lower() in primaryColor and color_3.lower() in primaryColor:
#     print("all primary colors")
# else:
#     print("Not all primary colors")

# # Question 8 
# mode = input("Input mode : ")
# if mode == "manual":
#     print("Manual mode activated")
# elif mode == "automatic":
#     print("Automatic mode activated")
# else:
#     print("System is off")

# # Question 9 
# message = input("Type your message : ")
# a = "urgent"
# b = "important"
# c = "immediate"
# if message.find(a) != -1 :
#     print("High priority message")
# elif message.find(b) != -1 :
#     print("High priority message")
# elif message.find(c) != -1 :
#     print("High priority message")
# else:
#     print("Normal message")

# # Question 10
# user1 = input("input your status")
# user2 = input("Input your status")
# status1 = user1.find("active"), user1.find("inactive"), user1.find("pending")
# status2 = user1.find("active"), user1.find("inactive"), user1.find("pending")
# if status1 == (-1,-1,-1) or status2 == (-1,-1,-1):
#     print("invalid status")
# elif user1 == "active" and user2 == "active":
#     print("active")
# elif user1 == "active" or user2 == "active":
#     print("only one user is active")
# else: 
#     print("None active")

# # Question 11
# user = input("input your file name")
# if user.endswith(".jpg") == True:
#     print("Image file")
# elif user.endswith(".png") == True:
#     print("Image file")
# elif user.endswith(".gif") == True:
#     print("Image file")
# else:
#     print("Not a Image file")

# Question 12 
# access = input("user,admin or guest : ").lower()
# access_level = ["user", "admin", "guest"]
# user = access_level[0]
# admin = access_level[1]
# guest = access_level[2]
# if access == user:
#     print("Limited User")
# elif access == admin:
#     print("Full access")
# elif access == guest:
#     print("No acesss")
# # else:
# #     print("not valid")


# Question13





# numbers = input("input three numbers separated by comma")
# number_split = numbers.split(",")
# print(number_split)
# a,b,c = number_split
# a,b,c = int(a),int(b),int(c)
# if a >= b and a >= c:
#     print(f'{a} is the greatest')
# elif b >= a and b >= c:
#     print(f'{b} is the greatest')
#     print('sdd')
# elif c >= a and c >= b:
#     print(f'{c} is the greatest')



# # Assignment 1
# # An amusement park ride has these rules:
# # - Must be at least 120 cm tall to ride.
# # - If under 120 cm but with an adult, still allowed.
# # - Otherwise, not allowed.

# user = int(input("what is your height : "))
# usera = input("are you with adult? : ")
# if user > 120 or usera == "yes":
#     print("allowed")
# elif user < 120 and usera == "yes":
#     print("allowed")
# else:
#     print("not allowed")

# # Assignment 2
# # An exam grading system with retake rule:
# # The user enters exam score and retake status ("yes" or "no").
# # - If score is at least 50, print "Pass".
# # - If score is less than 50 but retake is "yes", print "Retake allowed".
# # - If score is less than 50 and no retake, print "Fail".
# user = int(input("What is your exam sccore : "))
# usera = input("is retake available? (yes/no) : ")
# if user >= 50:
#     print("PASS")
# elif usera == "yes":
#     print("Retake allowed")
# else: 
#     print("FAIL")

# Assignment 3
# A ride-hailing app calculates trip approval:
# The user enters distance (km) and wallet balance.
# Each km costs 200 units.
# - If wallet balance is enough for the trip, print "Trip confirmed".
# - If balance is less but at least half the cost, print "Add funds".
# - If less than half, print "Trip denied".

user =  int(input("Enter the distance : "))
usera = int(input("what is your balance"))
units = user * 200
if usera >= units:
    print("Trip confirmed")