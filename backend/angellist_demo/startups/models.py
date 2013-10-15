from django.db import models

# Create your models here.
class Startup(models.Model):
	id = models.TextField(primary_key=True) # set primary_key=True to override mongodb's default object id
	name = models.TextField()
	url = models.TextField()
	incubator = models.TextField()
