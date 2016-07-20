import logging

from celery.signals import celeryd_init
from celery.task import Task
from celery.utils.log import get_task_logger

from datasync.controlbox import ControlboxSyncher
from .models import Controller

LOGGER = get_task_logger(__name__)


class ConnectorTask(Task):
    """A Celery Task that runs at startup and listen to controlbox-connect-py
    events"""

    def __init__(self):
        self.syncher = ControlboxSyncher()

    def run(self, **kwargs):
        print("STARTING")
        LOGGER.debug("STARTING LOGGER")
        self.syncher.run()

@celeryd_init.connect()
def run_connector_task_at_startup(conf=None, **kwargs):
    ct = ConnectorTask()
    ct.run()
