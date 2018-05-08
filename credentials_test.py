from account import Credentials
import unittest

class TestCredentials( unittest.TestCase ):
    def setUp(self):
        self.new_credential = Credentials("murungi","my secret","234")

    def tearDown(self):
        Credentials.list_of_credentials=[]

    def test_init(self):
        self.assertEqual(self.new_credential.user_name,"murungi")
        self.assertEqual(self.new_credential.credential_name,"my secret")
        self.assertEqual(self.new_credential.credential_password,"234")
        
    def test_save_credentials(self):
        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),1)

    def test_save_multiple_credential(self):
        self.new_credential.save_credentials()
        test_credential = Credentials("kj","twitter","kj24")
        test_credential.save_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),2) 

    def test_delete_credential(self):
        self.new_credential.save_credentials()
        test_credential = Credentials("kj","twitter","kj24")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),1)

    def test_find_credential_by_name(self):
        self.new_credential.save_credentials()
        test_credential = Credentials("kj","twitter","kj24")
        test_credential.save_credentials()

        found_credential = Credentials.find_credentials_by_name("kj")
        self.assertEqual(found_credential.credential_name,test_credential.credential_name)

    def test_credential_exists(self):
        self.new_credential.save_credentials()
        test_credential = Credentials("kj","twitter","kj24")
        test_credential.save_credentials()

        credential_exist = Credentials.credential_exists("kj")
        self.assertTrue(credential_exist)

    def test_display_credentials(self):
        self.assertEqual(Credentials.display_all_credentials(), Credentials.list_of_credentials)




if __name__ == '__main__':
    unittest.main()
