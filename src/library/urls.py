from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('game/<int:gameID>/', views.game_details),
    path('home/', views.home),
]
