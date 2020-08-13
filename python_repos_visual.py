import requests

from plotly.graph_objs import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=star'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers= headers)
print(f"Status code: {r.status_code}")

# Process result
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars= [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'pink',
        'line': {'width': 1.5, 'color': 'purple'}
    },
    'opacity': 0.8
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'}

}

offline.plot({'data': data, 'layout': my_layout}, filename= 'python_repos.html')