from django.db import models

from devices.core.actuator.models import DS2413Actuator


class HERMSProcessConfiguration(BrewPiProcessConfiguration):
    valve_waterin = models.ForeignKey(DS2413Actuator, related_name='process_configuration')


class HERMSProcess(BrewPiProcess):
    pass
