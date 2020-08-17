from django.db import models

# Create your models here.
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

    def __str__(self):
        return self.site_name

class ScanSet(models.Model):
    scanset_name = models.CharField(max_length=250)
    scan_template = models.ForeignKey(ScanTemplate, on_delete=models.RESTRICT)
    scan_schedule =


    def __str__(self):
        return self.scanset_name

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