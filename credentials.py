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