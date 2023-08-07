from django.shortcuts import render, get_object_or_404
from .models import Facility, Station, FacAmenity, StatAmenity
from .serializers import FacilitySerializer, StationSerializer, FacAmenitySerializer, StatAmenitySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

# 문화 시설 정보
class FacilityDetail(APIView):
    def get(self, request, name):
        facility = get_object_or_404(Facility, name=name)
        serializer = FacilitySerializer(facility)
        return Response(serializer.data)

# 지하철 역 정보
class StationDetail(APIView):
    def get(self, request, name):
        station = get_object_or_404(Station, name=name)
        serializer = StationSerializer(station)
        return Response(serializer.data)

# 문화 시설의 편의 시설
class FacAmenityDetail(APIView):
    def get(self, request, name):
        facility = Facility.objects.get(name=name)
        fac_amenities = FacAmenity.objects.filter(fac_name=facility)
        serializer = FacAmenitySerializer(fac_amenities, many=True)
        return Response(serializer.data)

# 지하철 역의 편의 시설
class StatAmenityDetail(APIView):
    def get(self, request, name):
        station = Station.objects.get(name=name)
        stat_amenities = StatAmenity.objects.filter(stat_name=station)
        serializer = StatAmenitySerializer(stat_amenities, many=True)
        return Response(serializer.data)