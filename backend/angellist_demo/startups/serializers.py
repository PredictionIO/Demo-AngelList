from rest_framework import serializers
from startups.models import Startup


class StartupIdSerializer(serializers.ModelSerializer):
	class Meta:
		model = Startup
		fields = ('id',)

class StartupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Startup
		fields = ('id', 'name', 'url', 'incubator',) # note: tuple
