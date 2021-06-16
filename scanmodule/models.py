from django.db import models


# Create your models here.

class ScanTemplate(models.Model):
    template_name = models.CharField(max_length=250)
    scan_options = models.CharField(max_length=250)
    scan_script = models.CharField(max_length=250)

    NMAP_OUTPUT_CHOICES = [
    ('XM', 'XML'),
    ('LS', 'LOGSTASH'),
    
    ]
    output_format = models.CharField(max_length=2,choices=NMAP_OUTPUT_CHOICES,default='XML')

    def __str__(self):
        return self.template_name

class ScanSet(models.Model):
    scanset_name = models.CharField(max_length=250)
    scan_template = models.ForeignKey(ScanTemplate, on_delete=models.RESTRICT)
    scan_every_min = models.IntegerField(blank=True, null=True)
    scan_every_days = models.IntegerField(blank=True, null=True)
    scan_every_month = models.IntegerField(blank=True, null=True)
    scan_start_time = models.TimeField(auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.scanset_name


class SiteAssest(models.Model):
    site_name = models.CharField(max_length=250,blank=False)
    location_name = models.CharField(max_length=250,blank=False)
    # Geo location
    lon = models.FloatField()
    lat = models.FloatField()
    site_ip_range1 = models.CharField(max_length=250,blank=True)
    site_ip_range2 = models.CharField(max_length=250,blank=True)
    site_ip_range3 = models.CharField(max_length=250,blank=True)
    last_scaned = models.DateField(auto_now_add=False)
    TASK_STATUS_CHOICES = [
    ('ID', 'IDLE'),
    ('RU', 'RUNNING'),
    
    ]
    current_status = models.CharField(max_length=2,choices=TASK_STATUS_CHOICES,default='IDLE')

    site_rank = models.IntegerField()

    scan = models.ForeignKey(ScanSet, on_delete=models.RESTRICT)
    scan_count = models.IntegerField(default=0)


    def __str__(self):
        return self.site_name


class ScanHistory(models.Model):
    site_name = models.ForeignKey(SiteAssest, on_delete=models.CASCADE)
    scan_date_record = models.DateTimeField()
    scan_complete = models.BooleanField(null=True)
    scan_rank = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.site_name)

    def monthscan(self):
        return self.scan_date_record.strftime('%B')
    
class HostScanned(models.Model):
    site_name = models.ForeignKey(SiteAssest, on_delete=models.CASCADE)
    host_ip_name = models.CharField(max_length=250,blank=True)
    resolved_hostname = models.CharField(max_length=250,blank=True)
    resolve_type = models.CharField(max_length=250,blank=True)
    mac_address = models.CharField(max_length=250,blank=True)
    mac_addr_type = models.CharField(max_length=250,blank=True)
    mac_vendor = models.CharField(max_length=250,blank=True)
    host_state = models.CharField(max_length=50,blank=True)
    host_state_method = models.CharField(max_length=50,blank=True)
    host_state_ttl = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return str(self.host_ip_name)



class HostOsScanned(models.Model):
    host_ip_name = models.ForeignKey(SiteAssest, on_delete=models.CASCADE)
    os_type = models.CharField(max_length=50,blank=True)
    os_accuracy = models.CharField(max_length=50,blank=True)







    