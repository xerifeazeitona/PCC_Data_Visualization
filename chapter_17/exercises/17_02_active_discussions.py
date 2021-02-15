"""
17-2. Active Discussions
Using the data from hn_submissions.py, make a bar chart showing the most
active discussions currently happening on Hacker News.
The height of each bar should correspond to the number of comments each
submission has.
The label for each bar should include the submission’s title and should
act as a link to the discussion page for that submission.
"""
from operator import itemgetter
import requests

from plotly import offline

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

links, comments, titles = [], [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    comments.append(submission_dict['comments'])

    sub_title = submission_dict['title']
    sub_url = submission_dict['hn_link']
    sub_link = f"<a href='{sub_url}'>{sub_title}</a>"
    links.append(sub_link)

# Make the visualization.
data = [{
    'type': 'bar',
    'x': links,
    'y': comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most active discussions on HN',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Articles',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_articles.html')
