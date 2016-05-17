from viewflow.views import StartProcessView, ProcessView

from process import flow
from process.flow import this

from . import models, tasks, views


class HERMSFlow(flow.BrewPiFlow):
    """
    A Sample HERMS Flow
    """
    process_cls = models.HERMSProcess

    start = flow.Start(StartProcessView, fields=['configuration']) \
        .Next(this.reset)

    reset = flow.Execute(tasks.reset_herms) \
        .Next(this.open_manual_valves)

    open_manual_valves = flow.View(ProcessView) \
        .Next(this.start_fill_hlt_with_cold_water)

    start_fill_hlt_with_cold_water = flow.Execute(tasks.start_fill_hlt_with_cold_water) \
        .Next(this.check_fill_hlt_with_cold_water_is_done)

    check_fill_hlt_with_cold_water_is_done = flow.If(tasks.check_fill_hlt_with_cold_water_is_done) \
        .OnTrue(this.stop_fill_hlt_with_cold_water) \
        .OnFalse(this.stop_fill_hlt_with_cold_water)

    stop_fill_hlt_with_cold_water = flow.Execute(tasks.stop_fill_hlt_with_cold_water) \
        .Next(this.end)

    end = flow.End()


