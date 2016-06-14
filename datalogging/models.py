from django.db import models

from model_utils import FieldTracker


class InfluxSerializer(object):
    def serialize(self, aModel):
        json = {}
        json['measurement'] = aModel._meta.timeseries_name
        json['time'] = aModel._meta.timeseries_datefield
        json['fields'] = aModel._meta.timeseries_fields

        return json

class TimeSeriesMixin(object):
    timeseries_tracker = FieldTracker()

    def __init__(self):
        self.serializer = InfluxSerializer()

    def write_timeseries(self):
        json = self.serializer.serialize(self)
        client = InfluxDBClient('localhost', 8086, 'root', 'root', 'brewpi')
        client.write_points(json_body)


class TimeSeries(object):
    pass
