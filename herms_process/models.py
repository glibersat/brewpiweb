from django.db import models
from django.utils.translation import ugettext as _

from process.models import BrewPiProcess, BrewPiProcessConfiguration

from devices.core.actuator.models import MotorizedValve, ManualValve


class HERMSProcessConfiguration(BrewPiProcessConfiguration):
    m2 = models.ForeignKey(MotorizedValve, help_text=_("Cold Water in HLT Valve (Motorized)"))
    m13 = models.ForeignKey(ManualValve, help_text=_("Tap Cold Water input (Manual)"))


class HERMSProcess(BrewPiProcess):
    configuration = models.ForeignKey(HERMSProcessConfiguration, related_name='process')
