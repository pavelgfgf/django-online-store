from rest_framework import serializers
from .models import ListProduct

class ListProductSerialisers(serializers.ModelSerializer):
    class Meta: 
        model = ListProduct
        fields = '__all__'
        exclude = []