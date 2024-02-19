# zkintegration/management/commands/retrieve_data.py
from django.core.management.base import BaseCommand
from fingerprint.zk_integration import connect_to_device, get_attendance

class Command(BaseCommand):
    help = 'Retrieve ZKTeco device data'

    def handle(self, *args, **options):
        device_ip = '192.168.1.201'
        conn = connect_to_device(device_ip)
        attendance = get_attendance(conn)
        conn.disconnect()

        # Process and use the data as needed