from django.urls import path

from . import views
urlpatterns =[
    path('', views.weather_search, name='weather_search')
]
