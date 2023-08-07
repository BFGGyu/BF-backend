from rest_framework import serializers
from .models import Path, Route

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path

        fields = "__all__"

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route

        fields = "__all__"        