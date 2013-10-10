# Create your views here.
from startups.models import Startup
from startups.serializers import StartupSerializer
from rest_framework import generics

class StartupList(generics.ListCreateAPIView):
	queryset = Startup.objects.all()
	serializer_class = StartupSerializer

class StartupDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Startup.objects.all()
	serializer_class = StartupSerializer
	