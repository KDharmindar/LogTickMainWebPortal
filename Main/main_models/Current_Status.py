from django.db import models

class Current_Status(models.Model):
    id=models.BigAutoField(primary_key=True)
    current_status=models.CharField(max_length=10, default="Running")
    
    def __str__(self):
        return self.current_status
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    