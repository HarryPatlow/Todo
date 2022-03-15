from unicodedata import name
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('complete/<int:i>',views.complete,name="complete"),
    path('delete/<int:i>',views.delete ,name="delete"),
]
