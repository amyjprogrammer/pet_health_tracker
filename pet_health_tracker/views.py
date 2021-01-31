from django.shortcuts import render, redirect, get_object_or_404

from .models import PetInfo, HealthTracker
from .forms import PetInfoForm, HealthTrackerForm

# home view
def home(request):
    return render(request, 'pet_health_tracker/home.html')

def pet_names(request):
    """page showing all the pet names"""
    pet_names= PetInfo.objects.filter(owner=request.user).order_by('pet_name')
    context = {'pet_names': pet_names}
    return render(request, 'pet_health_tracker/pet_names.html', context)

def pet_health(response, pet_id):
    """Show a single pet and all the info"""
    pet_name = PetInfo.objects.get(id=pet_id)
