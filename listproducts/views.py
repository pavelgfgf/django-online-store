from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ListProduct
from .serializer import ListProductSerialisers

# Create your views here.
class ListProductDetails(APIView):
    def get_object(self, pk):
        try:
            return ListProduct.objects.get(pk=pk)
        except ListProduct.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    def get(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ListProductSerialisers(products)
        return Response({'data': [serializer.data]})