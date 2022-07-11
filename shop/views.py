from django.shortcuts import render

from rest_framework import viewsets

from .serializers import  NGSDataSerializer
from .models import NGSData

class NGSViewSet(viewsets.ModelViewSet):
    queryset = NGSData.objects.all()
    serializer_class =  NGSDataSerializer



# Create your views here.
