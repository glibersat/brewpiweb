from viewflow import (
    flow as viewflow_flow,
    lock
)
from viewflow.base import this, Flow
from viewflow.flow import (
    Start,
    Handler as Execute,
    If,
    View,
    End,
    Function,
    flow_job
)
from viewflow.contrib.celery import (
    Job as ExecuteAsync
)


class BrewPiFlow(Flow):
    """
    A flow that modelizes some process
    """
    lock_impl = lock.select_for_update_lock
