from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.all_news,name="all_news"),
    path("add/",views.add_news,name="add_news"),
    path("<int:article_id>/",views.article,name="article"),
    path("<int:article_id>/like/", views.like, name="like"),
    path("<int:article_id>/delete/", views.delete, name="delete"),
    path("<int:article_id>/edit/", views.edit, name="edit")
]