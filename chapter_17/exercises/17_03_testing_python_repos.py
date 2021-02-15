"""
17-3. Testing python_repos.py
In python_repos.py, we printed the value of status_code to make sure the
API call was successful. Write a program called test_python_repos.py
that uses unittest to assert that the value of status_code is 200.
Figure out some other assertions you can make—for example, that the
number of items returned is expected and that the total number of
repositories is greater than a certain amount.
"""
import unittest
import requests

class GitHubAPITestCase(unittest.TestCase):
    """Tests for GitHub API."""

    def setUp(self):
        """
        Make an API call and store the API response in variables.
        """
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        headers = {'Accept': 'application/vnd.github.v3+json'}
        r = requests.get(url, headers=headers)
        self.status_code = r.status_code
        self.response_dict = r.json()

    def test_status_code(self):
        """If the status code isn't 200 it's not working."""
        self.assertEqual(self.status_code, 200)

    def test_repos_returned(self):
        """Is the number of repositories returned equal to 30?"""
        self.assertEqual(len(self.response_dict['items']), 30)

    def test_total_repos(self):
        """Is the total number of repositories higher than 6M?"""
        self.assertGreater(self.response_dict['total_count'], 6_000_000)

if __name__ == "__main__":
    unittest.main()
