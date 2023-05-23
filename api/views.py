from django.shortcuts import render

from .models import Jadwal
from .serializers import JadwalSerializer
from rest_framework import viewsets, permissions

# create your views here.

class JadwalViewSet(viewsets.ModelViewSet):
    queryset = Jadwal.objects.all()
    serializer_class = JadwalSerializer

