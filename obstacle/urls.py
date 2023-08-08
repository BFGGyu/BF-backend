from django.urls import path
from obstacle.views import *

urlpatterns = [   
    path('<str:departure>/<str:arrival>/', ObstacleList.as_view()),
    path('<str:departure>/<str:arrival>/<latitude>/<longitude>/', ObstacleDetail.as_view()),
]