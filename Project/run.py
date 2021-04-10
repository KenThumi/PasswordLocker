#!/usr/bin/env python3

# from credentials import Credentials
from user import User


def user(fullname,username,password):
    '''Create a new user user'''
    user = User(fullname,username,password)
    return user


def checkRegistered(user):
    '''checks whether or not a user is registered'''
    return user.checkRegistered()


def registerUser(user):
    '''register a user'''
    return user.registerUser()

def checkUsernameTaken(user):
    '''checks whether or not a username is taken'''
    return user.checkUsernameTaken()

def main():

    while True:
        print('Welcome to Password Locker, are you registered?choose yes or no')
        registered = input()
        registered = registered.lower()

        if registered == 'yes':
            fullname = input('Kindly enter your full name:\n')
            username = input('Kindly enter your username:\n')
            password = input('Kindly enter your password:\n')

            # user = Credentials(username,password)

            if checkRegistered( user(fullname,username,password) ):
                print('registerd')
            else:
                print('You are not registered.')
                break
        
        # when not registered
        elif registered == 'no':
            register = input('Would you like to register? enter yes or no:\n').lower()
            
            if register == 'yes':
                while True:
                    fullname = input('Kindly enter your full name:\n')
                    username = input('Kindly enter your unique username:\n')
                    password = input('Kindly enter your unique password:\n')

                    if checkUsernameTaken( user(username,password) ): #if username taken
                        print('Username Taken')
                        break
                    else:
                        registerUser( user(username,password))
                        print('Registered, Kindly login.')
                        break

            else:
                print('Goodbye')
                break

        #wrong registration entry
        else:
            print('Wrong Response.')
            continue



if __name__ == '__main__':
    main()