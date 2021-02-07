import datetime
from django.db import models
from django.contrib.auth.models import User

#Info about the pet and owner
class PetInfo(models.Model):
    pet_name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_choice = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
    ]
    pet_species = models.CharField(max_length=3,choices=pet_choice, default='Dog')
    pet_gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    pet_sex = models.CharField(max_length=6, choices=pet_gender, default= 'Male')
    pet_breed = models.CharField(max_length=200)
    pet_color = models.CharField(max_length=200, blank=True)
    starting_weight = models.FloatField()
    pet_birthday = models.DateField()
    pet_allergies = models.CharField(max_length=300, default="none")
    pet_primary_vet = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Pets Information'

    def __str__(self):
        return self.pet_name

class HealthTracker(models.Model):
    pet_name = models.ForeignKey(PetInfo, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    Daily_Tracking = "DT"
    Vet_visit = "VT"
    Emergency = "EM"
    tracking_choice = [
        (Daily_Tracking, 'Daily_Tracking'),
        (Vet_visit, 'Vet_visit'),
        (Emergency, 'Emergency'),
    ]
    tracking_type = models.CharField(
        max_length=2,
        choices=tracking_choice,
        default=Daily_Tracking
    )
    pet_weight = models.FloatField(blank=True, null=True)
    pet_temp = models.FloatField(blank=True, null=True)
    solid_stool = models.BooleanField(default=True)
    healthy_appetite = models.BooleanField(default=True)
    healthy_coat = models.BooleanField(default=True)
    range_of_motion_exercises = models.BooleanField(default=True)
    ongoing_meds = models.BooleanField(default=False)
    pet_glucose = models.IntegerField(blank=True, null=True)
    acupuncture = models.BooleanField(default=False)
    laser_therapy = models.BooleanField(default=False)
    adjustment = models.BooleanField(default=False)
    surgery = models.BooleanField(default=False)
    special_notes_for_next_time = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
