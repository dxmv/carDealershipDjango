from django import forms
from .models import Car
from django.core.exceptions import ValidationError
class ContactForm(forms.Form):
    email=forms.EmailField(required=True)
    header=forms.CharField(max_length=200,required=True)
    message=forms.CharField(widget=forms.Textarea,required=True)

class CarForm(forms.ModelForm):
    class Meta:
        model=Car
        fields="__all__"
        exclude=("owner","favourites")

    def clean_name(self):
        name=self.cleaned_data["name"]
        qs=Car.objects.all()
        if qs.filter(name=name).exists():
            raise ValidationError("Car with that name already exist")
        return name

    def clean_price(self):
        price=self.cleaned_data["price"]
        if price<=1000 or price>=10000000:
            raise ValidationError("Price must be within the range 1000 and 10 000 000.")
        return price

    def clean_year(self):
        year=self.cleaned_data["year"]
        if year<=1950 or year>=2022:
            raise ValidationError("Year must be within the range 1950 and 2022.")
        return year

    def clean_horse_power(self):
        hp=self.cleaned_data["horse_power"]
        if hp<=50 or hp>=1500:
            raise ValidationError("Horse Power must be within the range 50 and 1500")
        return hp

    def clean_seats(self):
        s=self.cleaned_data["seats"]
        if s not in [2,5,7,9]:
            raise ValidationError("Invalid number of seats")
        return s

    def clean_doors(self):
        d=self.cleaned_data["doors"]
        if d not in [3,5]:
            raise ValidationError("Invalid number of doors")
        return d