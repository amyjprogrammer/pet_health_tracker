from django import forms

from .models import PetInfo, HealthTracker

class PetInfoForm(forms.ModelForm):
    class Meta:
        model = PetInfo
        fields = [
            'pet_name', 'pet_species', 'pet_sex', 'pet_breed', 'pet_color', 'starting_weight', 'pet_birthday', 'pet_allergies',  'pet_primary_vet',
        ]
        labels = {
            'pet_name': 'Name',
            'pet_species': 'Species',
            'pet_sex': 'Sex',
            'pet_breed': 'Breed',
            'pet_color': 'Color',
            'starting_weight': 'Weight',
            'pet_birthday': 'Birthday',
            'pet_allergies': 'Allergies',
            'pet_primary_vet': 'Primary Vet',
        }

class HealthTrackerForm(forms.ModelForm):
    class Meta:
        model = HealthTracker
        fields= [
            'tracking_type', 'pet_weight', 'pet_temp', 'pet_glucose', 'solid_stool', 'healthy_appetite', 'healthy_coat', 'range_of_motion_exercises', 'ongoing_meds',  'acupuncture', 'laser_therapy', 'adjustment', 'surgery', 'special_notes_for_next_time', 'notes',
        ]
        labels = {
            'tracking_type': "Tracking Choice",
            'pet_weight': 'Weight',
            'pet_temp': 'Temp',
            'pet_glucose': 'Glucose Number',
            'solid_stool': 'Solid Stool',
            'healthy_appetite': 'Healthy Appetite',
            'healthy_coat': 'Healthy Coat',
            'range_of_motion_exercises': 'Range of motion exercises',
            'ongoing_meds': 'Ongoing Medication',
            'acupuncture': 'Acupuncture',
            'laser_therapy': 'Laser Therapy',
            'adjustment': 'Adjustment',
            'surgery': 'Surgery',
            'special_notes_for_next_time': 'Quick Reminder for Next Time',
            'notes': 'Notes'
        }
