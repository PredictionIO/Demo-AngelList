"""
Import data into MongoDB for Django
"""
from startups.models import Startup

ITEMS_FILE = "../angellist_data/startup_id_name_url.csv"

print 'Importing items...'
f = open(ITEMS_FILE, 'r')
firstline = True
for line in f:
	if firstline:
		firstline = False
	else:
		data = line.rstrip('\r\n').split(',')
		Startup.objects.create(id=data[0], name=data[1], url=data[2])
f.close()
print 'Done.'
