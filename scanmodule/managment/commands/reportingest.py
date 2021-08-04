from django.core.management.base import BaseCommand, CommandError
from scanmodule.models import *

class Command(BaseCommand):
    help = 'The help information for this command.'
    
    def add_arguments(self, parser):
        parser.add_argument('--scan_name', type=str, help='Scan Name details')
        parser.add_argument('--site_name', type=str, help='Scanned site name.')

        parser.add_argument('--lon_site', type=int, default=None, help='Scanned site longitude.')
        parser.add_argument('--lat_site', type=int, default=None, help='Scanned site latitude.')

        parser.add_argument('--site_ip_range1', type=str, help='Range scanne')

        parser.add_argument('--scan_time_start', type=str, help='Scanned start time.')
        parser.add_argument('--scan_timestr_start', type=str, help='Scanned start time string.')

        
        parser.add_argument('--scan_time_end', type=str, help='Scanned end time.')
        parser.add_argument('--scan_timestr_end', type=str, help='Scanned string end time.')

        parser.add_argument('--scan_elapsed', type=float, help='Scanned Elapsed time.')
        parser.add_argument('--scan_args', type=str, help='Scanned Argument.')
        parser.add_argument('--nmap_version', type=str, help='Nmap version.')
        

        

    def handle(self, *args, **options):
        
        scan_site = SiteAssest(
            scan_name=options['scan_name'],
            site_name=options['site_name'],
            lon_site=options['lon_site'],
            lat_site=options['lat_site'],
            site_ip_range1=options['site_ip_range1'],
            scan_time_start=options['scan_time_start'],
            scan_timestr_start=options['scan_timestr_start'],
            scan_time_end=options['scan_time_end'],
            sscan_timestr_end=options['scan_timestr_end'],
            scan_elapsed=options['scan_elapsed'],
            scan_args=options['scan_args'],
            nmap_version=options['nmap_version'],
            
        )
        scan_site.save()
        