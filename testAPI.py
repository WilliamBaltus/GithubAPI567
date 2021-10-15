import unittest
from unittest import mock
import unittest.mock

mockedReq = mock.Mock()

from githubAPI import repo_info

class TestAPIs(unittest.TestCase):

    # def testUserNameA(self): 
    #     self.assertEqual(repo_info(123), 'Invalid User Format')

    # def testUserNameB(self): 
    #     self.assertEqual(repo_info('richkempinski1'), 'User Not Found')
    
    # def testRepoCommits(self):
    #     self.assertEqual(repo_info('WilliamBaltus'), "Repos: 10 Commits: 85")
    

    @mock.patch('requests.get')
    def testUserName(self, mockedReq):
        expected = {
            "message": "Not Found",
            "documentation_url": "https://docs.github.com/rest/reference/repos#list-repositories-for-a-user"
        }
        mockedReq.return_value = expected
        self.assertEqual(repo_info('richkempinski1'), 'User Not Found')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
