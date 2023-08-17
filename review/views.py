from django.shortcuts import render, get_object_or_404
from .models import Review
from .serializers import ReviewSerializer
from path.models import Path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from place.models import Station, Facility

# Create your views here.
class ReviewList(APIView):
    def get(self, request, arrival):
        try:
            arrival_facility = Facility.objects.get(name=arrival)
            path = Path.objects.get(arrival=arrival_facility)
        except Path.DoesNotExist:
            raise Http404

        reviews = Review.objects.filter(path_id=path.id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, arrival):
        try:
            arrival_facility = Facility.objects.get(name=arrival)
            path = Path.objects.get(arrival=arrival_facility)
        except Path.DoesNotExist:
            raise Http404
        
        request.data['path_id'] = path.id        
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ReviewDetail(APIView):             
    def get(self, request, arrival, writer):          
        try:
            arrival_facility = Facility.objects.get(name=arrival)
            path = Path.objects.get(arrival=arrival_facility)
        except Path.DoesNotExist:
            raise Http404

        try:
            review = Review.objects.get(path_id=path.id, writer=writer)
        except Review.DoesNotExist:
            raise Http404        

        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request,arrival, writer):
        try:
            arrival_facility = Facility.objects.get(name=arrival)
            path = Path.objects.get(arrival=arrival_facility)
        except Path.DoesNotExist:
            raise Http404

        try:
            review = Review.objects.get(path_id=path.id, writer=writer)
        except Review.DoesNotExist:
            raise Http404    
        
        serializer = ReviewSerializer(review, data=request.data, partial=True)  # 부분 업데이트 가능

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,arrival, writer):
        try:
            arrival_facility = Facility.objects.get(name=arrival)
            path = Path.objects.get(arrival=arrival_facility)
        except Path.DoesNotExist:
            raise Http404

        try:
            review = Review.objects.get(path_id=path.id, writer=writer)
        except Review.DoesNotExist:
            raise Http404    

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)