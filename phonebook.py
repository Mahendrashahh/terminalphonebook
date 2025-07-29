contacts = {} 
while True:
   
    print("welcome to the phonebook application")
    print("1. Add a new contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. exit")


    num=int(input("choose option 1-4 : "))
    if num==1:
        print("do you want to add bulk contacts? y for yes n for no  (y/n) : ")
        if input().lower() == 'y':
            while True:
                name = input("Enter name (or type 'exit' to stop): ")
                if name.lower() == 'exit':
                    break
                phone = input("Enter phone number: ")
                contacts[name] = phone
                print(f"Contact added: {name} - {phone}")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully!")
        print(f"👤 Name: {name}, 📞 Phone: {contacts[name]}")
    elif num==2:
        print ("Viewing all contacts...")
        if not contacts:
         print("No contacts found.")
        else:
         for name, phone in contacts .items():
            print(f"Name: {name}, Phone: {phone}")
    elif num==3:
        search_name = input("Enter the name to search: ")
        if search_name in contacts:
            print(f"Found contact - Name: {search_name}, Phone: {contacts[search_name]}")
        else:
            print("Contact not found.")
    elif num==4:
        delete_name = input("Enter the name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"Contact {delete_name} deleted successfully!")
        else:
            print("Contact not found.")
    elif num==5:
        print("Exiting phonebook application. Goodbye!")
    else:
        print("Invalid option selected. Please choose a valid option (1-5).")


    repeat = input("Do you want to perform another operation? (y/n): ")
    if repeat.lower() != 'y':
        print("Exiting phonebook application. Goodbye!")
        break