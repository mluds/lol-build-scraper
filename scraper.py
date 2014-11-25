# Install using 'pip install requests'
import requests
import os
import json

# Get all champion names
response = requests.get('http://www.lolflavor.com/data/champion.json')
response = response.json()
champions = []
for champion in response['data']:
  champions.append(champion)

# Each champion has a build for each role
roles = ['lane', 'jungle', 'support', 'aram']

# Scrape the builds
# You may need to change the directory path
for champion in champions:
  for role in roles:
  
    request = requests.get(
      'http://www.lolflavor.com/champions/' +
      champion + '/Recommended/' +
      champion + '_' + role + '_scrape.json'
    )
    
    try:
      json.loads(request.text)
    except ValueError:
      print('Request text is not valid JSON')
      continue
      
    filename = ('C:/Riot Games/League of Legends/Config/Champions/' +
      champion + '/Recommended/' + role + '.json')
      
    if not os.path.exists(os.path.dirname(filename)):
      os.makedirs(os.path.dirname(filename))
      
    with open(filename, 'w') as f:
      f.write(request.text)
      
    print('Wrote to ' + filename)