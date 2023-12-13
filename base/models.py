from django.db import models

# Create your models here.

class Car(models.Model):
    Brand = models.CharField(max_length=30)
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.Brand
