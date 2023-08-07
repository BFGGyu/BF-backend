from django.urls import path
from place.views import *

urlpatterns = [   
    path('facility/<str:name>/', FacilityDetail.as_view()),
    path('station/<str:name>/', StationDetail.as_view()),    
    path('facility/amenity/<str:name>/', FacAmenityDetail.as_view()),
    path('station/amenity/<str:name>/', StatAmenityDetail.as_view()),
]