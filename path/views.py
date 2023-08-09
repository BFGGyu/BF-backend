from django.shortcuts import render, get_object_or_404
from .models import Path, Route
from .serializers import PathSerializer, RouteSerializer
from obstacle.models import Obstacle, ObsType
from obstacle.serializers import ObstacleSerializer, ObsTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
# 경로 좌표 출력
class RouteList(APIView):
    def get(self, request, departure, arrival):
        try:
            path = Path.objects.get(departure=departure, arrival=arrival)
        except Path.DoesNotExist:
            raise Http404
        
        routes = Route.objects.filter(path_id=path.id)
        serializer = RouteSerializer(routes, many=True)
        
        departure_latitude = path.departure.latitude
        departure_longitude = path.departure.longitude
        arrival_latitude = path.arrival.latitude
        arrival_longitude = path.arrival.longitude

        departure_info = {
            "latitude": departure_latitude,
            "longitude": departure_longitude
        }
        
        arrival_info = {
            "latitude": arrival_latitude,
            "longitude": arrival_longitude
        }
        
        response_data = {
            "path_id": path.id,
            "departure": departure_info,
            "arrival": arrival_info,
            "routes": serializer.data
        }
        
        return Response(response_data)   
    
# 경로상 장애물 정보 출력
class ObstacleList(APIView):
    def get(self, request, departure, arrival):
        path_id = Path.objects.get(departure=departure, arrival=arrival)
        obstacles = Obstacle.objects.filter(path_id=path_id)
        serializer = ObstacleSerializer(obstacles, many=True)
        return Response(serializer.data)