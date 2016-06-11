"""
This module holds all the generic Models about devices
"""

from django.db import models
from django.utils.translation import ugettext as _

from polymorphic.models import PolymorphicModel

from controller.models import Controller


class Device(PolymorphicModel):
    """
    Any hardware device such as a Temperature Sensor or a Valve
    """
    label = models.CharField(max_length=255, default="Unnamed Device", blank=True, null=True)

    def __str__(self):
        return "{0}: {1}".format(self.__class__.__name__, self.label)


class ElectronicDevice(Device):
    """
    A mixin meaning the device (sensor, actuator) is operated by electricity
    and is connected to a Controller.
    """
    uri = models.CharField(max_length=255, help_text=_("A device URI such as onewire://182377282"))

    slot = models.PositiveIntegerField(blank=True, null=True,
                                       help_text=_("The slot ID assigned paired with the Controller"))

    controller = models.ForeignKey(Controller, related_name='devices')

    @property
    def is_installed(self):
        return self.slot is not None


# Sensors  --------------------------------------------------------
class Sensor(ElectronicDevice):
    """
    A sensor is an object whose purpose is to detect events or changes
    in its environment, and then provide a corresponding output.
    """
    pass


# Actuators --------------------------------------------------------
class ManualActuator(Device):
    """
    An Manual Actuator is a type of device moved by human force.
    """
    pass


class Actuator(ElectronicDevice):
    """
    An actuator is a type of motor that is responsible for moving or
    controlling a mechanism or system.
    """
    pass


class PWMActuator(Actuator):
    """
    An actuator that is driven by Pulse Width Modulation (PWM)
    """
    class Meta:
        abstract = True
