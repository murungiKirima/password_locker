class User:
    user_list = []

    def __init__(self,f_name,l_name,password):
        self.f_name = f_name
        self.l_name = l_name
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    def delete_user(self):
        User.user_list.remove(self)

    @classmethod
    def display_user(self):
        return cls.user_list
