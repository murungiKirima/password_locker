#!/usr/bin/env python3.6

from account import User

def create_user(f_name,l_name,password):
    new_user =  User(f_name,l_name,password)
    return new_user

def save_users(user):
    user.save_user()

def del_user(user):
    user.delete_user()

def display_user():
    return User.display_user()

def main():
    print("Welcome, What's your name?")
    user_name = input()

    print(f"Hello {user_name}, what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : \n cc - create a new user account,\n dc - display users,\n fc -Check if a user exists, \n lg -Login to account \n ex -exit account ")
        short_code = input().lower()

        if short_code == 'cc':
            print("-" * 10)
            print("New contact")

            print("First Name ...")
            f_name = input()

            print("Last Name ...")
            l_name = input()

            print("Password ...")
            password = input()

            save_users(create_user(f_name,l_name,password))
            print('\n')
            print(f"New User {f_name} {l_name} created")
            print('\n')

        elif short_code == 'dc':
            if display_user():
                print("Here is a list of your Users.")
                print('\n')

                for user in display_user():
                    print(f"{user.f_name} {user.l_name}")
                    print('\n')

            else:
                print('\n')
                print("You don't have any users saved yet.")
                print('\n')

if __name__ == '__main__':
    main()
