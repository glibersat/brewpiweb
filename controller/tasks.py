from celery.task import Task
from celery.signals import celeryd_init

import time

from .models import Controller

class ConnectorTask(Task):
    """A Celery Task that runs at startup and listen to controlbox-connect-py
    events"""
    def run(self, **kwargs):
        while True:
            Controller.objects.get_or_create(name="Sample BrewPi", uri="nowhere://")
            time.sleep(10)


@celeryd_init.connect()
def run_connector_task_at_startup(conf=None, **kwargs):
    ct = ConnectorTask()
    ct.run()
