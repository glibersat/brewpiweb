from rest_framework import serializers

from device.models import ElectronicDevice
from device.serializers import ElectronicDeviceSerializer

from .models import Controller


class ControllerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Controller
        fields = ('name', 'url', 'alive', 'devices')
        read_only_fields = ('alive', 'url')

    devices = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        lookup_field='pk',
        view_name='electronicdevice-detail'
    )
