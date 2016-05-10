from django.conf import settings
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brewpi_webservice.settings')

app = Celery('brewpi_webservice',
             broker='django://',
             include=['controller.tasks'])


