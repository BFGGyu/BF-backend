from django.urls import path
from place.views import *

urlpatterns = [   
    path('facility/<str:fac_name>/', FacilityDetail.as_view()),
    path('station/<str:stat_name>/', StationDetail.as_view()),    
    path('facility/amenity/<str:fac_name>/', FacAmenityDetail.as_view()),
    path('station/amenity/<str:stat_name>/', StatAmenityDetail.as_view()),
]