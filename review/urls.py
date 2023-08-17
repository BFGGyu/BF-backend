from django.urls import path
from review.views import *

urlpatterns = [
    path('<str:arrival>/', ReviewList.as_view()),
    path('<str:arrival>/<str:writer>/', ReviewDetail.as_view()),
]