library = []

def add_book():
    title = input('Please enter the title of the book : ')
    author = input('Please enter the author of the book : ')
    yop = int(input('Please enter the year of publication : '))
    isbn = input('Please enter the ISBN : ')
    available = True
    m = {'Title':title,'Author':author,'Year of publication':yop, 'ISBN':isbn, 'Available': available}
    library.append(m)

def view_book():
    for i in library:
        print('\n')
        for m,a in i.items():
            print(f'{m} : {a}')
        
def update_book(isbn):
    for i,a in enumerate(library,start=0):
        if isbn == library[i]['ISBN']:
            change = input('Please enter the change we want to make, e.g Title, Author, Year of publication : ').title()
            update = input('Should we replaced with what : ')
            library[i][change] = update
            break
    else:
        print('Book not found')

def delete_book(isbn):
    for i,a in enumerate(library,start=0):
        if isbn == library[i]['ISBN']:
            del library[i]
            break
    else:
        print('Book not found')    

def search_book(title):
    for i,a in enumerate(library,start=0):
        if title == library[i]['Title']:
            for a,b in library[i].items():
                print(f'{a} : {b}')
                break
    else:
        print('Book not found')

def borrow_book(isbn):
    for i,a in enumerate(library,start=0):
        if isbn == library[i]['ISBN']:
            library[i]['Available'] = False
            break
    else:
        print('Book not found')

def return_book(isbn):
    for i,a in enumerate(library,start=0):
        if isbn == library[i]['ISBN']:
            library[i]['Available'] = True
            break
    else:
        print('Book not found')

while True:
    print('''
    Welcome to the library:
    What would you like to do?
    1. Add book
    2. View book
    3. Update book
    4. Delete book
    5. Search book
    6. Borrow book
    7. Return book
    8. Quit
    ''')

    ch = input('Please select an option : ')
    if ch == '1':
        add_book()
    elif ch == '2':
        view_book()
    elif ch == '3':
        a = input('Please enter the ISBN : ')
        update_book(a)
    elif ch == '4':
        a = input('Please enter the ISBN : ')
        delete_book(a)
    elif ch == '5':
        a = input('Please enter the title : ')
        search_book(a)
    elif ch == '6':
        a = input('Please enter the ISBN : ')
        borrow_book(a)
    elif ch == '7':
        a = input('Please enter the ISBN : ')
        return_book(a)
    elif ch == '8':
        print('Quitting!!!')
        break
    else:
        print('Didn\'t get that, Please try again.')
