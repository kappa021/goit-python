from typing import List
from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    
    def __eq__(self, other: object) -> bool:
        return self.value == other.value

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
    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec

    def find_record(self, name: Name) -> Record:
        return self.data.get(name.value)

    def delete_record(self, value: Name):
        self.data.pop(value.value)

    def __str__(self) -> str:
        return str(self.data)

phone_book = AddressBook()


def input_error(function):
    def inner(args):
        try:
            return function(args)
        except KeyError:
            print("Not such name exist.")
        except ValueError:
            print("Enter the name and number after the command separated by a space.")
        except IndexError:
            print("Phone book is empty.")
    return inner

def greeting_command():
    print("How can I help you?")

@input_error
def add_contact(args):
    
    name = args[0]
    if len(args) == 1:
        phone_book.add_record(Record(Name(name), []))
        print(f"The record with {name} was added without phone")
    elif phone_book.find_record(Name(name)):
        result = phone_book.find_record(Name(name))
        result.add_phone(Phone(args[1]))
        print(f"The phone was added for the {name}.")
    else:
        phone_book.add_record(Record(Name(name), [Phone(args[1])]))
        print("Contact added successfully")


@input_error
def change_phone_number(args):
    name, old_phone, new_phone = args
    if phone_book.find_record(Name(name)):
        result = phone_book.find_record(Name(name))
        result.edit_phone(Phone(old_phone), Phone(new_phone))
        print(f"Phone number for the {name} was changed successfuly.")
    else:
        print(f"Record for the {name} does not exist. Enter the correct name, please.")


@input_error
def get_phone_number(args):
    name = args[0]
    result = phone_book.find_record(Name(name))
    print(result)


@input_error
def delete_record(args):
    name = args[0]
    phone_book.delete_record(Name(name))
    print(f"The record with {name} was deleted successfuly")


@input_error
def remove_phone(args):
    name, phone = args
    result = phone_book.find_record(Name(name))
    result.delete_phone(Phone(phone))
    print(f"The phone for the {name} was removed successfuly.")

@input_error
def show_all_contacts(_):
    if len(phone_book) == 0:
        raise IndexError 
    print(phone_book)


def exit_command():
    print("Good bye!")


def main():
    while True:
        c = input("Enter a command: ")
        args = c.split(" ")

        if args[0].lower() == "hello":
            greeting_command()
        elif args[0].lower() == "add":
            add_contact(args[1:])
        elif args[0].lower() == "phone":
            get_phone_number(args[1:])
        elif args[0].lower() == "change":
            change_phone_number(args[1:])
        elif args[0].lower() == "delete":
            delete_record(args[1:])
        elif args[0].lower() == "remove":
            remove_phone(args[1:])
        elif len(args)>=2 and f"{args[0]} {args[1]}".lower() == "show all":
            show_all_contacts([])
        elif len(args)>=2 and f"{args[0]} {args[1]}".lower() == "good bye" \
                                                or args[0].lower() == "close" or args[0].lower() == "exit":
            exit_command()
            break
        else:
           print("This command is unlnown. Try again!")

if __name__ == "__main__":
    main()