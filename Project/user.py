import random
import secrets
import string

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
    
    def checkRegistered(self): #write
        '''Method check if one is registered'''
        return self.username in User.users.keys() and self.password == User.users[self.username ]['password']


    def registerUser(self): #write
        '''Registers a new user'''
        self.users[self.username] = {'password':self.password,'fullname':self.fullname}
    


    def checkUsernameTaken(self):
        '''Checks whether or not the username is taken'''
        return self.username in User.users.keys()
   

    def addCredential(self,application,appPassword): #write
        '''adds an app credetials'''
        self.users[self.username]['credentials'] = {'appName':application.lower(),
                                                    'password':appPassword}


    def checkCredsExists(self,application):
        '''Checks whether or not application credentials are exists'''
        if self.users[self.username].get('credentials') != None:
            return application.lower() in self.users[self.username]['credentials'].values()
        else:
            return False


    def generateAppPwd(self,l=10):
        '''Generate alphanumeric password with at least one symbol,one lowercase character, at least one uppercase character, and at least three digits
        '''
        alphabet = string.ascii_letters + string.digits                     
        password = ''

        # Generate a ten-character alphanumeric password with at least one lowercase character, at least one uppercase character, and at least two digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(l)) 
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and sum(c.isdigit() for c in password) >= 2
                    ):
                break


        punc = string.punctuation

        password = password.replace(password[random.randint(1,5)],       #replace char btwn index 1-5 with a symbol
                                    punc[random.randint(1,len(punc) )] )

        return password





#obj = User('ken thums','thumise','hsajkhah')
#obj.registerUser()
#obj.generateAppPwd()
#obj.addCredential('facebookk','loremipsum')
#print(obj.users[obj.username]['credentials'])
# obj.registerUser()
#print(obj.checkCredsExists('facebook'))

#print('password' in  obj.users['password'] )


