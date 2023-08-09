from django.shortcuts import render, get_object_or_404
from .models import Review
from .serializers import ReviewSerializer
from path.models import Path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class ReviewList(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        departure = request.data.get('departure')
        arrival = request.data.get('arrival')
        
        try:
            path = Path.objects.get(departure=departure, arrival=arrival)
        except Path.DoesNotExist:
            return Response({"error": "경로를 찾을 수 없습니다!"}, status=status.HTTP_400_BAD_REQUEST)
        
        request.data['path_id'] = path.id        
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ReviewDetail(APIView):
    def get(self, request, departure, arrival, writer):
        try:
            path = Path.objects.get(departure=departure, arrival=arrival)
        except Path.DoesNotExist:
            raise Http404

        try:
            review = Review.objects.get(path_id=path.id, writer=writer)
        except Review.DoesNotExist:
            raise Http404
            
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, departure, arrival, writer):
        review = get_object_or_404(Review, writer=writer)
        serializer = ReviewSerializer(review, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, stauts=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, departure, arrival, writer):
        review = get_object_or_404(Review, writer=writer)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)