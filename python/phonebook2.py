phonebook = []

def add_contact():
    phone = input("what is the phone number:  ")
    name = input("what do you want to save the name as: ")
    favourite = False
    contact = {'Name':name,'Phone Number':phone,'Favourite':favourite}
    phonebook.append(contact)

def view_contact():
    for people in phonebook:
        print("\n")
        for contact,value in people.items():
            print(f'{contact}:{value}')

def update_contact(phone):
    for contact,value in enumerate(phonebook,start=0):
        if phone == phonebook[contact]['Phone Number']:
            update = input('What is the new name: ')
            library[i]['Name'] = update
            break
    else:
        print('Contact not found')

def delete_contact(phone):
    for contact,value in enumerate(phonebook,start=0):
        if phone == phonebook[contact]['Phone Number']:
            del phonebook[contact]
            break
    else:
        print("Contact not found")

def searuser_contact(name):
    for contact,value in enumerate(phonebook,start=0):
        if name == phonebook[contact]['Name']:
            for a,b in phonebook[contact].items():
                print(f'{a}:{b}')
                break
    else:
        print("Contact not found")

def mark_favorite(phone):
    for contact,value in enumerate(phonebook,start=0):
        if phone == phonebook[contact]['Phone Number']:
            phonebook[contact]['Favourite'] = True
            break
    else:
        print('Contact not found')

def unmark_favorite(phone):
    for contact,value in enumerate(phonebook,start=0):
        if phone == phonebook[contact]['Phone Number']:
            phonebook[contact]['Favourite'] = False
            break
    else:
        print('Contact not found')


while True: 
    print(f''' 
Phonebook
--------------------------------------------------------
What do you want to do today''')
    view_contact()

    print(
        '\n'f'''1. Add contact
2. update contact
3. delete contact
4. searuser contact
5. mark favourite
6. unmark favourite
7. quit

''')
    user = input('Please select an option : ')
    if user == '1':
        add_contact()
    elif user == '2':
        value = input('Please enter the Phone Number : ')
        update_contact(value)
    elif user == '3':
        value = input('Please enter the Phone Number: ')
        delete_contact(value)
    elif user == '4':
        value = input('Please enter the contact name : ')
        searuser_contact(value)
    elif user == '5':
        value = input('Please enter the phone number : ')
        mark_favorite(value)
    elif user == '6':
        value = input('Please enter the phone number : ')
        unmark_favorite(value)
    elif user == '7':
        print('Thank you')
        break
    else:
        print('Didn\'t get that, Please try again.')
