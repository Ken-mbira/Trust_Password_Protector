from user import User
import unittest

class User_Tests(unittest.TestCase):
    def setUp(self):
        """
        The setup to run before every test case
        """
        self.new_user = User("Ken","1234")