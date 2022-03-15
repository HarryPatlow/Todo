from asyncio import Task
from django.shortcuts import render
from .models import Task
# Create your views here.

def index(request):
    return render(request,'Tasks/index.html',{
        "tasks":Task.objects.all(),
        "important":Task.objects.filter(priority__in=[7,8,9,10]),
        "basic":Task.objects.filter(priority__in=[0,1,2,3,4,5])
    })

def tasks(request):
    if request.method == "POST":
        pass
    return render(request, "Tasks/tasks.html",{
        "important":Task.objects.filter(priority__in=[7,8,9,10]),
        "basic":Task.objects.filter(priority__in=[0,1,2,3,4,5])
    })