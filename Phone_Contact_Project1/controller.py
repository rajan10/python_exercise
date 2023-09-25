from contact_list import ContactList, take_inputs, take_update_inputs, take_delete_input


class ContactController:
    def __init__(self, contact_list: ContactList):
        self.contact_list = contact_list

    def add_record(self) -> None:
        user_inputs = take_inputs()
        name, phone = user_inputs
        self.contact_list.add_contact(name, phone)
        print("Record added & saved Successfully!")

    def search_record(self, name: str) -> None:
        result_contact = self.contact_list.search_contact(name)
        if result_contact:
            print(f"Name: {result_contact.name}, Phone: {result_contact.phone}")
        else:
            print("Contact not found.")

    def update_record(self, name: str) -> None:
        new_phone = take_update_inputs()
        self.contact_list.update_contact(name, new_phone)

    def delete_record(self, name: str) -> None:
        delete_name = take_delete_input()
        self.contact_list.delete_contact(delete_name)

    def show_all_record(self) -> None:
        self.contact_list.show_all_contacts()
