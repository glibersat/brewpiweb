from django.db import models

from viewflow.models import Process

class BrewPiProcessConfiguration(models.Model):
    class Meta:
        abstract = True

    def all(self, aModel):
        """
        Return all foreign keys of a given type
        """
        all_fks = [getattr(self, f.name) for f in self._meta.fields if type(f) == models.fields.related.ForeignKey]
        return aModel.objects.filter(pk__in=[fk.id for fk in all_fks if isinstance(fk, aModel)])



class BrewPiProcess(Process):
    class Meta:
        abstract = True

