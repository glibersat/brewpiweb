import time

from celery import shared_task
from celery.utils.log import get_task_logger

from devices.core.actuator.models import Valve

from process.flow import flow_job

logger = get_task_logger(__name__)


class HERMSTasks(object):
    """
    Common tasks performed during usage
    """
    @staticmethod
    def reset(activation, **kwargs):
        """
        Reset HERMS by:
        - closing all valves
        - turning off heating elements
        - stopping all pumps
        """
        process = activation.process
        config = process.configuration

        all_valves = config.all(Valve)
        # all_heating_elements = config.all(HeatingElement)
        # all_pumps = config.all(Pump)

        # Reset everything
        # all_heating_elements.stop()
        # all_pumps.stop()
        # all_valves.close()

        # Let the water in
        # config.m13.open()

        # config.hlt_heater.ramp_to(process.mash_temp)


class HERMSPrepareWaterTasks(object):
    """
    All tasks to prepare water for a brewday
    """
    @staticmethod
    def start_fill_hlt_with_cold_water(activation, **kwargs):
        """
        Step: Fill HLT with Cold Water
         - Open Valve M2
         - Run Pump1 until there's no more pressure
        """
        process = activation.process
        config = process.configuration

        # config.m2.open()
        # config.p1.run()

    @shared_task(bind=True)
    @flow_job()
    def check_fill_hlt_with_cold_water_is_done(self, activation):
        """
        Wait until the HLT has been filled with Cold Water (pressure drops)
        """
        process = activation.process
        config = process.configuration

        # while config.p1.pressure > 0.1:
        for i in range(5):
            logger.info("Still filling...")
            time.sleep(1)

    @staticmethod
    def stop_fill_hlt_with_cold_water(activation, **kwargs):
        """
        Stop filling HLT with cold water by:
         - Stopping P1
         - Closing M2
        """
        process = activation.process
        config = process.configuration

        # config.p1.stop()
        # config.m2.close()


