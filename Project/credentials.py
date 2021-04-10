from user import User

class Credentials(User):
    '''Class to manage all credential matters'''
    

    # def __init__(self,fullname,username, password,credentials,application,appPassword):
    #     '''Initialize each credential with username,password and empty appCredentials'''
    #     super().__init__(fullname,username,password)
    #     self.credentials = credentials

    
    # def checkCredentialsExist(self):
    #     '''check if certain app credentials exists'''
    #     if self.users.get('credentials') != None:
    #         return self.application in self.users['credential'].keys()

    
    # def addCredential(self):
    #     '''adds an app credetials'''
    #     self.users[self.username] = {'password':self.password,
    #                                  'fullname':self.fullname,
    #                                  'credentials':{'appName':self.application,
    #                                                 'password':self.appPassword}
    #                                 }


# obj = Credentials('kenn')

# obj.registerUser()

# print(obj.username in Credentials.credentials.keys() and obj.password in Credentials.credentials.values())