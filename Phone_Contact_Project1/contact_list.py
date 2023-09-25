import json


class Contact:
    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone


class ContactList:
    def __init__(self, file="phone_list.json"):
        self.contacts = []  # initially it will be empty list
        self.file = file
        self.load_contacts()

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        self.save_contacts()

    def load_contacts(self):
        try:
            with open(self.file, "r") as file:
                data = json.load(file)
                self.contacts = [
                    Contact(**contact_data) for contact_data in data
                ]  # into dict form
        except FileNotFoundError:
            self.contacts = []

        except Exception as exc:
            print(f"Handling excpetion in load_contacts.... {str(exc)}")

    def save_contacts(self):
        with open(self.file, "w") as file:
            json.dump([vars(contact) for contact in self.contacts], file)

    def search_contact(self, name: str) -> Contact:
        for contact in self.contacts:
            if contact.name == name:
                return contact

    def update_contact(self, name, new_phone: int) -> str:
        contact = self.search_contact(name)
        if contact:
            contact.name = name
            contact.phone = new_phone
            self.save_contacts()

    def delete_contact(self, name: str) -> None:
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            self.save_contacts()

    def show_all_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name} \t Phone: {contact.phone}")


def take_inputs() -> tuple:
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    return name, phone


def take_update_inputs() -> str:
    new_phone = input("Enter new phone number to update: ")
    return new_phone


def take_delete_input():
    delete_name = input("Enter name to delete: ")
    return delete_name
