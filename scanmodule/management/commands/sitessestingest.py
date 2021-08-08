from django.core.management.base import BaseCommand, CommandError
from scanmodule.models import *
import pytz

class Command(BaseCommand):
    help = 'The help information for this command.'
    
    def add_arguments(self, parser):
        parser.add_argument('--site_name', type=str, help='Scanned site name.')
        parser.add_argument('--scan_name', type=str, help='Scan Name details')
        parser.add_argument('--location_name', type=str, help='Scan Location details')
        

        parser.add_argument('--lon', type=str, default=None, help='Scanned site longitude.')
        parser.add_argument('--lat', type=str, default=None, help='Scanned site latitude.')

        parser.add_argument('--site_ip_range1', type=str, help='Range scanne')

        parser.add_argument('--scan_time_start', type=str, help='Scanned start time.')
        parser.add_argument('--scan_timestr_start', type=str, help='Scanned start time string.')

        
        parser.add_argument('--scan_time_end', type=str, help='Scanned end time.')
        parser.add_argument('--scan_timestr_end', type=str, help='Scanned string end time.')

        parser.add_argument('--scan_elapsed', type=str, help='Scanned Elapsed time.')
        parser.add_argument('--scan_args', type=str, help='Scanned Argument.')
        parser.add_argument('--nmap_version', type=str, help='Nmap version.')
        

        

    def handle(self, *args, **options):

    
        
        scan_site = SiteAssest(
            scan_name=options['scan_name'],
            site_name=options['site_name'],
            location_name =options['location_name'],
            lon=float(options['lon']),
            lat=float(options['lat']),
            site_ip_range1=options['site_ip_range1'],
            scan_time_start=datetime.datetime.utcfromtimestamp(int(options['scan_time_start'])),
            scan_timestr_start=options['scan_timestr_start'],
            scan_time_end=datetime.datetime.utcfromtimestamp(int(options['scan_time_end'])),
            scan_timestr_end=options['scan_timestr_end'],
            scan_elapsed=float(options['scan_elapsed']),
            scan_args=options['scan_args'],
            nmap_version=options['nmap_version'],
            scan_id=1,
            
        )
        try:

            scan_site.save()
            self.stdout.write(self.style.SUCCESS('Success SiteAssest write'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(e))


        