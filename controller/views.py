from rest_framework import viewsets
from rest_framework.response import Response

from .models import Controller
from .serializers import ControllerSerializer


class ControllerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to manage Controllers
    """
    queryset = Controller.objects.all().order_by('name')
    serializer_class = ControllerSerializer
