from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','password', 'first_name','last_name','email')
        

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('created_by',)
        
        
class TaskForm(ModelForm):
    class Meta:
        model = ProjectTask
        exclude = ('created_by',)        