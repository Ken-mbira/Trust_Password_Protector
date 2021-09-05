#!/usr/bin/env python3.6.0

from user import User
from credentials import Cred

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