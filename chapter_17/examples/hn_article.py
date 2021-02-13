"""
The Hacker News API provides access to data about all submissions and
comments on the site, and you can use the API without having to register
for a key. But the response is difficult to examine without some better
formatting. Let’s run this URL through the json.dump() method, like we
did in the earthquake project in Chapter 16, so we can explore the kind
of information that’s returned about an article
"""
import requests
import json

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = '../data/readable_hn_data.json'
with open(readable_file, 'w') as file_obj:
    json.dump(response_dict, file_obj, indent=4)
