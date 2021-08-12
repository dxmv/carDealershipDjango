from django.shortcuts import render,redirect
from .forms import UserRegisterForm,EditForm,EditProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from dealership.models import Car


def register(request):
    if request.method=="POST":
        user_form=UserRegisterForm(request.POST)
        if user_form.is_valid():
            user=user_form.save()
            phone=user_form.cleaned_data["phone"]
            city=user_form.cleaned_data["city"]
            new_user=Profile.objects.create(user=user,phone_number=phone,city=city)
            new_user.save()
            login_user=authenticate(username=user_form.cleaned_data["username"],password=user_form.cleaned_data["password1"])
            login(request,login_user)
            return redirect("dealership:home")
    else:
        user_form=UserRegisterForm()
    return render(request,"users/register.html",{"user_form":user_form})

def account(request,user_id):
    user=User.objects.get(id=user_id)
    cars=Car.objects.all().filter(owner=user)
    fav=Car.objects.all().filter(favourites=user)
    return render(request,"users/account.html",{"user":user,"cars":cars,"fav":fav})
def add_favourite(request,post_id):
    user=request.user
    post=Car.objects.get(id=post_id)
    if post.favourites.filter(id=user.id).exists():
        post.favourites.remove(user)
    else:
        post.favourites.add(user)
    return redirect(f"/cars/{post_id}")

def delete_account(request,user_id):
    user=User.objects.get(id=user_id)
    if request.method=="POST":
        user.delete()
        return redirect("/")
    else:
        return render(request,"users/delete.html")
def edit_account(request,user_id):
    user = User.objects.get(id=user_id)
    if request.method=="POST":
        user_form=EditForm(request.POST,instance=user)
        p_form = EditProfileForm(request.POST,instance=user.profile)
        if user_form.is_valid() and p_form.is_valid():
            user_form.save()
            p_form.save()
            return redirect(f"/account/{user.id}/")
    else:
        user_form=EditForm(instance=user)
        p_form=EditProfileForm(instance=user.profile)
    return render(request,"users/edit.html",{"user_form":user_form,"p_form":p_form})
