from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .models import PetInfo, HealthTracker
from .forms import PetInfoForm, HealthTrackerForm

# home view
def home(request):
    return render(request, 'pet_health_tracker/home.html')

@login_required
def pet_names(request):
    """page showing all the pet names"""
    pet_names= PetInfo.objects.filter(owner=request.user).order_by('pet_name')
    context = {'pet_names': pet_names}
    return render(request, 'pet_health_tracker/pet_names.html', context)

@login_required
def add_pet(request, pet_id):
    """form to add a pet"""

    return render(request, 'pet_health_tracker/add_pet.html', context)


@login_required
def pet_health(request, pet_id):
    """Show a single pet and all the info"""
    pet_name = get_object_or_404(PetInfo, id=pet_id)
    check_pet_owner(request, pet_name.owner)
    health_trackers = pet_name.healthtracker_set.order_by('date_added')
    context = {'pet_name': pet_name, 'health_trackers': health_trackers}
    return render(request, 'pet_health_tracker/pet_health.html', context)

@login_required
def pet_form(request, pet_id):
    """option to add a new health form"""

    return render(request, 'pet_health_tracker/pet_form.html', context)

@login_required
def check_pet_owner(request, owner):
    """makes sure editor or viewer is the owner"""
    if owner!= request.user:
        raise Http404
