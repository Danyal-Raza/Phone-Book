import os

def is_file_empty(filename):
    return os.stat(filename).st_size == 0  # Check if the file size is 0

def AddContact():
    name = input("Enter Name: ")
    while True:
        try:
            contact = int(input("Enter your contact number: "))
            break
        except ValueError:
            print("Please enter a valid numeric contact number.")
    file = open("contacts.txt", "a")
    file.write(name + " " + str(contact) + "\n")
    file.close()

def UpdateContact():
    file = open("contacts.txt", "r")
    if is_file_empty(file.name):
        print("No contacts found in the Phone Book\n")
    else:
        lines = file.readlines()
        file.close()
        file = open("contacts.txt", "w")
        name = input("Enter name of the contact: ")
        found = False
        for line in lines:             # fetch line by line from the file
            Name=line.split()
            if len(Name) >= 1 and (name.lower() == Name[0].lower() or name.lower() == Name[1].lower() or name.lower() == Name[-1].lower()):
                # fetches first word from a line and compare it
                name = input("Enter contact name: ")
                contact = input("Enter contact number: ")
                file.write(name + " " + contact+ "\n")
                found = True
                break
            else:
                file.write(line)
        if not found:
            print("Contact not found\n")
        file.close()

def Search():
    file = open("contacts.txt", "r")
    if is_file_empty(file.name):
        print("No contacts found in the Phone Book\n")
    else:
        name = input("Enter Name: ")
        found = False
        lines = file.readlines()
        for line in lines:
            Name=line.split()
            if len(Name) >= 1 and (name.lower() == Name[0].lower() or name.lower() == Name[1].lower() or name.lower() == Name[-1].lower()):
                print("Contact Details\n",line.strip())
                found = True
                break
        if not found:
            print("Contact not found")
    file.close()

def Show():
    file = open("contacts.txt", "r")
    if is_file_empty(file.name):
        print("No contacts found in the Phone Book\n")
    else:
        print("All Contact Details\n")
        for line in file:
            print(line.strip())
    file.close()

def RemoveContact():
    file = open("contacts.txt", "r")
    if is_file_empty(file.name):
        print("No contacts found in the Phone Book\n")
    else:
        lines = file.readlines()
        file.close()
        file = open("contacts.txt", "w")
        name = input("Enter Name: ")
        found = False
        for line in lines:   #fetches words from a line
            Name = line.split()
            if len(Name) >= 1 and (name.lower() == Name[0].lower() or name.lower() == Name[1].lower() or name.lower() == Name[-1].lower()):
                found = True
            else:
                file.write(line)
        if not found:
            print("Contact not found\n")
        else:
            print("Contact Removed Successfully\n")
    file.close()