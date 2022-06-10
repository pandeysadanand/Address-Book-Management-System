"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-10 14:26:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-10 14:28:00
    @Title : Ability to create a Contacts in Address Book with first and last names, address,
             city, state, zip, phone number and email...

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

    @staticmethod
    def add_contact():
        """
            Here taking input from user and printing details
        Returns: None

        """
        address_book_name = input("Enter address book name you want to add: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        phone_number = int(input("Enter phone number: "))
        email = input("Enter email: ")
        city = input("Enter city: ")
        state = input("enter state: ")
        zip_code = int(input("Enter zip_code code: "))
        print("----------------------------------------------------------------------------------")
        print("First\tLast\tPhone\tCity\tState\tzip code\tEmail")
        print("-----------------------------------------------------------------------------------")
        print(f"{first_name}\t{last_name}\t{phone_number}\t{city}\t{state}\t{zip_code}\t{email}")
        print("==================================================================================\n")


if __name__ == '__main__':
    address_book_dict = {}
    print("----------------------------------------------------------")
    print("---------!! Welcome to Address Book System!!--------------")
    print("----------------------------------------------------------")
    Contact.add_contact()
