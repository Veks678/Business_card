from django.db import models

class Publications(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    section = models.CharField(max_length=100)

    url = models.CharField(max_length=200)
    focus_id = models.CharField(max_length=200)