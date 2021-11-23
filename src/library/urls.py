from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from library import views

urlpatterns = [
    path('api/', views.game_list),
    # path('library/<int:pk>', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)