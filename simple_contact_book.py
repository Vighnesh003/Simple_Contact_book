class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        self.contacts[name] = {"phone_number": phone_number, "email": email}
        print(f"Contact '{name}' added successfully.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' removed successfully.")
        else:
            print(f"Contact '{name}' not found in the contact book.")

    def view_contacts(self):
        if self.contacts:
            print("Your contacts:")
            for name, contact in self.contacts.items():
                print(f"Name: {name}, Phone Number: {contact['phone_number']}, Email: {contact['email']}")
        else:
            print("No contacts in the contact book.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Contact '{name}':")
            print(f"Phone Number: {self.contacts[name]['phone_number']}")
            print(f"Email: {self.contacts[name]['email']}")
        else:
            print(f"Contact '{name}' not found in the contact book.")

def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. Remove Contact")
        print("3. View Contacts")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)
        elif choice == "2":
            name = input("Enter contact name to remove: ")
            contact_book.remove_contact(name)
        elif choice == "3":
            contact_book.view_contacts()
        elif choice == "4":
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()