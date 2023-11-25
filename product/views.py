# from django.shortcuts import render

# from rest_framework.generics import ListAPIView

# from product.models import Product
# from product.serializer import ProductSerializer
# from django.shortcuts import render

# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser 
# from rest_framework import status

# from rest_framework.decorators import api_view

# class ProductList(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer()
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from product.models import Product
from .serializer import ProductSerializer

class TodoListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        todos = Product.objects.all()
        serializer = ProductSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
