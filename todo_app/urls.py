from django.urls import path
from . import views

urlpatterns = [
    # Add Task
    path('addTask/', views.addTask, name='addTask'),
    
    # Mark as Done #
    path('markasdone/<int:pk>', views.mark_as_done, name='mark_as_done'),
    
    # Mark as Undone
    path('markasundone/<int:pk>', views.mark_as_undone, name='mark_as_undone'),
    
    # EDIT Feature #
    path('edit_task/<int:pk>', views.edit_task, name='edit_task'),
    
    # Delete task #
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
]
