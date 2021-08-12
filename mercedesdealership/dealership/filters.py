import django_filters
from .models import *
class CarFilter(django_filters.FilterSet):
    class Meta:
        model=Car
        fields=["year","city","color","transmision","body_type","fuel_type"]