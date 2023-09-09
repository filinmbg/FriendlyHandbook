from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value

class Name(Field):
    pass

class Record:
    def __init__(self, name: Name, phones: list, emails: list):
        self.name = name
        self.phones = [Phone(phone) for phone in phones]
        self.emails = emails

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def find_phone(self, value):
        for phone in self.phones:
            if phone.value == value:
                return phone
        return None

    def delete_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = Phone(new_phone)

class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)

    def edit_record(self, name, new_phones, new_emails):
        if name in self.data:
            record = self.data[name]
            record.phones = [Phone(phone) for phone in new_phones]
            record.emails = new_emails
            self.data[name] = record
            print(f"Contact {name} edited successfully.")
        else:
            print(f"Contact with Name '{name}' not found.")

def main():
    address_book = AddressBook()

    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter Name: ")
            phone_numbers = input("Enter Phone Numbers (Якщо кілька, то вказати через кому): ").split(',')
            emails = input("Enter Emails (Якщо кілька, то вказати через кому): ").split(',')

            name_field = Name(name.strip())
            record = Record(name_field, phone_numbers, emails)
            address_book.add_record(record)
            print(f"Contact {name} added to the address book.")

        elif choice == "2":
            search_term = input("Enter Name to search for: ")
            record = address_book.find_record(search_term)
            if record:
                print(f"Name: {record.name.value}")
                print("Phone Numbers:")
                for phone in record.phones:
                    print(phone.value)
                print("Emails:")
                for email in record.emails:
                    print(email)
            else:
                print(f"Contact with Name '{search_term}' not found.")

        elif choice == "3":
            edit_name = input("Enter Name to edit: ")
            new_phone_numbers = input("Enter New Phone Numbers (Якщо кілька, то вказати через кому): ").split(',')
            new_emails = input("Enter New Emails (Якщо кілька, то вказати через кому): ").split(',')
            address_book.edit_record(edit_name.strip(), new_phone_numbers, new_emails)

        elif choice == "4":
            delete_term = input("Enter Name to delete: ")
            record = address_book.find_record(delete_term)
            if record:
                del address_book.data[delete_term]
                print(f"Contact {delete_term} deleted from the address book.")
            else:
                print(f"Contact with Name '{delete_term}' not found.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
