from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Place

# Create your views here.
@require_http_methods(["GET"])
def get_place_detail(request, id):
    place_json={
            "id" : Place.place_id,
            "name" : Place.name,
			"description" : Place.description,
            "category" : Place.category,
            "latitude" : Place.latitude,
            "longtitude" : Place.longitude,
            "toilet" : Place.has_accessible_toilet,
			"elevator" : Place.has_elevator
	}
    
    return JsonResponse({
        'status' : 200,
        'message' : '장소정보 조회 성공',
        'data' : place_json
	})