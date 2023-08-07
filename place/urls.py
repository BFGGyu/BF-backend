from django.urls import path
from place.views import *

urlpatterns = [   
    path('facility/amenity/<str:name>/', FacAmenityDetail.as_view()),
    path('station/amenity/<str:name>/', StatAmenityDetail.as_view()),
]