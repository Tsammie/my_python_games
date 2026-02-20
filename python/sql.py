# # Getting started with sql using python


# import sqlite3

# # connect to a database or create one if it doesn't exist

# conn = sqlite3.connect('sqict.db')

# # create a cursor object
# cursor = conn.cursor()

# # # create a table called students
# # cursor.execute('''
# # create table if not exists students (
# #     id integer primary key autoincrement,
# #     name text not null,
# #     age integer not null
# #                )
# # ''')


# # populating a table
# # cursor.execute('''
# # insert into students(name, age)
# # values
# # ('Samuel',24),
# # ('Adebowale',29),
# # ('Charlie Brown',21),
# # ('Diana Evans',23),
# # ('Ethan Davis',20)
# # ''')

# # conn.commit()


# # # Fetching student table
# # cursor.execute('select * from students')
# # row = cursor.fetchall()
# # print(row)


# cursor.execute('''
# create table if not exists intructors (
#     id integer primary key autoincrement,
#     name text not null,
#     age integer not null,
#     salary integer not null
#                )
# ''')

# # cursor.execute('''
# # insert into intructors(name, age, salary)
# # values
# # ('Samuel',24,250000),
# # ('Adebowale',29,180000),
# # ('Charlie Brown',21,40000),
# # ('Diana Evans',23,200000),
# # ('Ethan Davis',20,77000)
# # ''')

# # conn.commit()

# cursor.execute('''
# update intructors
# set salary = 4000000
# where id = 1
# ''')

# conn.commit()

import sqlite3
import hashlib

from getpass import getpass

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL,
    password TEXT NOT NULL
)
""")
def sign_up():

    print("***************Sign Up***************")

    while True:

        first_name = input("Enter your first name: ").strip()

        if not first_name:
            print("First name field cannot be left blank")
            continue
        break

    while True:
        last_name = input("Enter your last name: ").strip()

        if not last_name:
            print("Last name field cannot be left blank")
            continue
        break

    while True:
        username = input("Enter your username: ").strip()
        if not last_name:
            print("Last name field cannot be left blank")
            continue
        break

    while True:

        try:
            age = int(input("Enter your age: "))
        except ValueError:
            print("Age must be a number")
            continue
        else:
            break

    while True:

        password = getpass("Enter your password: ").strip()
        if not password:
            print("Password field cannot be left blank")
            continue

        confirm_password = getpass("Confirm your password: ").strip()
        if not confirm_password:
            print("Confirm Password field cannot be left blank")
            continue


        if password != confirm_password:
            print("Those passwords don't match")
            continue

        break
    hashed_password = hashlib.sha256(password.encode()).hexdigest()


    try:
        cursor.execute("""
        INSERT INTO users (first_name, last_name, username, age, password) VALUES
        (?, ?, ?, ?, ?)
        """, (first_name, last_name, username, age, hashed_password))
    except sqlite3.IntegrityError:
        print("Username already exists")
    else:
        conn.commit()
        print("Sign Up was successful")
        log_in()


def log_in():
    print("***************Log In***************")
    while True:
        username = input("Enter your username: ").strip()
        if not username:
            print("Username field cannot be left blank")
            continue
        break

    while True:
        password = getpass("Enter your password: ").strip()
        if not password:
            print("Password field cannot be left blank")
            continue
        break


    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    user = cursor.execute("""
    SELECT first_name, username FROM users WHERE username = ? AND password = ?
    """, (username, hashed_password)).fetchone()

    if user is None:
        print("Invalid username or password: ")
        return
    print("Log In Successful")
    checkout(user)
    

def checkout(user):
    print("***************Check Out***************")
    print(user)
    print(f"Welcome to the checkout page {user[0]}")

menu = """
***************Menu***************"
1. Sign Up.
2. Log In
3. Quit
"""



try:
    while True:
        print(menu)
        choice = input("Choose an option from the menu above: ").strip()

        if choice == "3":
            print("Thanks for shopping with us!")
            break

        if choice == "1":
            sign_up()
        elif choice == "2":
            log_in()
        else:
            print("Invalid choice, select from the menu")
except Exception as e:
    print(f"Oops! Something went wrong: {e}")
finally:
    conn.close()
