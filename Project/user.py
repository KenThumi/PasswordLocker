
class User():
    '''User class to manage users'''


    # def __init__(self,username):
    #     '''Initialize every user with a username'''

    #     self.username = username


    users = {'kenneth':{'password':'password','fullname':'kenmwas'}}     # main dictionary to handle all credentials

    def __init__(self,fullname,username, password):
        '''Initialize each user with username,password'''
        self.fullname = fullname
        self.username = username
        self.password = password
    
    def checkRegistered(self):
        '''Method check if one is registered'''
        return self.username in User.users.keys() and self.password == User.users[self.username ]['password']


    def registerUser(self):
        '''Registers a new user'''
        self.users[self.username] = {'password':self.password,'fullname':self.fullname}
    


    def checkUsernameTaken(self):
        '''Checks whether or not the username is taken'''
        return self.username in User.users.keys()
   

    def addCredential(self,application,appPassword):
        '''adds an app credetials'''
        self.users[self.username]['credentials'] = {'appName':application.lower(),
                                                    'password':appPassword}


    def checkCredsExists(self,application):
        '''Checks whether or not application credentials are exists'''
        if self.users[self.username].get('credentials') != None:
            return application.lower() in self.users[self.username]['credentials'].values()
        else:
            return False
                                    

# class Credentials:
#     '''Class to manage all credential matters'''

#     credentials = {'lorem':'ipsum'}     # main dictionary to handle all credentials



obj = User('ken thums','thumise','hsajkhah')
obj.registerUser()

obj.addCredential('facebookk','loremipsum')
#print(obj.users[obj.username]['credentials'])
# obj.registerUser()
print(obj.checkCredsExists('facebook'))

#print('password' in  obj.users['password'] )


