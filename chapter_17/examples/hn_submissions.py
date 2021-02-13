"""
The following URL returns a simple list of all the IDs of the current
top articles on Hacker News:
https://hacker-news.firebaseio.com/v0/topstories.json

We can use this call to find out which articles are on the home page
right now, and then generate a series of API calls similar to the one we
just examined. With this approach, we can print a summary of all the
articles on the front page of Hacker News at the moment.
"""
from operator import itemgetter
import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    
    try:
        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
    except KeyError:
        pass
    else:
        submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts, key=itemgetter('comments'), reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
