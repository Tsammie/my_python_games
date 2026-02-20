import sqlite3
import hashlib
import random
from getpass import getpass

conn = sqlite3.connect("mybank.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    account_no INTEGER PRIMARY KEY NOT NULL,
    fullname TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    balance INTEGER NOT NULL,
    password TEXT NOT NULL
)
""")

def sign_up():
    
    print("***************Sign Up***************")

    while True:
        fullname = input("Enter your fullname: ").strip()
        if not fullname:
            print("Fullname field cannot be left blank")
            continue
        break

    while True:
        username = input("Enter your username: ").strip()
        if not username:
            print("Username field cannot be left blank")
            continue
        break
    
    while True:

        try:
            initial_deposit = int(input("Enter your amount you want to deposit initially: "))
            if initial_deposit < 0:
                print("Amount must be Positive")
                continue
        except ValueError:
            print("Amount must be a number")
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
    account_no = random.randint(12000000, 22000000)

    try:
        cursor.execute("""
        INSERT INTO customers (account_no, fullname, username, balance, password) VALUES
        (?, ?, ?, ?, ?)
        """, (account_no, fullname, username, initial_deposit, hashed_password))
    except sqlite3.IntegrityError:
        print("Username already exists\n Account number already exist")
    else:
        conn.commit()
        print("Sign Up was successful")
        print(f'Your Account number is {account_no}')
        log_in()

def Withdrawal(username):
    print("Withdrawal is being made!!!")
    while True: 
        try:
            amount = int(input("Enter Amount to withdraw: ").strip())
            if amount <= 0:
                print("Amount must be greater than Zero.")
                continue
            break
        except ValueError:
            print("Amount must be number.")
    row = cursor.execute(
        "SELECT balance FROM customers WHERE username = ?",
        (username,)
    ).fetchone()

    if row is None:
        print("User not found in the database.")
        return

    balance = row[0]

    if amount > balance:
        print("Insufficient funds. Your current balance is:", balance)
        return
    new_balance = balance - amount

    cursor.execute(
        "UPDATE customers SET balance = ? WHERE username = ?",
        (new_balance, username)
    )
    conn.commit()

    print(f"Withdrawal successful. New balance is: {new_balance}")

def deposit(username):
    print("***************Deposit***************")

    while True:
        try:
            amount = int(input("Enter amount to deposit: ").strip())
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Amount must be a number.")

    row = cursor.execute(
        "SELECT balance FROM customers WHERE username = ?",
        (username,)
    ).fetchone()

    if row is None:
        print("User not found!")
        return

    balance = row[0]
    new_balance = balance + amount

    cursor.execute(
        "UPDATE customers SET balance = ? WHERE username = ?",
        (new_balance, username)
    )
    conn.commit()

    print(f"Deposit successful. New balance is: {new_balance}")


def view_balance(username):
    print("***************Available Balance***************")
    
    row = cursor.execute(
        "SELECT balance FROM customers WHERE username = ?",
        (username,)
    ).fetchone()

    if row is None:
        print("User not found.")
        return

    balance = row[0]
    print(f"Your available balance is: ₦{balance}")


def transfer(username):
    print("***************Money Transfer***************")

    while True:
        try:
            receiver_acct = int(input("Enter receiver's account number: ").strip())
            break
        except ValueError:
            print("Account number must be numbers only.")

    receiver = cursor.execute(
        "SELECT username, balance FROM customers WHERE account_no = ?",
        (receiver_acct,)
    ).fetchone()

    if receiver is None:
        print("Receiver account number does not exist.")
        return

    receiver_username = receiver[0]
    receiver_balance = receiver[1]

    if receiver_username == username:
        print("You cannot transfer money to your own account.")
        return

    while True:
        try:
            amount = int(input("Enter amount to transfer: ").strip())
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Amount must be a number.")

    sender_row = cursor.execute(
        "SELECT balance FROM customers WHERE username = ?",
        (username,)
    ).fetchone()

    sender_balance = sender_row[0]

    if amount > sender_balance:
        print("Insufficient funds. Transfer cannot be completed.")
        return

    new_sender_balance = sender_balance - amount
    new_receiver_balance = receiver_balance + amount


    cursor.execute(
        "UPDATE customers SET balance = ? WHERE username = ?",
        (new_sender_balance, username)
        )

    cursor.execute(
        "UPDATE customers SET balance = ? WHERE username = ?",
        (new_receiver_balance, receiver_username)
        )

    conn.commit()
    print(f"Transfer successful! You sent ₦{amount} to {receiver_username}.")
    print(f"Your new balance is: {new_sender_balance}")


def delete_account(username):
    print("***************Delete Account***************")
    
    confirm = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
    
    if confirm != "yes":
        print("Account deletion cancelled.")
        return

    user = cursor.execute("""
        SELECT account_no FROM customers 
        WHERE username = ? 
    """, (username, )).fetchone()

    cursor.execute(
        "DELETE FROM customers WHERE username = ?",
        (username,)
    )
    conn.commit()

    print("Your account has been permanently deleted. We're sorry to see you go!")
    print("You are now logged out.")


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

    customer = cursor.execute("""
        SELECT account_no, fullname, username, balance 
        FROM customers 
        WHERE username = ? AND password = ?
    """, (username, hashed_password)).fetchone()

    if customer is None:
        print("Invalid username or password")
        return

    print(f"Log In Successful. Welcome, {customer[1]}!")
    # customer = (account_no, fullname, username, balance)
    logged_in_username = customer[2]

    login_menu = '''
**************Menu***************
1. Make Withdrawal
2. Make Deposit
3. View Available Balance
4. Transfer Funds
5. Delete Account
6. Log Out
'''

    while True:
        print(login_menu)
        choice = input("Choose an option from the menu above: ").strip()

        if choice == "1":
            Withdrawal(logged_in_username)
        elif choice == "2":
            deposit(logged_in_username)
        elif choice == "3":
            view_balance(logged_in_username)
        elif choice == "5":
            delete_account(logged_in_username)
        elif choice == "4":
            transfer(logged_in_username)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice, select from the menu")

    

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
            print("Thank you for banking with us!")
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