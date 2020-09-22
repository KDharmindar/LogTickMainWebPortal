from django.db import models
from django.contrib.auth.models import User
#from Main.main_models.Current_Status import Current_Status
import datetime

class ProcessedData(models.Model):
    process_id = models.BigIntegerField(default=1)
    # project_id = models.BigIntegerField(default=1)
    # task_id = models.BigIntegerField(default=1)
    # start_time = models.TimeField(null=True)
    # end_time = models.TimeField(null=True)
    # user_id = models.BigIntegerField(default=9999)
    # weekend_id = models.BigIntegerField(default=1)
    # duration = models.TimeField(null=True)
    image_data = models.ImageField(upload_to='images', blank=True)
    
    
    
    def __str__(self):
        return self.process_id
