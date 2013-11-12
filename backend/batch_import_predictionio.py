"""
Import data into PredictionIO
"""
import predictionio
import Queue
import csv

USERS_FILE = "angellist_data/users.csv"
ITEMS_FILE = "angellist_data/startup_id_name_url_incubator_markets.csv"
FOLLOW_ACTIONS_FILE = "angellist_data/follows.csv"

APP_KEY = "Xk28xvHUjkMKzRY3ZuNzKmJ9XQmx18FwHgBku7PxeXlMnENJ3mXxYTYhB0b8Heyh"
API_URL = "http://localhost:8000"
THREADS = 25
REQUEST_QSIZE = 500

client = predictionio.Client(APP_KEY, THREADS, API_URL, qsize=REQUEST_QSIZE)

print 'Importing users...'
with open(USERS_FILE, 'r') as f:
	reader = csv.reader(f)
	firstline = True
	for line in reader:
		if firstline:
			firstline = False
		else:
			client.acreate_user(line[0])
print 'Done.'

# startup_id,name,url,incubator,markets
print 'Importing items...'
with open(ITEMS_FILE, 'r') as f:
	reader = csv.reader(f)
	firstline = True
	for line in reader:
		if firstline:
			firstline = False
		else:
			if line[4]:
				market_ids = tuple(line[4].split(','))
			else:
				market_ids = tuple()
				
			itypes = ('startup',) + market_ids
			client.acreate_item(line[0], itypes)
print 'Done.'

print 'Importing actions...'
with open(FOLLOW_ACTIONS_FILE, 'r') as f:
	reader = csv.reader(f)
	firstline = True
	for line in reader:
		if firstline:
			firstline = False
		else:
			iid = line[0]
			uid = line[1]
			client.identify(uid)
			client.arecord_action_on_item("like", iid) # use built-in "like" action to represent "follow"
print 'Done.'

client.close()




