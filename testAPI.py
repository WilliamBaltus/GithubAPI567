import unittest

from githubAPI import repo_info

class TestAPIs(unittest.TestCase):

    def testUserNameA(self): 
        self.assertEqual(repo_info(123), 'Invalid User Format')

    def testUserNameB(self): 
        self.assertEqual(repo_info('richkempinski1'), 'User Not Found')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
