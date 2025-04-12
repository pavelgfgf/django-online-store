from django.db import models
from products.models import Product
from authorization.models import CustomUser

# Create your models here.
class ProductBuy(models.Model):
    STATUS_CHOICES = [
    ('pending', 'В процессе'),
    ('success', 'Оплачен'),
    ('failed', 'Ошибка'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')