from django.conf.urls import patterns, url, include

from viewflow import views as viewflow

from .flows import HERMSFlow

urlpatterns = patterns('',
    url(r'^herms/',
        include([
            HERMSFlow.instance.urls,
            url('^$', viewflow.ProcessListView.as_view(), name='index'),
            url('^tasks/$', viewflow.TaskListView.as_view(), name='tasks'),
            url('^queue/$', viewflow.QueueListView.as_view(), name='queue'),
            url('^details/(?P<process_pk>\d+)/$',
                viewflow.ProcessDetailView.as_view(), name='details')],
                namespace=HERMSFlow.instance.namespace),
        {'flow_cls': HERMSFlow})
)
