"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-10 18:26:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-10 18:35:00
    @Title : Ability to add a new Contact to Address Book

"""


class Contact:
    def __init__(self, first_name, last_name, phone, email, city, state, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.city = city
        self.state = state
        self.zip_code = zip_code


class Addressbook:

    def __init__(self, address_book_name):
        """
        This is constructor
        Args:
            address_book_name: Taking addressbook name from user
        """
        self.address_book_name = address_book_name
        self.contact_dict = {}


def add_address_book():
    """
        Adding address book name and also checking book present or not. If present then don't add
        but if not then add book.
    Returns: None

    """
    try:
        address_book_name = input("Enter address book name you want to add: ")
        address_book = Addressbook(address_book_name)
        address_obj = address_book_dict.get(address_book_name)
        if address_obj:
            print("Book name already exist")
            return
        address_book_dict.update({address_book_name: address_book})
        print("{} added successfully".format(address_book_name))
        print("----------------------------------\n")
    except Exception as e:
        print("Please enter valid book name", e)


def add_contact():
    """
    Adding contact to address book but before that I'm checking contact is present or not. If not
    then add that contact otherwise don't add
    Returns: None

    """
    try:
        address_book_name = input("Enter book name to add contact: ")
        book_obj = address_book_dict.get(address_book_name)
        if not book_obj:
            print("Book not found")
            print("----------------")
            return
        first_name = input("Enter first name: ")
        if book_obj.contact_dict.get(first_name):
            print("Contact already exist")
            print("------------------------")
            return
        last_name = input("Enter last name: ")
        phone_number = int(input("Enter phone number: "))
        email = input("Enter email: ")
        city = input("Enter city: ")
        state = input("enter state: ")
        zip_code = int(input("Enter zip_code code: "))
        contact = Contact(first_name, last_name, phone_number, email, city, state, zip_code)
        book_obj.contact_dict.update({contact.first_name: contact})
        print("Contact added successfully")
        print("---------------------------")
    except Exception as e:
        print("Please enter correct book name", e)


def display_contact():
    """
    Displaying the contacts present in particular address book
    Returns: None

    """
    try:
        address_book_name = input("Enter book name to display contact: ")
        book_obj = address_book_dict.get(address_book_name)
        if not book_obj:
            print("Book not found")
            return
        print("----------------------------------------------------")
        print("First\tLast\tPhone\tCity\tState\tzip code")
        print("----------------------------------------------------")
        for k, v in book_obj.contact_dict.items():
            print(f"{v.first_name}\t{v.last_name}\t{v.phone}\t{v.city}\t{v.state}\t{v.zip_code}")
        print("====================================================\n")
    except Exception as e:
        print("Please enter correct book name!")


if __name__ == '__main__':
    address_book_dict = {}
    print("!! Welcome to address book management system !!")
    print("-------------------------------------------------\n")
    more_choice = True
    while more_choice:
        print("Choose below option to perform task")
        print("===================================")
        print("1. Add an address book\n"
              "2. Add contact\n"
              "3. Display contact\n"
              "0. Exit address book...")
        choice = {1: add_address_book, 2: add_contact, 3: display_contact}
        print()
        try:
            user_input = int(input("Enter choice: "))
            if user_input != 0:
                choice.get(user_input)()
            elif user_input == 0:
                more_choice = False
                print("Existing Employee wage system !!")
                print()
        except Exception as e:
            print("Please enter valid input ↑", e)
            print()
