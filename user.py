class User:
    """
    Class that generates new instances of contacts
    """

    def __init__(self,user_name, password):
        """
        This will construct an object of the instance of the class user
        """
        self.user_name = user_name
        self.password = password

    user_list = [] #This is the list of the users

    def save_user(self):
        User.user_list.append(self)