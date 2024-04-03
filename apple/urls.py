from django.urls import path
from apple.views import index, mypage

urlpatterns = [
    path('mypage', mypage),
    path('', index),
]