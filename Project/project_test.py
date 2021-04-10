
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

if __name__ == '__main__':
    unittest.main()