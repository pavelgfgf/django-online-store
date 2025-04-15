from django.db import models

# Create your models here.
class Ad(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name