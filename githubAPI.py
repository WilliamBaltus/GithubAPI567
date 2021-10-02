import requests
import json

def repo_info(username):
    if (type(username) == str):
        repos = "https://api.github.com/users/" + username + "/repos"
        repoJson = requests.get(repos).json()

        for json in repoJson:
            counter = 0
            print("Repository Name: " + json['name'])
            commits = "https://api.github.com/repos/" + username + "/" + json['name'] + "/commits"
            commitJson = requests.get(commits).json()
            for json in commitJson:
                counter = counter + 1
            print("Commits: " + str(counter))


repo_info('WilliamBaltus')