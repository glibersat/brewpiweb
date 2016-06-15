from rest_framework import serializers

from .models import ElectronicDevice


class ElectronicDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ElectronicDevice
        exclude = ('polymorphic_ctype',)
        read_only_fields = ('uri', 'slot',)
