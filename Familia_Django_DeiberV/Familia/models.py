from django.db import models
from django.forms import CharField, DateField, IntegerField

class Familiar(models.Model):
    nombre = CharField(max_length=20)
    edad = IntegerField()
    cumpleanos = DateField()