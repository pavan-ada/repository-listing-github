# Author : Pavan Kumar << mr.pavan@gmail.com>>
# for listing public repo's for user - github api :get/users/{user}/repos
# for listing org repos replace /users with /orgs/{org}/repos
# GET Token from github account -> profile, settings, developer settings, personal access tokens
import requests
import os

username = input("Enter the github username:")
usertoken = os.getenv('GHTOKEN')
request = requests.get('https://api.github.com/users/'+username+'/repos')
json = request.json()
for i in range(0,len(json)):
  print('{number} :  {name} :  {url}'.format(number = i+1, name = json[i]['name'], url = json[i]['svn_url']))
  # for Multiline output
  # print("Project Number:",i+1)
  # print("Project Name:",json[i]['name'])
  # print("Project URL:",json[i]['svn_url'],"\n")