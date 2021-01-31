from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """creating a new account"""
    if request.method != "POST":
        form = UserCreationForm()
    else:
        #complete the set up process
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            #now log the user in and direct to the home page
            login(request, new_user)
            return redirect('pet_health_tracker:home')

    context = {'form': form}
    return render(request, 'registration/register.html', context)
