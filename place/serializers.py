from rest_framework import serializers
from .models import Facility, Station, FacAmenity, StatAmenity

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility

        fields = "__all__"

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station

        fields = "__all__"        

class FacAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FacAmenity

        fields = "__all__"        

class StatAmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StatAmenity

        fields = "__all__"        

from .models import UserBookmark

class UserBookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBookmark
        fields = '__all__'