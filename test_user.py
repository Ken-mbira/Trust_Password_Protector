import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("James","1234")

    def test__init(self):
        """
        test _init test if the object is initialized properly
        """
        self.assertEqual(self.new_user.user_name,"James")
        self.assertEqual(self.new_user.password,"1234")

    def test_save_user(self):
        """
        Test that checks if a user can be saved into the userlist
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        """
        This is a method to run when each test has finished running
        """
        User.user_list = []

    def test_multiple_users(self):
        """
        This test will check if multiple users can be saved into the user list
        """
        self.new_user.save_user()
        other_user = User("Mbira","1234")
        other_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        """
        This test will check if a user can be deleted
        """
        self.new_user.save_user()
        other_user = User("Kinuthia","4321")
        other_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_user(self):
        """
        This will check if a list of users can be displayed
        """
        self.new_user.save_user()
        other_user = User("Mbira","1234")
        other_user.save_user()
        self.assertEqual(User.display_users(self),User.user_list)

    def test_find_user(self):
        """
        This will check if we can locate a user by their name
        """
        self.new_user.save_user()
        other_user = User("Mbira","4321")
        other_user.save_user()

        found_user = User.find_user("Mbira")

        self.assertEqual(found_user.password,other_user.password)

    def test_assert_found(self):
        """
        This will check that the method to return a boolean if the user is found or not is working
        """
        self.new_user.save_user()
        other_user = User("Mbira","4321")
        other_user.save_user()
        
        user_found = User.user_found("Mbira")

        self.assertTrue(user_found)


if __name__ == '__main__':
    unittest.main()
