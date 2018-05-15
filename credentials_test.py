from account import Credentials
import unittest

"""Test class that defines test cases for the Credentials class behaviour"""
class TestCredentials( unittest.TestCase ):
    def setUp(self):
        """Set Up Method to run before each test case to check if the class has been instantiated correctly"""
        self.new_credential = Credentials("murungi","my secret","234")

    def tearDown(self):
        """tearDown method that does clean up after each test case has run."""
        Credentials.list_of_credentials=[]

    def test_init(self):
        """Test to ensure that the object is initialized properly"""
        self.assertEqual(self.new_credential.user_name,"murungi")
        self.assertEqual(self.new_credential.credential_name,"my secret")
        self.assertEqual(self.new_credential.credential_password,"234")

    def test_save_credentials(self):
        """Method that tests whether a Credentials have been successfully saved"""
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),1)

    def test_save_multiple_credential(self):
        """Method that tests whether a multiple Credentials have been successfully saved"""
        self.new_credential.save_credentials()
        test_credential = Credentials("kj","twitter","kj24")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),2)

    def test_delete_credential(self):
        """Method that tests whether credentials have been deleted successfully"""
        self.new_credential.save_credentials()
        test_credential = Credentials("kj","twitter","kj24")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),1)

    def test_find_credential_by_name(self):
        """Method that tests whether a credential has been found successfully"""
        self.new_credential.save_credentials()
        test_credential = Credentials("kj","twitter","kj24")
        test_credential.save_credentials()

        found_credential = Credentials.find_credentials_by_name("kj")
        self.assertEqual(found_credential.credential_name,test_credential.credential_name)

    def test_credential_exists(self):
        """Method that tests whether credential exists"""
        self.new_credential.save_credentials()
        test_credential = Credentials("kj","twitter","kj24")
        test_credential.save_credentials()

        credential_exist = Credentials.credential_exists("kj")
        self.assertTrue(credential_exist)

    def test_display_credentials(self):
        """Method that tests whether credential are being displayed"""
        self.assertEqual(Credentials.display_all_credentials(), Credentials.list_of_credentials)




if __name__ == '__main__':
    unittest.main()
