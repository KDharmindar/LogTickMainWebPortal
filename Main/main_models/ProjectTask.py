from django.db import models
from Main.main_models.Current_Status import Current_Status
from Main.main_models.Project import Project
from django.contrib.auth.models import User

class ProjectTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    project_id = models.ForeignKey(Project, verbose_name="Project", related_name="Project", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    end_date = models.DateTimeField(auto_now_add=True, blank=True)
    duration = models.DateTimeField(auto_now_add=True, blank=True)
    current_status = models.ForeignKey(Current_Status, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
