from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Age = models.CharField(max_length=255)

