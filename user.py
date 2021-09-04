class User:
    """
    Class that generates a new account for a user
    to store passwords
    """
    user_list = [] #The arrar that multiple users will be saved

    def __init__ (self,user_name,password):
        """
        The method that creates an instance of the user class"""
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """
        This is to save a new user into the list of users
        """
        User.user_list.append(self)