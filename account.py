class User:
    user_list = []

    def __init__(self,f_name,l_name,password):
        """function that creates user object"""
        self.f_name = f_name
        self.l_name = l_name
        self.password = password

    def save_user(self):
        """function that saves users"""
        User.user_list.append(self)

    def delete_user(self):
        """function that deletes users"""
        User.user_list.remove(self)

    @classmethod
    def display_user(self):
        """function that displays users"""
        return User.user_list

    @classmethod
    def find_user_by_name(cls,name):
        """function that finds users by name"""
        for user in cls.user_list:
            if user.f_name == name:
                return user

    @classmethod
    def user_exist(cls,f_name):
        """function that checks if users exists"""
        for user in cls.user_list:
            if user.f_name == f_name:
                return True

        return False



class Credentials:
    def __init__ (self,user_name, credential_name , credential__password):
        """function that creates credentials"""
        self.user_name = user_name
        self.credential_name =credential_name
        self.credential_password =credential__password

    list_of_credentials = []

    def save_credentials(self):
        """function that saves credentials"""
        self.list_of_credentials.append(self)

    def delete_credentials(self):
        """function that deletes credentials"""
        Credentials.list_of_credentials.remove(self)

    @classmethod
    def find_credentials_by_name(cls,name):
        """function that finds credentials by name"""
        for credential in cls.list_of_credentials:
            if credential.user_name == name:
                return credential

    @classmethod
    def credential_exists(cls,name):
        """function that checks if credentials exists"""
        for credential in cls.list_of_credentials:
            if credential.user_name == name:
                return True

    @classmethod
    def display_all_credentials(cls):
        """function that displays Credentials"""
        return cls.list_of_credentials
