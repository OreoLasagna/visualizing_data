import requests


def call_API():
    """Setting up my tests a bit smarter"""

    #Make an API call and check the response
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000" #Second line is the query string

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers)
    return r

#Then to run this in the terminal we type: pytest 
#We don't call this function anywhere see? We have to just blanket call pytest
#So just cd navigate to the apis folder and type in: pytest

def test_status_code_200():
    """Does the url in python_repos return a status code of 200 when we try to grab it?"""
    r = call_API()
    assert r.status_code == 200

#Then to run this in the terminal we type: pytest
#We don't call this function anywhere see? We have to just blanket call pytest


def test_repository_count():
    """Does the repository count, which at time of writing is 667, stay the same or exceed it?"""
    
    r = call_API()

    #Convert the response object to a dictionary
    response_dict = r.json()

    assert response_dict['total_count'] >= 667