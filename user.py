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