from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_list_or_404
from .models import Product, ProductBuy

# Create your views here.
class BuyProductList(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        order = ProductBuy.objects.get(pk=pk)

        pay_url = f'https://payment.example.com/pay?order_id={pk}'

        return Response({'pay_url': pay_url}, status=status.HTTP_200_OK)