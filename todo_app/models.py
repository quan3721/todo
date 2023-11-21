from django.db import models

# Create your models here.

class Task(models.Model):
    # field 1
    task = models.CharField(max_length=250)
    # field 2
    is_completed = models.BooleanField(default=False) # default : uncompleted task
    
    created_at = models.DateTimeField(auto_now_add=True) 
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task