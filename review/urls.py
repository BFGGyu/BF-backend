from django.urls import path
from review.views import *

urlpatterns = [
    path('', ReviewList.as_view()),
    path('<int:id>/', ReviewDetail.as_view()),
]