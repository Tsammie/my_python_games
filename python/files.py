# Handling files in python
# Working with files in python

# opening s file in python

# reading from a file 

# with open('ourclass.txt','r') as file:
#     content = file.read()
#     print(content)

# with open('ourclass.txt',"r") as file:
#     a = file.readlines()
#     print(a)

# with open('ourclass.txt',"r") as file:
#     a = file.readline()
#     print(a)

with open("mode.txt","w") as m:
    big = m.write("I am now lying professionally")
#     i = m.writelines(["Firstline\n","secondLine\n","thirdline\n"])

# # appending or adding to a file
# with open('ourclass.txt','a') as mp:
#     map = mp.write('This will be added')


# from mypackage import module1,module2

# print(module1.function1())
# print(module2.function2())

# import datetime
# now = datetime.datetime.now()
# print(type(now))
# print(now)

# # creating a specfic date 
# date = datetime.date(2020,8,11)
# print(date)
# print(type(date))

# # Fomratting dates:
# format_date = now.strftime('%Y-%m-%d %H:%M:%S')
# print(format_date)
# print(type(format_date))

# # Parsing date
# date_string = "2024-07-30 14:53:20"
# parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print(parsed_date)
# print(type(parsed_date))

# import math
# f = math.lcm(72)
# print(f)

# with open("ourclass.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("ourclass.txt", "w") as file:
#     sam = file.write("THis is going to be added at the end of the program")
#     print(sam)

with open("sam.txt", "w") as file:
    sam = file.write("I love me")

with open("sam.txt", "r") as file:
    sam = file.read()
    print(sam)

with open("data.txt","r") as file:
    data = file.read()
    print(data)

