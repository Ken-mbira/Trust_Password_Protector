from user import User
import unittest

class User_Tests(unittest.TestCase):
    def setUp(self):
        """
        The setup to run before every test case
        """
        self.new_user = User("Ken","1234")

    def user_generate_test(self):
        self.assertEqual(self.new_user.user_name, "Ken")
        self.assertEqual(self.new_user.password,"1234")

    def user_save_test(self):
        """
        This is to test whether a user can be saved into the list of users
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == "__main__":
    unittest.main()