from django.db import models
from django.contrib.auth.models import User
from Main.main_models.Project import Project

class ProjectTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    project = models.ForeignKey(Project, related_name="project", on_delete=models.CASCADE)
    team_member = models.ForeignKey(User, related_name="team_member", on_delete=models.CASCADE)
    is_teamLead = models.BooleanField(default=False)