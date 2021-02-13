from django.urls import path, include

from . import views

#Url for logging in

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #Page to register
    path('register/', views.register, name= 'register'),

]
