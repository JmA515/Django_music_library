from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework import response, serializers
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

class SongDetail(APIView):

    def get_object(self, pk):
        try:
            return Song.objects.get(pk = pk)
        except Song.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        song= self.get_object(pk)
        serializer = SongSerializer(song)
        return response.Response(serializer.data)
    
    def put(self, request, pk):
        song= self.get_object(pk)
        serializer = SongSerializer(song, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = self.get_object(pk)
        song.delete()
        return response.Response(song, status = status.HTTP_200_OK)