from django.db import models

class Employee(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.CharField(max_length=255)

