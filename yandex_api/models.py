from django.db import models

class Route(models.Model):
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)
    distance = models.CharField(max_length=50, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)