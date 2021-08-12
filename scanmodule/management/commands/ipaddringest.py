from django.core.management.base import BaseCommand, CommandError
from scanmodule.models import *
import pytz

class Command(BaseCommand):
    help = 'The help information for this command.'
    
    def add_arguments(self, parser):
        parser.add_argument('--host_ip_name', type=str, help='IP address.')
        parser.add_argument('--resolved_hostname', type=str, help='Hostname')
        parser.add_argument('--resolve_type', type=str, help='Resolved host type')
        

        parser.add_argument('--mac_address', type=str, default=None, help='Host MAC address.')
        parser.add_argument('--mac_addr_type', type=str, default=None, help='Host Mac addr type.')

        parser.add_argument('--mac_vendor', type=str, help='Host MAC Address Vendor.')

        parser.add_argument('--host_state', type=str, help='Host state.')
        parser.add_argument('--host_state_method', type=str, help='host_state_method.')

        
        parser.add_argument('--host_state_ttl', type=str, help='host_state_ttl.') 
        parser.add_argument('--scan_name_id', type=str, help='Scan asset id.')      

    def handle(self, *args, **options):

        scan_name_id=SiteAssest.objects.get(scan_name=options['scan_name_id'])
        
        
        
        scan_iphost = HostScanned(
            host_ip_name=options['host_ip_name'],
            resolved_hostname=options['resolved_hostname'],
            resolve_type =options['resolve_type'],
            mac_address=options['mac_address'],
            mac_addr_type=options['mac_addr_type'],
            mac_vendor=options['mac_vendor'],
            host_state=options['host_state'],
            host_state_method=options['host_state_method'],
            host_state_ttl=options['host_state_ttl'],

            scan_name_id=int(scan_name_id.id),
            
            
        )
        try:

            scan_iphost.save()
            self.stdout.write(self.style.SUCCESS('Success HostScanned write'))
        except Exception as e:
            print('id scanned',scan_name_id.id)
            self.stdout.write(self.style.ERROR(e))


        