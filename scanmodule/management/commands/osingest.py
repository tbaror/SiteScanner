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

    def handle(self, *args, **options):

        host_ip_name_id=HostScanned.objects.get(host_ip_name=options['scan_name_id'])
        
        
        
        scan_iphost = HostOsScanned(
            host_ip_name=options['os_type'],
            resolved_hostname=options['os_accuracy'],
            resolve_type =options['os_name'],
            mac_address=options['os_fingerprint'],
            mac_addr_type=options['os_family'],
            mac_vendor=options['os_vendor'],
            host_state=options['os_cpe'],
            
            host_ip_name_id=int(host_ip_name_id.id),
            
            
        )
        try:

            scan_iphost.save()
            self.stdout.write(self.style.SUCCESS('Success HostOsScanned write'))
        except Exception as e:
            
            self.stdout.write(self.style.ERROR(e))


        