from unittest.mock import MagicMock

from django.apps.registry import Apps
from django.apps import apps
from django.db import models
from django.test import TestCase
from django.db.models.signals import post_save
from django.dispatch import receiver

from device.models import Sensor
from controller.models import Controller

from .models import TimeSeriesMixin
from .models import TimeSeries

class TestSensor(Sensor, TimeSeriesMixin):
    class Meta:
        app_label = "datalogging_test"

    temperature = models.SmallIntegerField()


@timeseries.register(TestSensor)
class TestSensorSeries(TimeSeries):
    series_name = "test_sensor"
    fields = ['temperature']

@receiver(post_save)
def log_timeseries(sender, instance, **kwargs):
    from . import timeseries
    if sender in timeseries:
        instance.write_timeseries()



class TimeSeriesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.controller = Controller.objects.create()

    def test_logging_on_save(self):

        TestSensor._save_table = MagicMock(return_value=True)

        sensor = TestSensor(controller=self.controller)
        sensor.temperature = 10

        sensor.save()





