# Author : Pavan Kumar << mr.pavan@gmail.com>>
# for listing repo's for organization - github api :get/orgs/{org}/repos
# for listing user repos replace /orgs with /users/{user}/repos
# GET Token from github account -> profile, settings, developer settings, personal access tokens

from decouple import config
import requests
import os

# Pass the access tokens as headers ref https://docs.github.com/en/rest
# usertoken = 'insert user token from github or from the enviornment vairable'
# header = {'Authorization': 'token access-token-from-your-account-cbacab'}
# decouple - create .env in root repo dicrectory and add variable GHTOKEN=your-personal-access-token
# os.getenv - for your system enviornment variable
# usertoken = 'token {}'.format(os.getenv('GHTOKEN'))

orgname = input("Enter the github orgname:")
usertoken = 'token {}'.format(config('GHTOKEN'))
payload = {'visibility': 'all', 'per_page': 100}
header = {'Authorization': usertoken}

request = requests.get('https://api.github.com/orgs/'+orgname+'/repos', params=payload ,headers=header)

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
