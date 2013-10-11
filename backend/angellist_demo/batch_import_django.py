"""
Import data into MongoDB for Django
"""
from startups.models import Startup
import csv

ITEMS_FILE = "../angellist_data/startup_id_name_url.csv"

print 'Importing items...'
with open(ITEMS_FILE, 'r') as f:
	reader = csv.reader(f)
	firstline = True
	for line in reader:
		if firstline:
			firstline = False
		else:
			Startup.objects.create(id=line[0], name=line[1], url=line[2])
print 'Done.'
