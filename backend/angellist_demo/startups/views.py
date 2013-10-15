# Create your views here.
from startups.models import Startup
from startups.serializers import StartupSerializer
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def startup_list(request, format=None):
	"""
	List all startups
	"""
	if request.method == 'GET':
		startups = Startup.objects.all()
		serializer = StartupSerializer(startups, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def startup_detail(request, pk, format=None):
	"""
	Retrieve a startup
	"""
	try:
		startup = Startup.objects.get(id=pk)
	except Startup.DoesNotExist:
		return Response({"message": "Startup not found"}, status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = StartupSerializer(startup)
		return Response(serializer.data)
