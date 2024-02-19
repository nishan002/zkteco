from django.urls import path
from . import views

urlpatterns = [
    path('attend-list', views.index, name='attend_list'),
    path('attend', views.attend, name='attend'),
]