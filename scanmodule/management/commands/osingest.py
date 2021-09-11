from django.core.management.base import BaseCommand, CommandError
from scanmodule.models import *
import pytz

class Command(BaseCommand):
    help = 'The help information for this command.'
    
    def add_arguments(self, parser):



        parser.add_argument('--os_type', type=str, help='Opertion system Type.')
        parser.add_argument('--os_accuracy', type=str, help='Opertion system accuracy')
        parser.add_argument('--os_name', type=str, help='Opertion system Name')
        

        parser.add_argument('--os_fingerprint', type=str, default=None, help='Opertion system finger print.')
        parser.add_argument('--os_family', type=str, default=None, help='Opertion system family.')

        parser.add_argument('--os_vendor', type=str, help='Opertion system Vendor.')

        parser.add_argument('--os_cpe', type=str, help='Opertion system customer-provided equipment(cpe).')
        
        parser.add_argument('--host_ip_name_id', type=str, help='Scan IP id.')      

        parser.add_argument('--scan_name', type=str, help='Scan Name id.')

    def handle(self, *args, **options):
        print("options['scan_name']:", options['scan_name'])
        scan_name_id=SiteAssest.objects.get(scan_name=options['scan_name'])
        #print('scan_name_id: ',scan_name_id)
        scan_iphost = HostScanned(scan_name=scan_name_id)
        #print('scan_iphost: ',scan_iphost)
        #host_os_scanned = HostOsScanned(host_scanned=scan_iphost)

        #host_ip_name_id=HostScanned.objects.get(host_ip_name=scan_name_id)
        
        
        
        scan_iphost = HostOsScanned(
            os_type=options['os_type'],
            os_accuracy=options['os_accuracy'],
            os_name =options['os_name'],
            os_fingerprint=options['os_fingerprint'],
            os_family=options['os_family'],
            os_vendor=options['os_vendor'],
            os_cpe=options['os_cpe'],
            
            host_ip_name=scan_iphost,
            
            
        )
        try:

            scan_iphost.save()
            self.stdout.write(self.style.SUCCESS('Success HostOsScanned write'))
        except Exception as e:
            
            self.stdout.write(self.style.ERROR(e))


        