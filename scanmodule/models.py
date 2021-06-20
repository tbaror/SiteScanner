from django.db import models
import datetime


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
    scan_name = models.CharField(max_length=250,blank=False)
    site_name = models.CharField(max_length=250,blank=False)
    location_name = models.CharField(max_length=250,blank=False)
    # Geo location
    lon = models.FloatField()
    lat = models.FloatField()
    site_ip_range1 = models.CharField(max_length=250,blank=True)
    site_ip_range2 = models.CharField(max_length=250,blank=True)
    site_ip_range3 = models.CharField(max_length=250,blank=True)
    #new entry
    scan_time_start = models.DateTimeField(default=datetime.date.today())
    scan_timestr_start = models.CharField(max_length=250,blank=True)
    scan_time_end = models.DateTimeField(default=datetime.date.today())
    scan_timestr_end = models.CharField(max_length=250,blank=True)
    scan_elapsed = models.IntegerField(blank=True, null=True)
    scan_exit_resault = models.CharField(max_length=50,blank=True)
    scan_args = models.CharField(max_length=250,blank=True)
    nmap_version = models.CharField(max_length=50,blank=True)

    # end new entry

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
        return self.scan_name


class ScanHistory(models.Model):
    site_name = models.ForeignKey(SiteAssest, on_delete=models.CASCADE)
    scan_date_record = models.DateTimeField()
    scan_complete = models.BooleanField(null=True)
    scan_rank = models.IntegerField(default=0, null=True)
    scan_name = models.CharField(max_length=250,blank=True,default="DEF")

    def __str__(self):
        return str(self.site_name)

    def monthscan(self):
        return self.scan_date_record.strftime('%B')
    
class HostScanned(models.Model):
    scan_name = models.ForeignKey(SiteAssest, on_delete=models.CASCADE)
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

    def __str__(self):
        return str(self.os_type)


class PortDiscovery(models.Model):
    host_ip_name = models.ForeignKey(SiteAssest, on_delete=models.CASCADE)
    port_protocol = models.CharField(max_length=50,blank=True)
    portid = models.IntegerField(blank=True, null=True)
    port_stat = models.CharField(max_length=50,blank=True)
    port_scanned_method = models.CharField(max_length=50,blank=True)
    port_scanned_ttle = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return str(self.portid)

class PortServiceDsocovery(models.Model):

    portid = models.ForeignKey(PortDiscovery, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=50,blank=True)
    service_product = models.CharField(max_length=100,blank=True)
    Service_version = models.CharField(max_length=100,blank=True)
    service_extrainfo = models.CharField(max_length=200,blank=True)
    service_os_related = models.CharField(max_length=50,blank=True)
    service_method_scanned = models.CharField(max_length=50,blank=True)
    conf = models.CharField(max_length=50,blank=True)
    service_cpe = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return str(self.service_name)

class ServiceScript(models.Model):
    service_product = models.ForeignKey(PortServiceDsocovery, on_delete=models.CASCADE)
    name_service = models.CharField(max_length=100,blank=True)
    banner_raw = models.CharField(max_length=100,blank=True)
    script_name = models.CharField(max_length=100,blank=True)
    raw_output = models.CharField(max_length=500,blank=True)
    cve_cpe = models.CharField(max_length=200,blank=True)
    is_exploit = models.BooleanField()
    cve_type = models.CharField(max_length=100,blank=True)
    cvss = models.IntegerField(blank=True, null=True)
    cve_id = models.CharField(max_length=200,blank=True)
    cve_url = models.URLField(max_length=200,blank=True)

    def __str__(self):
        return str(self.name_service)
    






    