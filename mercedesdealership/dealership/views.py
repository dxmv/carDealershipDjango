from django.shortcuts import render,redirect
from .models import Car
from .filters import CarFilter
from .forms import ContactForm,CarForm
from django.core.mail import send_mail, BadHeaderError
def home(request):
    cars=Car.objects.all().order_by("-id")[:3]
    return render(request,"dealership/home.html",{"cars":cars})

def cars(request):
    cars=Car.objects.all()
    filter=CarFilter(request.GET,queryset=cars)
    cars=filter.qs
    context={
        "cars":cars,
        "filter":filter,
    }
    return render(request,"dealership/cars.html",context)

def single_car(request,car_id):
    car=Car.objects.all().get(id=car_id)
    all_cars=Car.objects.all().filter(owner=car.owner)
    all_cars=[c for c in all_cars if c!=car]
    is_fav=car.favourites.filter(id=request.user.id).exists()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            header=form.cleaned_data["header"]+" - "+str(car.name)
            mes=form.cleaned_data["message"]
            send_mail(header,mes,email,[car.owner.email])
            return redirect(f"/cars/{car_id}")
    else:
        form=ContactForm()
    return render(request,"dealership/single_car.html",{"car":car,"form":form,"is_fav":is_fav,"all_cars":all_cars})

def add_car(request):
    if request.method=="POST":
        form=CarForm(request.POST,request.FILES)
        if form.is_valid():
            car=form.save(commit=False)
            car.owner=request.user

            car.save()
            return redirect("/cars/")
    else:
        form=CarForm
    return render(request,"dealership/add_car.html",{"form":form})

def edit_car(request,car_id):
    car=Car.objects.get(id=car_id)
    if request.method=="POST":
        form=CarForm(request.POST,request.FILES,instance=car)
        if form.is_valid():
            form.save()
            return redirect(f"/cars/{car_id}")
    else:
        form=CarForm(instance=car)
    return render(request,"dealership/edit_car.html",{"form":form,"car":car})

def delete_car(request,car_id):
    car=Car.objects.get(id=car_id)
    if request.method=="POST":
        car.delete()
        return redirect("/")
    return render(request,"dealership/delete_car.html",{"car":car})
