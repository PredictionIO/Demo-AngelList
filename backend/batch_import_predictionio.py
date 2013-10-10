"""
Import data into PredictionIO
"""
import predictionio
import Queue

USERS_FILE = "angellist_data/users.csv"
ITEMS_FILE = "angellist_data/startup_id_name_url.csv"
FOLLOW_ACTIONS_FILE = "angellist_data/follows.csv"

APP_KEY = "vCHDz4B6GDXSgRwuLcJ6BdElM0yWf65NqTAfJ3v4caVuRj42CjbrfqNAD5nQ8nWp"
API_URL = "http://localhost:8000"
THREADS = 25
REQUEST_QSIZE = 500

client = predictionio.Client(APP_KEY, THREADS, API_URL, qsize=REQUEST_QSIZE)

print 'Importing users...'
f = open(USERS_FILE, 'r')
firstline = True
for line in f:
	if firstline:
		firstline = False
	else:
		data = line.rstrip('\r\n')
		client.acreate_user(data)
f.close()
print 'Done.'

print 'Importing items...'
f = open(ITEMS_FILE, 'r')
firstline = True
for line in f:
	if firstline:
		firstline = False
	else:
		data = line.rstrip('\r\n').split(',')
		client.acreate_item(data[0], ('startup',))
f.close()
print 'Done.'

print 'Importing actions...'
f = open(FOLLOW_ACTIONS_FILE, 'r')
firstline = True
for line in f:
	if firstline:
		firstline = False
	else:
		data = line.rstrip('\r\n').split(',')
		iid = data[0]
		uid = data[1]
		client.identify(uid)
		client.arecord_action_on_item("like", iid)
f.close()
print 'Done.'

client.close()



