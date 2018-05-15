import unittest
from account import User

"""Test class that defines test cases for the user class behaviour"""
class TestUser(unittest.TestCase):
    def setUp(self):
        """Set Up Method to run before each test case to check if the class has been instantiated correctly"""
        self.new_user = User("kj","Muru","12345")

    def test_init(self):
        """Test to ensure that the object is initialized properly"""
        self.assertEqual(self.new_user.f_name,"kj")
        self.assertEqual(self.new_user.l_name,"Muru")
        self.assertEqual(self.new_user.password,"12345")

    def test_save_user(self):
         """Method that tests whether a user have been successfully saved"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        """tearDown method that does clean up after each test case has run."""
        User.user_list = []

    def test_multiple_user(self):
        """test_save_multiple_users to check if we can save multiple user objects"""
        self.new_user.save_user()
        test_user = User("mm","yy","123")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        """test_delete_users to check if we can delete user objects"""
        self.new_user.save_user()
        test_user = User("mm","yy","123")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_user(self):
        """test_display_users to check if we can display user objects"""
        self.assertEqual(User.display_user(),User.user_list)

    def test_user_exists(self):
        """test_check_users to check if user objects exists"""
        self.new_user.save_user()
        test_user = User("mm","yy","123")
        test_user.save_user()

        found_user = User.user_exist("mm")

        self.assertTrue(found_user)

if __name__ == '__main__':
    unittest.main()
