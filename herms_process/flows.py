from django.utils.translation import ugettext as _

from viewflow.views import StartProcessView, ProcessView

from process import flow
from process.flow import this

from . import models, views
from .tasks import HERMSTasks, HERMSPrepareWaterTasks


class HERMSFlow(flow.BrewPiFlow):
    """
    A HERMS Flow based on https://github.com/BrewPi/herms-layout/
    """
    process_cls = models.HERMSProcess

    start = flow.Start(StartProcessView, fields=['configuration']) \
        .Next(this.reset)

    reset = flow.Execute(HERMSTasks.reset) \
        .Next(this.open_manual_valves)

    open_manual_valves = flow.View(ProcessView,
                                   task_description=_("Manually open Water Input valve: M13")) \
        .Next(this.start_fill_hlt_with_cold_water)

    start_fill_hlt_with_cold_water = flow.Execute(HERMSPrepareWaterTasks.start_fill_hlt_with_cold_water) \
        .Next(this.check_fill_hlt_with_cold_water_is_done)

    check_fill_hlt_with_cold_water_is_done = flow.ExecuteAsync(HERMSPrepareWaterTasks.check_fill_hlt_with_cold_water_is_done) \
        .Next(this.stop_fill_hlt_with_cold_water)

    stop_fill_hlt_with_cold_water = flow.Execute(HERMSPrepareWaterTasks.stop_fill_hlt_with_cold_water) \
        .Next(this.close_manual_valves)

    close_manual_valves = flow.View(ProcessView,
                                    task_description=_("Manually close Water Input valve: M13")) \
        .Next(this.end)


    end = flow.End()


