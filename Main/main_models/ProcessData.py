from django.db import models
from django.contrib.auth.models import User
from Main.main_models.Current_Status import Current_Status
import datetime

class ProcessData(models.Model):
    process_id = models.BigIntegerField()
    project_id = models.BigIntegerField()
    task_id = models.BigIntegerField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    user_id = models.BigIntegerField(default=9999)
    weekend_id = models.BigIntegerField(default=1)
    duration = models.TimeField(null=True)
    image_data = models.TextField(default='')
    
    
    def __str__(self):
        return self.process_id
