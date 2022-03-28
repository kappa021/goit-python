from typing import List
from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phones: List[Phone] = None) -> None:
        self.name = name
        if phones is None:
            self.phones = []
        else:
            self.phones = phones

    def add_phone(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        for phone in self.phones:
            if phone.value == old_phone.value:
                phone.value = new_phone.value

    def delete_phone(self, phone_number: Phone):
        for phone in self.phones:
            if phone.value == phone_number.value:
                self.phones.remove(phone)
        
    def __repr__(self) -> str:
        return f"Name: {self.name.value}, Phones {', '.join([str(phone.value) for phone in self.phones])}"


class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find_record(self, name: Name):
        return self.data.get(name.value)

    def delete_record(self, value: Name):
        self.data.pop(value.value)

    def __str__(self) -> str:
        return str(self.data)


def main():
    phone_book = AddressBook()

    phone_book.add_record(Record(Name("Andrey")))
    phone_book.add_record(Record(Name("Aleksey"), [Phone("0953550210")]))
    phone_book.add_record(Record(Name("Anita"), [Phone("0685979829"), Phone("0639323060")]))
    print(phone_book)
    print("\n")

    phone_book.delete_record(Name("Anita"))
    print(phone_book)
    print("\n")

    change_phone_number = phone_book.find_record(Name("Aleksey"))
    print(change_phone_number)
    print("\n")

    change_phone_number.add_phone(Phone("0956101472"))
    print(change_phone_number)
    print("\n")

    change_phone_number.edit_phone(Phone("0956101472"), Phone("0934440272"))
    print(change_phone_number)
    print("\n")

    change_phone_number.delete_phone(Phone("0953550210"))
    print(change_phone_number)
    print("\n")

    print(phone_book)


if __name__ == "__main__":
    main()