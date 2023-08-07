from django.shortcuts import render, get_object_or_404
from .models import Obstacle, ObsType
from .serializers import ObstacleSerializer, ObsTypeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.