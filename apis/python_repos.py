import requests

#Make an API call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000" #Second line is the query string

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}")

#Convert the response object to a dictionary
response_dict = r.json()

#Process results
print(response_dict.keys())

#Wrangling with the dictionary
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

#Explore information about repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

#Examine first directory
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")

#for key in sorted(repo_dict.keys()):
#    print(key)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")