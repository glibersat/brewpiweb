from viewflow.views import StartProcessView, ProcessView

from process import flow
from process.flow import this

from . import models, tasks


class HERMSFlow(flow.BrewPiFlow):
    """
    A Sample HERMS Flow
    """
    process_cls = models.HERMSProcess

    start = flow.Start(StartProcessView) \
        .Next(this.reset)

    reset = flow.Execute(tasks.reset_herms) \
        .Next(this.end)

    approve = flow.View(ProcessView) \
        .Next(this.check_approve)

    check_approve = flow.If(cond=lambda p: p.approved) \
        .OnTrue(this.end) \
        .OnFalse(this.end)

    end = flow.End()



