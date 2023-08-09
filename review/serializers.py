from rest_framework import serializers
from .models import Review
from path.models import Path

class ReviewSerializer(serializers.ModelSerializer):
    departure = serializers.SerializerMethodField()
    arrival = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['id', 'departure', 'arrival', 'writer', 'rating', 'comment', 'created_at', 'updated_at', 'path_id']

    def get_departure(self, obj):
        return obj.path_id.departure.name if obj.path_id else None
    
    def get_arrival(self, obj):
        return obj.path_id.arrival.name if obj.path_id else None