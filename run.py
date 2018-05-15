#!/usr/bin/env python3.6

from account import User, Credentials

def create_user(f_name,l_name,password):
    """function that creates new users"""
    new_user =  User(f_name,l_name,password)
    return new_user

def save_users(user):
    """function that saves users"""
    user.save_user()

def del_user(user):
    """function that deletes users"""
    user.delete_user()

def display_user():
    """function that displays users saved"""
    return User.display_user()

def user_exists(name):
    """function that checks whether a user exists"""
    return User.user_exist(name)

def find_users(name):
    """function that finds users by their first name"""
    return  User.find_user_by_name(name)



def create_credential(user_name,credential_name,credential_password):
    """function that creates new credentials in user account"""
    new_run_credential = Credentials(user_name,credential_name,credential_password)
    return new_run_credential

def save_credential(credential):
    """function that saves credentials in user account"""
    credential.save_credentials()

def delete_credential_run(credential):
    """function that deletes credentials in user account"""
    credential.delete_credentials()

def display_all_credentials():
    """function that displays credentials in user account"""
    return Credentials.display_all_credentials()

def credential_exists(credential):
    """function that checks if credentials exist in credentials in user account"""
    return Credentials.credential_exists(credential)

def main():
    print("Welcome, What's your name?")
    user_name = input()

    print('\n')
    print(f"Hello {user_name}, what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes :  \n lg -Login to account, \n cc - create a new user account,\n dc - display users,\n dl -Delete user account, \n ex -exit account ")
        short_code = input().lower()

        if short_code == 'lg':
            print('\n')
            print("Enter you login name (use your first name) ...")
            login_name = input()
            print("Enter you login password ...")
            login_password = input()

            if user_exists(login_name):
                print(f"Welcome {login_name}")
                logged_in_user = find_users(login_name)

                if logged_in_user.password == login_password:
                    print('\n')
                    print(f" {logged_in_user.f_name}, you are now logged into your user account.")
                    print('\n')

                while True:
                    print ('\n')
                    print("Please use the following short-codes.")
                    print ('-'*10)
                    print("cc - Add a credential.")
                    print("dc - Display credentials.")
                    print("ch - Check if user exists")
                    print("dl - Delete a credential.")
                    print("ex - Exit")
                    short_code1 = input()

                    credential_user_name = logged_in_user.f_name

                    if short_code1 == 'cc':
                        print('\n')
                        print("What to save some credentials?")

                        print("Enter your user Name")
                        user_name = input()

                        print("Enter a credential Name")
                        credential_name = input()

                        print("Enter a credential password")
                        credential_password = input()

                        save_credential(create_credential(user_name,credential_name,credential_password))
                        print('\n')
                        print(f"Credential {credential_name} has been created.")
                        print('\n')

                    elif short_code1 == 'dc':
                        if display_all_credentials():
                            print("Here are the saved credentials for {credential_user_name}.")

                        for user in display_all_credentials():
                            print(f"{credential.user_name} {credential.credential_name}")
                            print('\n')

                        else:
                            print ("\n")
                            print("There are NO saved credentials")
                            print ("\n")

                    elif short_code1 == 'dl':
                        if Credentials.credential_exists(credential_user_name):
                            print("Enter the credential to delete.")
                            credential_for_delete = input()

                            for credential in Credentials.display_all_credentials():
                                if credential.credential_name == credential_for_delete:
                                    credential.delete_credentials()
                                    print ("\n")
                                    print(f"Deleted {credential_for_delete}")
                                    print("\n")

                                else:
                                    print ("\n")
                                    print("The entered credential doesn't exist.")
                                    print ("\n")
                        else:
                            print ("\n")
                            print("There are NO saved credentials")
                            print ("\n")

                    elif short_code1 == 'ex':
                        print('\n')
                        print("Goodbye ...")
                        print('\n')
                        break

            else:
                print('\n')
                print("You don't have any users saved yet. Use short code 'cc' to create user account.")
                print('\n')

        if short_code == 'cc':
            print("-" * 10)
            print("Are you a new User? Register")

            print("Enter your First Name")
            f_name = input()

            print("Enter your Last Name")
            l_name = input()

            print("Enter a password")
            password = input()

            save_users(create_user(f_name,l_name,password))
            print('\n')
            print(f"User {f_name} {l_name} has been created. You can now log in and save your credentials.")
            print('\n')

        elif short_code == 'dc':
            if display_user():
                print("Here are the saved users.")
                print('\n')

                for user in display_user():
                    print(f"{user.f_name} {user.l_name}")
                    print('\n')

            else:
                print('\n')
                print("You don't have any users saved yet. Use short code 'cc' to create user account.")
                print('\n')

        elif short_code == 'dl':
            print('\n')
            print(f"Enter User's first name to check if the user exists. ")
            delete_name = input()

            if user_exists(delete_name):
                del_user(find_users(delete_name))
                print ('-'*10)
                print(f"User account {delete_name} has been DELETED")
                print ("\n")

            else:
                print ("\n")
                print("The entered user account doesn't exist.")
                print ("\n")

        elif short_code == "ex":
            print('\n')
            print("Goodbye ...")
            break

        else:
            print("I really didn't get that, please use the short-codes provided.")


if __name__ == '__main__':
    main()
