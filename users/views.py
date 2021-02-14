from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .decorators import unathenticated_user

#Customizing the UserCreationForm form
from .forms import CreateUserForm

@unathenticated_user
def register(request):
    """creating a new account"""
    if request.method != "POST":
        form = CreateUserForm()
    else:
        #complete the set up process
        form = CreateUserForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            #now log the user in and direct to the home page
            login(request, new_user)
            return redirect('pet_health_tracker:pet_names')

    context = {'form': form}
    return render(request, 'users/register.html', context)
