"""
Now we’ll begin to write a program to automatically issue an API call
and process the results by identifying the most starred Python projects
on GitHub.
"""
import requests

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()
# Process results.
print(response_dict.keys())
