import django_filters
from django_filters import CharFilter

from .models import HealthTracker

class HealthTrackerFilter(django_filters.FilterSet):
    special_notes = CharFilter(field_name= "special_notes_for_next_time", lookup_expr='icontains', label="Special Notes")
    notes = CharFilter(field_name="notes", lookup_expr='icontains')
    class Meta:
        model = HealthTracker
        fields = ['special_notes', 'notes']
