from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.home,name="home"),
    path("cars/",views.cars,name="cars"),
    path("cars/<car_id>/",views.single_car,name="single_car"),
    path("add/",views.add_car,name="add_car"),
    path("cars/<car_id>/edit/",views.edit_car,name="edit_car"),
    path("cars/<car_id>/delete/",views.delete_car,name="delete_car"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)