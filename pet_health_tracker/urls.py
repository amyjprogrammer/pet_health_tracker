"""Views for my website"""

from django.urls import path

from . import views

app_name = 'pet_health_tracker'

urlpatterns = [
    path('', views.home ,name="home"),
    path('pet_names/', views.pet_names, name='pet_names'),
    path('pet_health/<int:pet_id>/', views.pet_health, name='pet_health'),
    path('pet_form/<int:pet_id>/', views.pet_form, name='pet_form'),
    path('add_pet/<int:pet_id>/', views.add_pet, name='add_pet'),
    path('chart_weight_data/<str:pet>/', views.chart_weight_data, name='chart_weight_data'),
    path('chart_temp_data/<str:pet>/', views.chart_temp_data, name='chart_temp_data'),
    ]
