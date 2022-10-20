from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Things(models.Model):
    name = models.CharField(
        max_length=30, unique=True, blank=False
    )
    description = models.CharField(max_length=120, blank=True)
    quantity = models.IntegerField(validator=[MinValueValidator(0), MaxValueValidator(100)])
