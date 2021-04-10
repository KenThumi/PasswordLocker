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


def checkCredentialsExist(user,application):
    '''Checks whether or not application credentials are exists'''
    return user.checkCredsExists(application)


def generateAppPwd(user,l=10):
    '''generate app pwd'''
    return user.generateAppPwd(l)


def addCredential(user,application,appPwd):
    '''adds an app credetials'''
    user.addCredential(application,appPwd)

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
            while True:
                if checkRegistered( user(fullname,username,password) ):
                    #what you need with the app
                    action = input("Choose what you need as below:\n--------------------------------------------\n-To--Create New Credentials--choose: CNC \n-To--View Credential(s)--choose: VC \n-To--Copy Credential--choose: CC \n-To--Delete Credentials--choose: DC \n-To--Exit--choose: EXIT \n--------------------------------------------\n").lower()

                    if action == 'cnc':
                        application = input('Input the application name to generate password for:\n').lower()

                        if checkCredentialsExist(user(fullname,username,password),application ) == False:
                            while True:
                                generatePwd = input('Do you want to generate password? choose yes or no\n').lower()

                                if generatePwd == 'yes':
                                    while True:
                                        pwdlen = input('Would you like to add length? choose yes or no\n')

                                        if pwdlen == 'yes':
                                            while True:
                                                len = input('Kindly enter length in number:\n')

                                                if len.isnumeric():
                                                    pwd = generateAppPwd(user(fullname,username,password), int(len) )

                                                    addCredential(user(fullname,username,password),application,pwd)

                                                    print(f"Successful,{application} added,generated pwd:{pwd} \n")

                                                    exit()
                                                else:
                                                    print('Kindly enter an integer')
                                                    continue

                                        elif pwdlen == 'no':
                                            while True:
                                                pwd = generateAppPwd(user(fullname,username,password))
                                        
                                                addCredential(user(fullname,username,password),application,pwd)

                                                print(f"Successful,{application} generated pwd:{pwd} \n")

                                                exit()
                                                
                                        else:
                                            print('Wrong response')
                                            continue

                                elif generatePwd == 'no':
                                    while True:
                                        pwd = input("Kindly input password that has alphanumerics, symbol(s),uppercase & lowercase mixture and above 8 characters:\n")

                                        if pwd != '':
                                            addCredential(user(fullname,username,password),application,pwd)

                                            print(f"Successful,{application} generated pwd:{pwd} \n")

                                            exit()
                                        else:
                                            print('Kindly enter password')
                                            continue
                                else:
                                    print("Wrong Response\n")
                                    continue

                        else:
                            print(f'Credentials for application {application} exists')
                            print( '-'*28)

                    elif action == 'vc':
                        pass
                    elif action == 'cc':
                        pass 
                    elif action == 'dc':
                        pass 
                    elif action == 'exit':
                        pass 
                    else:
                        pass
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