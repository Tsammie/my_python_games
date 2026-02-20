def signup():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    print("---Welcome to our Bank App---")
    username = input("Enter your username : ")
    for i in username:

        if i in alphabet.upper():
            print("Invalid Character!!!")
        elif len(username) < 4:
            print("Username is too short!!")
        elif len(username) > 255:
            print("Username is too long")
        else:
            print("Username saved")


signup()