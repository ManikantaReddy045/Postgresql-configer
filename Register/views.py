from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework import viewsets
from .models import Register
# Create your views here.


class Registerview(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = Register.objects.all()