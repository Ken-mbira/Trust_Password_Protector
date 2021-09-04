import unittest
from credentials import Cred

class Test_Credentials(unittest.TestCase):
    """
    This is the class to test the credentials to make sure all behaviors are working
    Args: 
        unittest.TestCase: This is a class of the unittest module that will bring some testing features
    """

    def setUp(self):
        """
        This is to be run before every test is carried out
        """
        self.new_credential = Cred("Insta","mbira","mbiraken@insta.com","1234")

    def test__init(self):
        """
        This will check if one an create a new credential
        """
        self.assertEqual(self.new_credential.account_name,"Insta")
        self.assertEqual(self.new_credential.email,"mbiraken@insta.com")
        self.assertEqual(self.new_credential.password,"1234")
        self.assertEqual(self.new_credential.user_name,"mbira")

if __name__ == "__main__":
    unittest.main()