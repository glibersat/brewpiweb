from django.db import models
from django.utils.translation import ugettext as _

from viewflow.models import Process


class BrewPiProcessConfiguration(models.Model):
    class Meta:
        abstract = True

    label = models.CharField(max_length=150, help_text=_("Name of this configuration"))

    def all(self, aModel):
        """
        Return all foreign keys of a given type
        """
        all_fks = [getattr(self, f.name) for f in self._meta.fields if type(f) == models.fields.related.ForeignKey]
        return aModel.objects.filter(pk__in=[fk.id for fk in all_fks if isinstance(fk, aModel)])

    def __str__(self):
        return "Process Configuration: {0}".format(self.label)



class BrewPiProcess(Process):
    class Meta:
        abstract = True
