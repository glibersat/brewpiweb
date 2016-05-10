import os

def reset_herms(self, activation, **kwargs):
    """
    Reset HERMS by:
    - closing all valves
    - turning off heating elements
    - stopping all pumps
    """
    process = activation.process
    config = process.configuration

    all_valves = Valve.installed_with(config)
    all_heating_elements = HeatingElement.installed_with(config)
    all_pumps = Pump.installed_with(config)

    # Reset everything
    all_heating_elements.stop()
    all_pumps.stop()
    all_valves.close()

    # Let the Water in
    config.valve_waterin.open()

    config.hlt_heater.ramp_to(process.mash_temp)

