from Phone_Book import *

while True:
    print("Welcome to Phone Book")
    print("1. Add Contact")
    print("2. Update Contact")
    print("3. Search")
    print("4. Show All Contacts")
    print("5. Remove Contact")
    print("6. Exit")
    try:
        opt = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid integer.")
        input("Press Enter to continue...")
        print("\n\n")
        continue
    match opt:
        case 1:
            AddContact()
        case 2:
            UpdateContact()
        case 3:
            Search()
        case 4:
            Show()
        case 5:
            RemoveContact()
        case 6:
            exit()
        case _:
            print("Invalid Choice\n")
    input("Press Enter to continue...")
    print("\n\n")