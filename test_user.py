from user import User
import unittest

class User_Tests(unittest.TestCase):
    def setUp(self):
        """
        The setup to run before every test case
        """
        self.new_user = User("Ken","1234")

    def user_generate(self):
        self.assertEqual(self.new_user.user_name, "Ken")
        self.assertEqual(self.new_user.password,"1234")

if __name__ == "__main__":
    unittest.main()