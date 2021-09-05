#!/usr/bin/env python3

from termcolor import colored
import pyfiglet
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from user import User
from credentials import Cred
import time
import getpass

def create_user(name,pin):
    """
    This will create a new user
    """
    new_user = User(name,pin)
    return new_user

def delete_user(user):
    """
    Function to delete a user
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

def display_users():
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
        txt = "TRUST"
        banner = pyfiglet.figlet_format(txt, font="isometric2", justify="center")
        print(colored(banner,'green'))
        print('\n')
        table = Table(title = f"Use the following commands to help you get around: ")
        table.add_column("Command", justify="right", style="green", no_wrap=True)
        table.add_column("Instruction", style="red")

        table.add_row(f"lg", f"To login to an account")
        table.add_row(f"du", f"To display a list of users who have accounts on this app")
        table.add_row("x", f"To leave the application")
        console = Console()
        console.print(table)
        
        choice = input().lower()
        if choice == "lg":
            have_account = input("Do you have an account? Y/N: ").lower()
            if have_account.startswith("n"):
                print('\n')
                user_name = input("Enter your user name: ")
                user_password = getpass.getpass("Enter you pin: ")
                save_user(create_user(user_name,user_password))

                print("Please wait...")
                time.sleep(1)
                print(colored(f"Congratulations {user_name} your account was created successfully!","green"))
                print('\n')
            print("Please login to your account...")
            print('\n')
            user_name_input = input("Enter your user name: ")
            user_password_input = input("Enter your password: ")
            print('\n')
            time.sleep(0.5)
            if authenticate_user(user_name_input,user_password_input):
                print(f"Welcome {user_name_input}, you have successfully logged in to your account.")
                while True:
                    table = Table(title = f"Use the following commands to help you get around: ")
                    table.add_column("Command", justify="right", style="green", no_wrap=True)
                    table.add_column("Instruction", style="red")

                    table.add_row(f"nc", f"To create a new credential")
                    table.add_row(f"dc", f"To view all your credentials")
                    table.add_row("fc", f"To find a specific credential")
                    table.add_row("xc","To delete a credential")
                    table.add_row("x","To leave your account")
                    console = Console()
                    console.print(table)
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
                            print('\n')
                            for credential in display_credentials():
                                table = Table(title = f"{credential.account_name}")
                                table.add_column("Detail", justify="right", style="cyan", no_wrap=True)
                                table.add_column("Data", style="magenta")

                                table.add_row(f"Account", f"{credential.account_name}")
                                table.add_row(f"User Name", f"{credential.user_name}")
                                table.add_row("Email", f"{credential.email}")
                                table.add_row("Password", f"{credential.password}")
                                console = Console()
                                console.print(table)
                                print('\n')
                    elif user_choice == "fc":
                        search_account_name = input("Enter the name of the account that you are searching for: ")
                        print('\n')
                        if credential_found(search_account_name):
                            account = find_account(search_account_name)
                            table = Table(title = f"{account.account_name}")
                            table.add_column("Detail", justify="right", style="cyan", no_wrap=True)
                            table.add_column("Data", style="magenta")

                            table.add_row(f"Account", f"{account.account_name}")
                            table.add_row(f"User Name", f"{account.user_name}")
                            table.add_row("Email", f"{account.email}")
                            table.add_row("Password", f"{account.password}")
                            console = Console()
                            console.print(table)
                            print('\n')
                        else:
                            print(f"""
                    Sorry but the inputted account name {search_account_name} does not seem to exist!""")

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
                                print(f"""
                    Sorry but the inputted account name {search_account_name} does not seem to exist!""")

                    elif user_choice == "x":
                        break
            else:
                print("Sorry, either your username or password is wrong")
        elif choice == "du":
            user_name = input("Please enter your username to verify that you are a user on this application: ")
            if user_found(user_name):
                print("The users in this application are: ")
                for user in display_users():
                    print(f"{user.user_name}")
            else:
                print("Sorry but you do not seem to be a user on the application and so cannot have the list of users!")
                    
        elif choice == "x":
            txt = "GOODBYE"
            banner = pyfiglet.figlet_format(txt, font="standard", justify="center")
            print(colored(banner,'red'))
            break



if __name__ == '__main__':
    main()