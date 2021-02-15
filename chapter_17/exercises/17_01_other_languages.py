"""
17-1. Other Languages
Modify the API call in python_repos.py so it generates a chart showing
the most popular projects in other languages. Try languages such as
JavaScript, Ruby, C, Java, Perl, Haskell, and Go.
"""
import requests

from plotly import offline

def plot_repos(lang):
    """
    query github api and plot a bar chart of the top 30 repos for the
    provided language.
    """
    # Make an API call and store the response
    url = f'https://api.github.com/search/repositories?q=language:{lang}&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")

    # Process results.
    response_dict = r.json()
    repo_dicts = response_dict['items']
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        # mount repo link
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    # Make the visualization.
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': f'Most-Starred {lang.title()} Projects on GitHub',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
        },
    }
    fig = {'data': data, 'layout': my_layout}
    filename = f"{lang}_repos.html"
    offline.plot(fig, filename=filename)

languages = [
    'python',
    'javascript',
    'ruby',
    'c',
    'java',
    'perl',
    'haskell',
    'go',
]

for language in languages:
    plot_repos(language)
