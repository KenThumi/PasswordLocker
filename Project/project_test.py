
import unittest
# from credentials import Credentials
from user import User

class TestProject(unittest.TestCase):
    '''Class to test all methods and fuctions of the project'''
    
    def setUp(self):
        '''initialize a user obj'''
        self.user = User('John Doe','johndoe','JohnDoe1&')


    def tearDown(self):
        '''tearDown method that does clean up after each test case has run'''

        User.users = {}

    def test_checkRegistered(self):
        '''check if test checkregistered method is working without errors'''
        self.user.registerUser() 

        self.assertEqual(self.user.username in User.users.keys(), self.user.checkRegistered())
        self.assertEqual(self.user.password == User.users['johndoe']['password'], self.user.checkRegistered())


    def test_registerUser(self):
        '''test if registration is working'''
        User.users['RandomName'] = {'password':'RandomPa$$w@rd','fullname':'Random Name'}  #add without using function
        self.user.registerUser()                                   #using fxn

        self.assertEqual(len(User.users),2)


    def test_checkUsernameTaken(self):
        '''tests whether cheUsernameTaken method works'''
        self.user.registerUser()
        
        self.assertTrue(self.user.checkUsernameTaken())

    
    def test_addCredential(self):
        ''' test whether addCredential method works'''
        self.user.registerUser() #register user
        self.user.users[self.user.username]['credentials']={'instagram':'appPassword'} #add one app creds directly

        self.user.addCredential('facebook','fbpwd')  #add creds using class method

        self.assertEqual( len(User.users[self.user.username]['credentials']), 2)


    def test_checkCredsExists(self):
        '''test whether checkCredsExists method works accordingly'''
        self.user.registerUser() #register user
        self.user.addCredential('facebook','fbpwd')  #add creds using class method

        self.assertTrue(self.user.checkCredsExists('facebook')) #should return true since facebook was inserted



    def test_generateAppPwd(self):
        '''check whether generateAppPwd works - generates password'''
        pwd = self.user.generateAppPwd()

        self.assertEqual(len(pwd),10)    # 10 being default pwd length


    def test_getAllUserCredetials(self):
        '''test whether getAllUserCredential method work without errors'''
        User.users = {}
        self.user.registerUser() #register user
        self.user.addCredential('facebook','fbpwd') #add one credential

        self.assertEqual( len(self.user.users[self.user.username]['credentials']), len(self.user.getAllUserCredentials()) )

if __name__ == '__main__':
    unittest.main()