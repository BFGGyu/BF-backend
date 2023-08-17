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
        if obj.path_id and isinstance(obj.path_id, Path):
            return str(obj.path_id.departure)  # Path 객체를 문자열로 변환
        return None

    def get_arrival(self, obj):
        if obj.path_id and isinstance(obj.path_id, Path):
            return str(obj.path_id.arrival)  # Path 객체를 문자열로 변환
        return None