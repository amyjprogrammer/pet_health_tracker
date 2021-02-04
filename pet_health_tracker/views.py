from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
def add_pet(request):
    """form to add a pet"""
    if request.method != 'POST':
        #no data submitted; creating a blank form
        form = PetInfoForm()
    else:
        #creating a new pet and verifying the data
        form = PetInfoForm(data=request.POST)
        if form.is_valid():
            add_pet = form.save(commit=False)
            add_pet.owner = request.user
            add_pet.save()
            return redirect('pet_health_tracker:pet_names')

    context = {'form': form}
    return render(request, 'pet_health_tracker/add_pet.html', context)


@login_required
def pet_health(request, pet_id):
    """Show a single pet and all the info"""
    pet_name = get_object_or_404(PetInfo, id=pet_id)
    check_pet_owner(request, pet_name.owner)
    health_trackers = pet_name.healthtracker_set.order_by('date_added')
    latest_health_tracker = pet_name.healthtracker_set.order_by('-date_added').all()[:1]
    context = {'pet_name': pet_name, 'health_trackers': health_trackers, 'latest_health_tracker': latest_health_tracker}
    return render(request, 'pet_health_tracker/pet_health.html', context)

@login_required
def pet_tracker(request, pet_id):
    """option to add a new health form"""
    pet_name = get_object_or_404(PetInfo, id=pet_id)
    check_pet_owner(request, pet_name.owner)

    if request.method != 'POST':
        #show empty form.  Allow user to enter info
        form = HealthTrackerForm()
    else:
        form = HealthTrackerForm(data=request.POST)
        if form.is_valid():
            pet_tracker = form.save(commit=False)
            pet_tracker.pet_name = pet_name
            pet_tracker.save()
            return redirect('pet_health_tracker:pet_health', pet_id=pet.id)

    context = {'pet_name': pet_name, 'form': form}
    return render(request, 'pet_health_tracker/pet_tracker.html', context)

@login_required
def check_pet_owner(request, owner):
    """makes sure editor or viewer is the owner"""
    if owner!= request.user:
        raise Http404

@login_required
def chart_weight_data(request,pet):
    pet_name = get_object_or_404(PetInfo, id=pet)
    check_pet_owner(request, pet_name.owner)
    health_trackers = pet_name.healthtracker_set.order_by('date_added')
    weight_info = []

    for info in health_trackers:
        date_add = info.date_added
        x_date = date_add.strftime('%m-%d-%Y')
        weight_info.append({x_date:info.pet_weight})

    return JsonResponse(weight_info, safe=False)

@login_required
def chart_temp_data(request,pet):
    pet_name = get_object_or_404(PetInfo, id=pet)
    check_pet_owner(request, pet_name.owner)
    health_trackers = pet_name.healthtracker_set.order_by('date_added')
    temp_info = []

    for info in health_trackers:
        date_adds = info.date_added
        date = date_adds.strftime('%m-%d-%Y')
        temp_info.append({date:info.pet_temp})

    return JsonResponse(temp_info, safe=False)
