from django.urls import path
from path.views import *

urlpatterns = [   
    path('<str:departure>/<str:arrival>/', RouteList.as_view()),
]