from urllib import request, response

import django
from musicians.models import Musician
from rest_framework.views import Response
from rest_framework.views import APIView
from .serializers import MusicianSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
# Create your views here.

class MusicianView(APIView):
    def get(self, request):
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MusicianRetriveView(APIView):
    def get(self, request, musician_id=''):
        if musician_id:
            try:
                musician = Musician.objects.get(id=musician_id)
                serializer = MusicianSerializer(musician)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return Response({'message': 'User not found'})
    

        
