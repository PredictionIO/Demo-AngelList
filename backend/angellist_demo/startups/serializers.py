from rest_framework import serializers
from startups.models import Startup

class StartupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Startup
		fields = ('id', 'name', 'url',) # note: tuple
