from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(request):
    
    task = request.POST['task'] # name = 'task'
    Task.objects.create(task=task)
    
    return redirect('home')