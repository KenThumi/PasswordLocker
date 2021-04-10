from user import User

class Credentials(User):
    '''Class to manage all credential matters'''

    # credentials = {'kenneth':'password'}     # main dictionary to handle all credentials

    # def __init__(self,username, password):
    #     '''Initialize each credential with username,password and empty appCredentials'''
    #     super().__init__(username)
    #     self.password = password
    #     self.appCredentials = ''
    
    # def checkRegistered(self):
    #     '''Method check if one is registered'''
    #     return self.username in Credentials.credentials.keys() and self.password in Credentials.credentials.values()


    # def registerUser(self):
    #     '''Registers a new user'''
    #     self.credentials[self.username] = self.password


    # def checkUsernameTaken(self):
    #     '''Checks whether or not the username is taken'''
    #     return self.username in Credentials.credentials.keys()


# obj = Credentials('obj','pwd')

# obj.registerUser()

# print(obj.username in Credentials.credentials.keys() and obj.password in Credentials.credentials.values())