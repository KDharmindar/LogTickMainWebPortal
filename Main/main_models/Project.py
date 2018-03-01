from django.db import models
from django.contrib.auth.models import User
from Main.main_models.Current_Status import Current_Status
import datetime

class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    description = models.TextField(null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    current_status = models.ForeignKey(Current_Status, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    