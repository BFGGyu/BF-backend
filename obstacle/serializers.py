from rest_framework import serializers
from .models import Obstacle, ObsType

class ObstacleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obstacle

        fields = "__all__"

class ObsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObsType

        fields = "__all__"        