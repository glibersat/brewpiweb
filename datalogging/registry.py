class TimeSeriesRegistry(object):
    def __init__(self):
        self._registry = {}  # model_class class -> timeseries instance

    def register(self, model, timeseries_class):
        timeseries_obj = timeseries_class(model, self)
        self._registry[model] = admin_obj

