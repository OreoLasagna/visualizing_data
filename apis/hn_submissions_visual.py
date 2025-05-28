from operator import itemgetter
import requests

import plotly.express as px

#Make an API call and check the response
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

#Process information about each submission
submission_ids = r.json()
submission_dicts = []

for submission_id in submission_ids[:30]:
    #Make a new API call for each submission
    new_url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(new_url)
    response_dict = r.json()

    #Build a dictionary for each article - Had to look up to add this if/else since some articles have no comments and therefore no descendant key!
    if 'descendants' in response_dict:
        submission_dict = {
            'title': response_dict["title"],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict["descendants"],
        }
        submission_dicts.append(submission_dict)

    else:
        submission_dict = {
            'title': response_dict["title"],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': 0,
        }
        submission_dicts.append(submission_dict)


#This sorts the data in the dictionary by comments
submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), reverse = True)

#Graphing Data
comments, discussion_links = [], []

#Now we populate the graphing data
for submission_dict in submission_dicts:
    comments.append(submission_dict['comments'])

    #Build hyperlinks for x-axis text
    discussion_link = f"<a href = '{submission_dict['hn_link']}'>{submission_dict['title']}</a>"
    discussion_links.append(discussion_link)


#Make visualization
title = 'Most Active Discussions on Hacker News'
labels = {'x': 'Article', 'y': 'Comments'}
fig = px.bar(x = discussion_links, y = comments, title = title, labels = labels) 

fig.update_layout(title_font_size = 28, xaxis_title_font_size = 20, yaxis_title_font_size = 20)
fig.update_traces(marker_color = 'SteelBlue', marker_opacity = 0.6)
fig.show()