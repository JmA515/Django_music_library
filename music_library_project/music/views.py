from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework import response
from rest_framework import status

# Create your views here.
class SongList(APIView):

    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many = True)
        return response.Response(serializer.data)

    def post(self, request):
        serializer = SongSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status = status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)