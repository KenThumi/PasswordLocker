#!/usr/bin/env python3

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


def getAllUserCredentials(user):
    '''Gets a list of all credentials'''
    return user.getAllUserCredentials()


def copyCredential(user,application):
    '''Copys credential pair to clipboard'''
    return user.copyCredential(application)


def deleteCredential(user,application):
    '''Delete a particular application password pair from credentials'''
    return user.deleteCredential(application)

def main():

    while True:
        print('Welcome to Password Locker, are you registered?choose yes or no')
        registered = input()
        registered = registered.lower()

        if registered == 'yes':
            fullname = input('Kindly enter your full name:\n')
            username = input('Kindly enter your username:\n')
            password = input('Kindly enter your password:\n')

            if checkRegistered( user(fullname,username,password) ):
                #what you need with the app
                while True:
                    print('-'*44)
                    action = input("Choose what you need as below:\n--------------------------------------------\n-To--Create New Credentials--choose: CNC \n-To--View Credential(s)--choose: VC \n-To--Copy Credential--choose: CC \n-To--Delete Credentials--choose: DC \n-To--Exit--choose: EXIT \n--------------------------------------------\n").lower()

                    if action == 'cnc':
                        application = input('Input the application name to generate password for:\n').lower()

                        if checkCredentialsExist(user(fullname,username,password),application ) == False:
                            while True:
                                generatePwd = input('Do you want to generate password? choose yes or no\n').lower()

                                if generatePwd == 'yes':
                                    while True:
                                        pwdlen = input('Would you like to give password length? choose yes or no\n')

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

                                            print(f"Successful,{application} added,pwd given :{pwd} \n")

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
                        #lists all credentials
                        credentials = getAllUserCredentials(user(fullname,username,password))
                        if credentials != False:
                            print("-"*60)
                            print("Below are your Credentials")
                            print("-"*60)

                            for key,value in credentials.items():
                                print(f">>>>>Application :{key} ,Password :{value}")
                                print('-' * 60)

                            exit()
                        else:
                            print('No Records Found')
                    elif action == 'cc':
                        while True:
                            application = input('Enter application\'s password you want to copy:\n' ).lower()

                            if application != '':
                                copyPwd = copyCredential(user(fullname,username,password), application)

                                if copyPwd != False:
                                    print(f'{application.capitalize()} password copied to clip, paste in your desired location')
                                    exit()
                                else:
                                    print('Application credentials non-existent')
                                    continue
                            else:
                                print('Empty application name')
                                continue

                    elif action == 'dc':
                        while True:
                            application = input("Enter the application to delete:\n").lower()
                            if application != '':
                                delApp = deleteCredential(user(fullname,username,password),application)

                                if delApp:
                                    print(f'{application.capitalize()} and password pair deleted.')
                                    exit()
                                else:
                                    print('Application credentials non-existent')
                                    continue

                            else:
                                print("Empty application name")
                                continue
                    elif action == 'exit':
                        print('Goodbye')
                        exit()
                    else:
                        print('Wrong input.')
                        continue
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

                    if checkUsernameTaken( user(fullname,username,password) ): #if username taken
                        print('Username Taken')
                        break
                    else:
                        registerUser( user(fullname,username,password))
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