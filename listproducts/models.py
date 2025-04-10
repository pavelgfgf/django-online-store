from django.db import models

# Create your models here.
class ListProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name