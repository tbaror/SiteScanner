from django.contrib import admin
from .models import SiteAssest, ScanTemplate, ScanSet, ScanHistory, HostScanned, HostOsScanned, PortDiscovery, PortServiceDsocovery, ServiceScript


# Register your models here.
admin.site.register(SiteAssest)
admin.site.register(ScanTemplate)
admin.site.register(HostScanned)
admin.site.register(HostOsScanned)
admin.site.register(PortDiscovery)
admin.site.register(PortServiceDsocovery)
admin.site.register(ServiceScript)

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('site_name','scan_date_record','scan_complete', 'scan_rank')
    search_fields = ('site_name','scan_date_record','scan_complete', 'scan_rank')
    readonly_fields=['scan_date_record']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(ScanHistory, HistoryAdmin)

