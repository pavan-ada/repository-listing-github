# Author : Pavan Kumar << mr.pavan@gmail.com>>
# for listing repo's for organization - github api :get/orgs/{org}/repos
# for listing user repos replace /orgs with /users/{user}/repos
# GET Token from github account -> profile, settings, developer settings, personal access tokens
# access token as paremeters api will be deprecated by github starting Sep 2021, start using orgsRepoLists.py 

import requests
import os

# Pass the access tokens as headers ref https://docs.github.com/en/rest
# usertoken = 'insert user token from github or from the enviornment vairable'
# request = requests.get('https://api.github.com/users/'+username+'/repos')
# request = requests.get('https://api.github.com/orgs/'+orgname+'/repos', params=payload)
orgname = input("Enter the github orgname:")
usertoken = os.getenv('GHTOKEN')
payload = {'access_token': usertoken, 'per_page': 100}

request = requests.get('https://api.github.com/orgs/'+orgname+'/repos', params=payload)


# validate GET request
print(request.url)
json = request.json()

# Print Repository Name and URL list in a row
  # for Multiline output
  # print("Project Number:",i+1)
  # print("Project Name:",json[i]['name'])
  # print("Project URL:",json[i]['svn_url'],"\n")
for i in range(0,len(json)):
  print('{number} :  {name} :  {url}'.format(number = i+1, name = json[i]['name'], url = json[i]['svn_url']))

