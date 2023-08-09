from django.urls import path
from path.views import *

urlpatterns = [   
    path('<str:departure>/<str:arrival>/', RouteList.as_view()),
    path('obstacle/<str:departure>/<str:arrival>/', ObstacleList.as_view()),
]