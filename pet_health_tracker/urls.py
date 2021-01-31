"""Views for my website"""

from django.urls import path

from . import views

app_name = 'pet_health_tracker'
urlpatterns = [
    path('', views.home ,name="home"),
    path('pet_names/', views.pet_names, name='pet_names'),
    path('pet_names/<int:pet_id>', views.pet_health, name='pet_health'),

    ]
