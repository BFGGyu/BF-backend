from django.urls import path
from review.views import *

urlpatterns = [
    path('', ReviewList.as_view()),
    path('<str:departure>/<str:arrival>/<str:writer>/', ReviewDetail.as_view()),
]