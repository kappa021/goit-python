phoneBook = {}


greetCommand = ("hello", )
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



def greeting_command():
    print("How can I help you?")

@input_error
def add_contact(string):
    name, phone = string.split(" ")
    phoneBook[name] = phone
    print("Contact added successfully")

@input_error
def change_phone_number(string):
    name, new_phone = string.split(" ")
    phoneBook[name] = new_phone

@input_error
def get_phone_number(string):
    print(f"Name: {string}, Phone: {phoneBook[string]}")

@input_error
def show_all_contacts():
    allContacts = []
    for value in phoneBook:
        allContacts.append(f"Name: {value}, Phone:{phoneBook[value]}")
    return allContacts


def exit_command():
    print("Good bye!")


def main():
    while True:
        c = input("Enter a command: ")
        command = c.lower()
        if command in greetCommand:
            greeting_command()
        elif  command in addCommand:
            add_contact(c)
        elif command in changePhoneCommand:
            change_phone_number(c)
        elif command in showPhoneNumber:
            get_phone_number(c)
        elif command in showPhoneBook:
            show_all_contacts()
        elif command in exitCommand:
            exit_command()
            break
        else:
           print("This command is unlnown. Try again!")

if __name__ == "__main__":
    main()
