from django.shortcuts import render
from rest_framework import generics, filters, viewsets
from .models import Food
from .serializers import FoodSerializer


class FoodAPIView(generics.ListCreateAPIView):
    search_fields = ['name', 'price']
    filter_backends = (filters.SearchFilter, )
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
