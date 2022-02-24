from django.db import models

class Writing(models.Model):
    publication = models.DateTimeField(auto_now_add=True)
    filling = models.TextField(null=True, blank=True)


