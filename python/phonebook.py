# Beginning the phonebook
# declare the storage
phonebook = []
def add_contact():
    user_name = input("Input the name of the contact: ")
    user_number = input("Input the phone number of the contact: ")

    for contact in phonebook:
        if contact["user_number"] == user_number:
            print("Contact already exist!")
            return
    new_contact = {
        "Name": user_name,
        "PhoneNumber": user_number,
        "Favourite": False
    }
    phonebook.append(new_contact)
    print(f'{user_name} sucessfully added to your contact')

def view_contact():
    if not phonebook:
        print("contact does not exist")
        return
    print("\n Your Contact list ")
    for contact in phonebook:
        fav_status: "true" if contact["Favourite"] else "false"
        print(f'name: { contact["user_name"]}\n phonenumber: {contact["user_number"]} \n Favourite: {contact["user_number"]}:{fav_status}')

def update_contact():
    for i, contact in enumerate(user_number, start=0):

