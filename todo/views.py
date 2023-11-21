from django.shortcuts import render
from todo_app.models import Task

def home(request):
    
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') # get objects following the condition
    # print(tasks)
    
    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }
    
    return render(request, 'home-todo.html', context)