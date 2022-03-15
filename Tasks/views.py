from asyncio import Task, tasks
from django.shortcuts import render, redirect
from .models import Task
from django import forms
from django.forms.widgets import NumberInput
# Create your views here.




def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        date = request.POST["date"]
        time = request.POST["time"]
        priority = request.POST["priority"]
        x = Task(name=name, due_date=date, due_time = time, priority=priority)
        x.save()
        return render(request, "Tasks/index.html",{
            "tasks":Task.objects.filter(status=False),
            "tasks_done":Task.objects.filter(status=True),
            "important":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=False),
            "important_done":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=True),
            "basic":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=False),
            "basic_done":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=True)
        })
    return render(request,'Tasks/index.html',{
        "tasks":Task.objects.filter(status=False),
        "tasks_done":Task.objects.filter(status=True),
        "important":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=False),
        "important_done":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=True),
        "basic":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=False),
        "basic_done":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=True)
    })


def complete(request, i):
    if request.method == "POST":
        task = Task.objects.get(pk=i)
        if task.status is False:
            task.status = True
        else:
            task.status = False
        task.save()
        return render(request, "Tasks/index.html",{
            "tasks":Task.objects.filter(status=False),
            "tasks_done":Task.objects.filter(status=True),
            "important":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=False),
            "important_done":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=True),
            "basic":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=False),
            "basic_done":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=True)
        })
    return render(request,'Tasks/index.html',{
            "tasks":Task.objects.filter(status=False),
            "tasks_done":Task.objects.filter(status=True),
            "important":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=False),
            "important_done":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=True),
            "basic":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=False),
            "basic_done":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=True)
    })

def delete(request, i):
    if request.method == "POST":
        task = Task.objects.filter(pk=i)
        task.delete()
        return render(request, "Tasks/index.html",{
            "tasks":Task.objects.filter(status=False),
            "tasks_done":Task.objects.filter(status=True),
            "important":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=False),
            "important_done":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=True),
            "basic":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=False),
            "basic_done":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=True)
        })
    return render(request,'Tasks/index.html',{
            "tasks":Task.objects.filter(status=False),
            "tasks_done":Task.objects.filter(status=True),
            "important":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=False),
            "important_done":Task.objects.filter(priority__in=[7,8,9,10]).filter(status=True),
            "basic":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=False),
            "basic_done":Task.objects.filter(priority__in=[0,1,2,3,4,5]).filter(status=True)
    })
