from . import views
from django.urls import path, include

urlpatterns = [
    path("",views.home, name = 'home'),
    path("about",views.about, name = 'about'),
    path("delete/<list_id>", views.delete, name='delete'),
    path("incomplete/<list_id>", views.incomplete, name='incomplete'),
    path("complete/<list_id>", views.complete, name='complete'),
    #edit the main item
    path("edit/<list_id>", views.edit, name= 'edit'),
]
