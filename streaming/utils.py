import json

with open('tweets.json') as f:
	data = json.load(f)


for user in data['users']:
	print user['id']






