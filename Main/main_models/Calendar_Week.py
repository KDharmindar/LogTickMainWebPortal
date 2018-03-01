from django.db import models

class Calendar_Week(models.Model):
    id = models.BigAutoField(primary_key=True)
    calendar_week = models.BigIntegerField()
    start_date = models.BigIntegerField()
    end_date = models.BigIntegerField()
    calendar_year = models.IntegerField()