from django.contrib import admin
from .models import SiteAssest, ScanTemplate, ScanSet


# Register your models here.
admin.site.register(SiteAssest)
admin.site.register(ScanTemplate)
admin.site.register(ScanSet)

