phoneBook = {}

def input_error(function):
    def inner(string):
        try:
            return function(string)
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
    if len(args) < 2:
        raise ValueError
    name, phone = args
    phoneBook[name] = phone
    print("Contact added successfully")

@input_error
def change_phone_number(args):
    if args[0] not in phoneBook:
        raise KeyError
    if args[0] in phoneBook:
        name, new_phone = args
        phoneBook[name] = new_phone
    print("Phone number change successfully")

@input_error
def get_phone_number(args):
    print(f"Name:{args[0]}, Phone: {phoneBook[args[0]]}") 
    
        
@input_error
def show_all_contacts(_):
    if len(phoneBook) == 0:
        raise IndexError 
    for name, val in phoneBook.items():
        print(name + ": " + (val))


def exit_command():
    print("Good bye!")


def main():
    while True:
        c = input("Enter a command: ")
        args = c.split(" ")

        if args[0].lower() == "hello":
            greeting_command()
        elif  args[0].lower() == "add":
            add_contact(args[1:])
        elif args[0].lower() == "change":
            change_phone_number(args[1:])
        elif args[0].lower() == "phone":
            get_phone_number(args[1:])
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
