import requests
import json

def repo_info(username):
    if (type(username) == str):
        repos = "https://api.github.com/users/" + username + "/repos"
        repoJson = requests.get(repos).json()
        #check for non-existant user!
        counter = 0
        for json in repoJson:
            counter += 1
        if (counter == 2):
            return "User Not Found"

        for json in repoJson:
            counter = 0
            print("Repository Name: " + json['name'])
            commits = "https://api.github.com/repos/" + username + "/" + json['name'] + "/commits"
            commitJson = requests.get(commits).json()
            for json in commitJson:
                counter = counter + 1
            print("Commits: " + str(counter))
    else: 
        return "Invalid User Format"


repo_info('WilliamBaltus')
