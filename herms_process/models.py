from django.db import models
from django.utils.translation import ugettext as _

from process.models import BrewPiProcess, BrewPiProcessConfiguration

from devices.core.actuator.models import MotorizedValve, ManualValve


class HERMSProcessConfiguration(BrewPiProcessConfiguration):
    """
    Configuration for a HERMS Process Template
    """
    m2 = models.ForeignKey(MotorizedValve, help_text=_("Cold Water in HLT Valve"))
    m13 = models.ForeignKey(ManualValve, help_text=_("Tap Cold Water input)"))


class HERMSProcess(BrewPiProcess):
    """
    A process that drives a HERMS
    """
    configuration = models.ForeignKey(HERMSProcessConfiguration, related_name='process')

