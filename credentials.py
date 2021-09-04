from user import User


class Cred:
    """
    This is a class that makes the user credentials for their different accounts
    """
    
    def __init__(self,account_name,user_name,email,password):
        """
        This will construct an instance of the credentials class
        """
        self.account_name = account_name
        self.user_name = user_name
        self.email = email
        self.password = password

    credential_list = []

    def save_credential(self):
        """
        This will add a newly created credential to the credentials list
        """
        Cred.credential_list.append(self)

    def delete_credential(self):
        """
        This method will delete a credential from the credential list
        """
        Cred.credential_list.remove(self)