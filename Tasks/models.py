from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    due_date = models.DateField(blank=True)
    due_time = models.TimeField(blank=True)
    notes = models.TextField(blank=True)
    status = models.BooleanField(default=False)


