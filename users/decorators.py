from django.http import HttpResponse
from django.shortcuts import redirect

#if logged in can't go to register page
def unathenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect ("pet_health_tracker:pet_names")
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
    
