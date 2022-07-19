from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=30,null=True)
    edad = models.IntegerField(default=0)
    cumpleanos = models.DateField(default="2006-03-31")