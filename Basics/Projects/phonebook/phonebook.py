# Phonebook App
# Write a Python program to implement a phonebook app that allows users to add, delete, and search for contacts. The app should use a dictionary to store contact information, with the contact name as the key and the phone number as the value.
# The app should have the following features:
# Add a contact: Prompt the user to enter a contact name and phone number, then add the contact to the dictionary. If the contact already exists, display an error message and do not add the contact.
# Delete a contact: Prompt the user to enter a contact name, then delete the contact from the dictionary if it exists. If the contact does not exist, display an error message.
# Search for a contact: Prompt the user to enter a contact name, then display the contact's phone number if it exists. If the contact does not exist, display an error message.
# Print all contacts: Display all contacts and their phone numbers in the dictionary.

import csv

contact = {}
class phonebook():
    def __init__(self,number,name):
        self.name = name
        self.number = number
class contactBook:
    def __init__(self):
        self.contact = []
    def add_number(name,number):
        if name in contact:
            print(f"{name} is already in the contact. Try another name")
        else:
            contact[name] = number
            print(f"{name} added with number")
    def delete_number(name):
        if name in contact:
            del contact[name]
            print(f"{name} deleted successfully")
        else:
            print(f"{name} does not exist in contact")
    def search_number(name):
        if name in contact:
            print(f"{name} number is {contact[name]}")
        else:
            print(f"{name} is not in contacts")
    def find_all():
        if contact:
            print('your contacts are:')
            for name, number in contact.items():
                print(f"{name}: {number}\n")
            else:
                print('empty phonebook')
while True:
    print("\nPhonebook App Menu:")
    print("1. Add a Contact")
    print("2. Delete a Contact")
    print("3. Search for a Contact")
    print("4. Print All Contacts")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        contactBook.add_number(name, number)
    elif choice == '2':
        name = input("Enter contact name to delete: ")
        contactBook.delete_number(name)
    elif choice == '3':
        name = input("Enter contact name to search: ")
        contactBook.search_number(name)
    elif choice == '4':
        contactBook.find_all()
    elif choice == '5':
        print("Exiting ContactBook. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
