from urllib import request, response
from musicians.models import Musician
from rest_framework.views import Response
from rest_framework.views import APIView
from .serializers import MusicianSerializer
# Create your views here.

class MusicianView(APIView):
    def get(self, request):
        musicians = Musician.objects.all()
        serializer = MusicianSerializer(musicians, many=True)
        return Response(serializer.data)