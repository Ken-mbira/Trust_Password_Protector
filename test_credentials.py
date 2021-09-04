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

    def tearDown(self):
        """
        This will run after every test runs and clear up the code
        """
        Cred.credential_list = []

    def test_save_cred(self):
        """
        This will test on whether we can add a credential to the credentials list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Cred.credential_list),1)

    def test_multiple_save(self):
        """
        This will test whether we can save multiple credentials
        """
        self.new_credential.save_credential()
        other_credential = Cred("Twitter","Mbira","mbira@ken.com","1234")
        other_credential.save_credential()
        self.assertEqual(len(Cred.credential_list),2)

    def test_delete_credential(self):
        """
        This will test whether we can delete a credential
        """
        self.new_credential.save_credential()
        other_credential = Cred("Twitter","Mbira","mbira@ken.com","1234")
        other_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Cred.credential_list),1)

    def test_display_credentials(self):
        """
        This will check if we can display all the credentials that we have in the credentials list
        """
        self.new_credential.save_credential()
        other_credential = Cred("Twitter","Mbira","mbira@ken.com","1234")
        other_credential.save_credential()
        self.assertEqual(Cred.display_credentials(self),Cred.credential_list)

    def test_find_account(self):
        """
        This will check if we can find a credential by the name of the account
        """
        self.new_credential.save_credential()
        other_credential = Cred("Twitter","Mbira","mbira@ken.com","1234")
        other_credential.save_credential()

        found_credential = Cred.find_account("Twitter")

        self.assertEqual(other_credential.user_name,found_credential.user_name)

    def test_find_account(self):
        """
        This will check if we can find a credential by the name of the account
        """
        self.new_credential.save_credential()
        other_credential = Cred("Twitter","Mbira","mbira@ken.com","1234")
        other_credential.save_credential()

        found_credential = Cred.find_account("Twitter")

        self.assertEqual(other_credential.user_name,found_credential.user_name)

    def test_found_account(self):
        """
        This will check if a boolean is returned on finding or not finding a credential
        """
        self.new_credential.save_credential()
        other_credential = Cred("Twitter","Mbira","mbira@ken.com","1234")
        other_credential.save_credential()

        found = Cred.credential_found("Twitter")

        self.assertTrue(found)

if __name__ == "__main__":
    unittest.main()