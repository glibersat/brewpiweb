from django.contrib import admin

from brewpi_webservice.admin import admin_site

from .models import HERMSProcess, HERMSProcessConfiguration

from viewflow.admin import ProcessAdmin


@admin.register(HERMSProcessConfiguration, site=admin_site)
class HERMSProcessConfigurationAdmin(admin.ModelAdmin):
    list_display = ['label']

@admin.register(HERMSProcess, site=admin_site)
class HERMSProcessAdmin(ProcessAdmin):
    pass
