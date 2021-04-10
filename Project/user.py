
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
   



# class Credentials:
#     '''Class to manage all credential matters'''

#     credentials = {'lorem':'ipsum'}     # main dictionary to handle all credentials



# obj = User('ken thums','thumise','hsajkhah')

# obj.registerUser()
# print(str(obj.users))

#print('password' in  obj.users['password'] )


