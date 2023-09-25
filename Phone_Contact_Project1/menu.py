from contact_list import ContactList
from controller import ContactController

contact_list_obj = ContactList()
controller = ContactController(contact_list_obj)


def menu_display():
    while True:
        print(
            """
         Contact List Menu
         1. Add Contact
         2. Search Contact By Name
         3. Update by Name
         4. Delete
         5. Show all Record
         6. Exit   
               """
        )
        choice = input("Enter your choice: ")

        if choice == "1":
            controller.add_record()

        elif choice == "2":
            name = input("Enter name to search: ")
            controller.search_record(name)

        elif choice == "3":
            name = input("Enter name to Update: ")
            controller.update_record(name)

        elif choice == "4":
            name = input("Enter name to Delete: ")
            controller.delete_record(name)

        elif choice == "5":
            controller.show_all_record()

        elif choice == "6":
            print("Existing the Contact List Program")
            break
        else:
            print("Invalid Choice. Please choose 1, 2 , 3, 4, 5 or 6 ")
