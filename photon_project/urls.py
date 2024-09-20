# photon_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add_player/', views.add_player, name='add_player'),
]
