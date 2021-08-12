from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path("register/",views.register,name="register"),
    path("login/",LoginView.as_view(template_name="users/login.html"),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
    path("fav/<int:post_id>/",views.add_favourite,name="favourite"),
    path("account/<int:user_id>/",views.account,name="account"),
    path("account/<int:user_id>/delete/",views.delete_account,name="delete_account"),
    path("account/<int:user_id>/edit/",views.edit_account,name="edit_account"),
]