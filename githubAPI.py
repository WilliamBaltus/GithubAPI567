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

        repoAmount = 0  
        commitTotal = 0
        for json in repoJson:
            commitsAmount = 0
            print("Repository Name: " + json['name'])
            repoAmount += 1
            commits = "https://api.github.com/repos/" + username + "/" + json['name'] + "/commits"
            commitJson = requests.get(commits).json()
            for json in commitJson:
                commitsAmount = commitsAmount + 1
            print("Commits: " + str(commitsAmount))
            commitTotal = commitTotal + commitsAmount
        return "Repos: " + str(repoAmount) + " Commits: " + str(commitTotal)
    else: 
        return "Invalid User Format"


repo_info('WilliamBaltus')
