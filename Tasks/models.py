from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Tasks(models.Model):
    name = models.CharField(max_length=100)
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    due_date = models.DateField()
    due_time = models.TimeField()
    notes = models.TextField()
    done = models.BooleanField(default=False)


