from django.contrib import admin

from brewpi_webservice.admin import admin_site

from .models import HERMSProcessConfiguration


@admin.register(HERMSProcessConfiguration, site=admin_site)
class HERMSProcessConfigurationAdmin(admin.ModelAdmin):
    pass
