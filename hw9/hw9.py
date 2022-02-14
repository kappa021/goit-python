phoneBook = {}


greeatCommand = ("hello", )
addCommand = ("add", )
changePhoneCommand = ("change", )
showPhoneNumber = ("phone", )
showPhoneBook = ("show all", )
exitCommand = ("good bye", "close", "exit")


def input_error(function):
    def inner(string):
        try:
            return function(string)
        except KeyError:
            return "Not such name exist."
        except ValueError:
            return "Enter the name and number after the command separated by a space."
        except IndexError:
            return "Phone book is empty."
    return inner



def greeting_command(string):
    return "How can I help you?"

@input_error
def add_contact(string):
    name, phone = string.split(" ")
    phoneBook[name] = phone
    return "Contact added successfully"

@input_error
def change_phone_number(string):
    name, new_phone = string.split(" ")
    for key, val in phoneBook.items():
        if key == name:
            
    pass

@input_error
def get_phone_number(string):
    return f"Name: {string}, Phone: {phoneBook[string]}"

@input_error
def show_all_contacts(string):
    allContacts = []
    for value in phoneBook:
        allContacts.append(f"Name: {value}, Phone:{phoneBook[value]}")
    return allContacts


def exit_command(string):
    return "Good bye!"


def main():
    while True:
        c = input("Enter a command: ")
        command = c.lower()
        if command in greeatCommand:
            greeting_command()
        elif  command in addCommand:
            add_contact()
        elif command in changePhoneCommand:
            change_phone_number()
        elif command in showPhoneNumber:
            get_phone_number()
        elif command in showPhoneBook:
            show_all_contacts()
        elif command in exitCommand:
            exit_command()
            break
        else:
            "This command is unlnown. Try again!"

if __name__ == "__name__":
    main()
