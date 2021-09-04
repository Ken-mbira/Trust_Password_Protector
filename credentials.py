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

    def display_credentials(self):
        """
        This will display all the credentials in the credentials list
        """
        return Cred.credential_list

    @classmethod
    def find_account(cls,account):
        """
        This will return the credentials after being given an account name
        Args:
            account_name: This is the account of the credentials that will be used to locate the credential
        """
        for credential in cls.credential_list:
            if credential.account_name == account:
                return credential