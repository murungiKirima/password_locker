import unittest
from account import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("kj","Muru","12345")

    def test_init(self):
        self.assertEqual(self.new_user.f_name,"kj")
        self.assertEqual(self.new_user.l_name,"Muru")
        self.assertEqual(self.new_user.password,"12345")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        User.user_list = []

    def test_multiple_user(self):
        self.new_user.save_user()
        test_user = User("mm","yy","123")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("mm","yy","123")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_display_user(self):
        self.assertEqual(User.display_user(),User.user_list)

    def test_user_exists(self):
        self.new_user.save_user()
        test_user = User("mm","yy","123")
        test_user.save_user()

        found_user = User.user_exist("123")

        self.assertTrue(found_user)

if __name__ == '__main__':
    unittest.main()
