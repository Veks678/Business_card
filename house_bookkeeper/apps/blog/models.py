from django.db import models

class Publications(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True, blank=True)

