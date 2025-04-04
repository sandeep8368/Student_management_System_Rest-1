from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from app.serializers import studentSerializers
from app.models import studentModel

class studentViewSet(viewsets.ModelViewSet):
    queryset = studentModel.objects.all()
    serializer_class = studentSerializers