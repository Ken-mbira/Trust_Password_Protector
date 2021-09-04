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

if __name__ == '__main__':
    unittest.main()
