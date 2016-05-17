import os

from devices.core.actuator.models import Valve

def reset_herms(activation, **kwargs):
    """
    Reset HERMS by:
    - closing all valves
    - turning off heating elements
    - stopping all pumps
    """
    process = activation.process
    config = process.configuration

    all_valves = config.all(Valve)
    #all_heating_elements = config.all(HeatingElement)
    #all_pumps = config.all(Pump)

    # Reset everything
    # all_heating_elements.stop()
    # all_pumps.stop()
    # all_valves.close()

    # Let the Water in
    # config.m13.open()

    #config.hlt_heater.ramp_to(process.mash_temp)


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

def check_fill_hlt_with_cold_water_is_done(process, **kwargs):
    """
    Wait until the HLT has been filled with Cold Water (pressure drops)
    """
    config = process.configuration

    return False # (config.p1.pressure < 0.1)



def stop_fill_hlt_with_cold_water(activation, **kwargs):
    process = activation.process
    config = process.configuration

    # config.p1.stop()
    # config.m2.close()


