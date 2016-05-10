from django.db import models

from viewflow.models import Process

class BrewPiProcessConfiguration(models.Model):
    class Meta:
        abstract = True


class BrewPiProcess(Process):
    class Meta:
        abstract = True

    configuration = models.ForeignKey(BrewPiProcessConfiguration)



