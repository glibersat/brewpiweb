from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from .models import ElectronicDevice
from .serializers import ElectronicDeviceSerializer


class ElectronicDeviceViewSet(viewsets.ModelViewSet):
    queryset = ElectronicDevice.objects.all()
    serializer_class = ElectronicDeviceSerializer
