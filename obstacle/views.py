from django.shortcuts import render, get_object_or_404
from .models import Obstacle, ObsType
from .serializers import ObstacleSerializer, ObsTypeSerializer
from path.models import Path
from path.serializers import PathSerializer 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class ObstacleList(APIView):
    def post(self, request, departure, arrival):
        path = Path.objects.get(departure=departure, arrival=arrival)
        request.data['path_id'] = path.id

        serializer = ObstacleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ObstacleDetail(APIView):   
    def delete(self, request, departure, arrival, latitude, longitude):
        path = Path.objects.get(departure=departure, arrival=arrival)
        obstacle = get_object_or_404(Obstacle, path_id=path.id, latitude=latitude, longitude=longitude)
        obstacle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)