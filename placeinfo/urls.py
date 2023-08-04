from django.urls import path
from placeinfo.views import *

urlpatterns = [
    path('<int:id>/', place_detail, name = 'place_detail'),
]