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
        """
        This will add a new user to the user list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        This will remove a user from the user list
        """
        User.user_list.remove(self)

    def display_users(self):
        """
        This will return all the users in the users list
        """
        return User.user_list

    @classmethod
    def find_user(cls,name):
        """
        Method that takes in a user's name and returns the users information
        Args:
            name: This is the user's name that is to be found
        Returns:
            user details of the person that matches the name
        """
        for user in cls.user_list:
            if user.user_name == name:
                return user

    @classmethod
    def user_found(cls,name):
        """
        Method that searches the user list for the user and returns either true or false depending on whether the user is found
        Args:
            name: This is the user's name being searched for
        """
        user_names = []
        for user in cls.user_list:
            user_names.append(user.user_name)

        if name in user_names:
            return True
        return False

    @classmethod
    def user_auth(cls,name,password):
        """
        This returns a boolean on whether the credentials given during logging in are correct
        """
        for user in cls.user_list:
            if user.user_name == name and user.password == password:
                return True
        return False