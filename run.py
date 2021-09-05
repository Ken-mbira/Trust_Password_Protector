#!/usr/bin/env python3

from user import User
from credentials import Cred
import time

def create_user(name,pin):
    """
    This will create a new user
    """
    new_user = User(name,pin)
    return new_user

def delete_user(user):
    """
    Function to delete a credential
    """
    user.delete_user()

def save_user(user):
    """
    This is a function that adds a user to the user list
    """
    user.save_user()

def authenticate_user(username,password):
    """
    This function will authenticate a user upon login
    """
    return User.user_auth(username,password)

def display_user():
    """
    This will show all the users that have an account
    """
    return User.display_users()

def find_user(name):
    """
    This will find a specific user account
    """
    return User.find_user(name)

def user_found(name):
    """
    This will return a boolean whether or not a user has been found
    """
    return User.user_found(name)

def create_credential(account,username,email,password):
    """
    This will create a credential
    """
    new_credential = Cred(account,username,email,password)
    return new_credential

def save_credential(credential):
    """
    This will add a credential to the list of credentials
    """
    credential.save_credential()

def delete_credential(credential):
    """
    This will remove a credential from the list of the credentials list
    """
    credential.delete_credential()

def display_credentials():
    """
    This will display the list of the credentials in the credential list
    """
    return Cred.display_credentials()

def find_account(account):
    """
    This will find the credential by the account name
    """
    return Cred.find_account(account)

def generate_password(length):
    """
    This function will geneate a random password after being given a desired length
    """
    return Cred.password_generator(length)

def credential_found(account):
    """
    This function will return a boolean on whether a credential has been found according to an account name
    """
    return Cred.credential_found(account)


def main():
    while True:
        print("""
    Hello and welcome to TRUST

Use the following commands to help you get around:
(i) "n" => To create a new account
(ii)"lg" => To login to an existing account
                """,)
        
        choice = input().lower()
        if choice == "n":
            print('\n')
            print("Enter your user name:")
            user_name = input()
            print("Enter your password:")
            user_password = input()
            save_user(create_user(user_name,user_password))

            print("Please wait...")
            time.sleep(1)
            print("CONGRATULATIONS YOUR ACCOUNT HAS BEEN CREATED.")
            print('\n')
            print("Please login to your account...")
            print("Enter your user name:")
            user_name_input = input()
            print("Enter your password:")
            user_password_input = input()
            print('\n')
            time.sleep(0.5)
            if authenticate_user(user_name_input,user_password_input):
                print(f"Welcome {user_name}, you have successfully logged in to your account.")
                while True:
                    print("""
                    You can use the following commands to get around:
                    1. "nc" => To create a new credential
                    2. "dc" => To view all your credentials
                    3. "fc" => To find a specific credential
                    4. "xc" => To delete a credential
                    """)
                    user_choice = input().lower()
                    if user_choice == "nc":
                        print("To create a new credential input the following fields:")
                        print('\n')
                        print()
                        account_name = input("enter your account name: ")
                        print('\n')
                        credential_user_name = input("Enter your username in the account: ")
                        print('\n')
                        user_email = input("Enter your email: ")
                        print('\n')
                        credential_password_choice = input("Do you wish to have a password generated for you automatically? Y/N : ").lower()
                        print('\n')
                        if credential_password_choice.startswith("y"):
                            desired_length = int(input("Enter the length of the password you wish to generate, only digits: "))
                            credential_password = generate_password(desired_length)
                        elif credential_password_choice.startswith("n"):
                            credential_password = int(input("Enter your credential password"))
                        save_credential(create_credential(account_name,credential_user_name,user_email,credential_password))
                        print('\n')
                        print(f"YOUR CREDENTIAL CREATION FOR YOUR {account_name} ACCOUNT WAS SUCCESSFUL!")
                    elif user_choice == "dc":
                        if display_credentials():
                            print("Here are the saved credentials:")
                            for credential in display_credentials():
                                print(f"""
                    
                      Platform  =>  {credential.account_name}
                      Username  =>  {credential.user_name}   
                      Email     =>  {credential.email}       
                      Password  =>  {credential.password}    """)

                    elif user_choice == "fc":
                        search_account_name = input("Enter the name of the account that you are searching for: ")
                        account = find_account(search_account_name)
                        print(f"""
                      Platform  =>  {account.account_name}
                      Username  =>  {account.user_name}   
                      Email     =>  {account.email}       
                      Password  =>  {account.password}    """)

                    elif user_choice == "xc":
                            search_account_name = input("Please enter the account name of the credential you would like to be deleted:")
                            account = find_account(search_account_name)
                            if credential_found(search_account_name):
                                confirmation = input(f"Are you sure, this action will permanently remove {search_account_name} from your list of credentials. Y/N: ").lower()
                                if confirmation.startswith("y"):
                                    delete_credential(account)
                                else:
                                    print(f"The account {search_account_name} was not deleted.")
                            else:
                                print("Sorry but the inputted account name does not seem to exist!")

                    elif user_choice == "xa":
                        break
            else:
                print("Sorry, either your username or password is wrong")


if __name__ == '__main__':
    main()