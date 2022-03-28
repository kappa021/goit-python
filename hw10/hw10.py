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

    def __init__(self, name: str, phones: List[str] = None) -> None:
        self.name = Name(name)
        if phones == None:
            self.phones = []
        else:
            self.phones = [Phone(phone) for phone in phones]

    def add_phone(self, phone_number: str):
        phone = Phone(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone

    def delete_phone(self, phone_number: str):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
        
    def __repr__(self) -> str:
        return f"Name: {self.name.value}, Phones {[phone.value for phone in self.phones]}"


class AddressBook(UserDict):
    
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find_record(self, value: str):
        return self.data.get(value)

    def delete_record(self, value: str):
        self.data.pop(value)

    def __str__(self) -> str:
        return str(self.data)


def main():
    phone_book = AddressBook()

    phone_book.add_record(Record("Andrey"))
    phone_book.add_record(Record("Aleksey", ("0953550210",)))
    phone_book.add_record(Record("Anita", ("0685979829", "0639323060")))
    print(phone_book)
    print("\n")

    phone_book.delete_record("Anita")
    print(phone_book)
    print("\n")

    change_phone_number = phone_book.find_record("Aleksey")
    print(change_phone_number)
    print("\n")

    change_phone_number.add_phone("0956101472")
    change_phone_number.edit_phone("0956101472", "0934440272" )
    print(change_phone_number)
    print("\n")

    change_phone_number.delete_phone("0953550210")
    print(change_phone_number)
    print("\n")

    print(phone_book)


if __name__ == "__main__":
    main()