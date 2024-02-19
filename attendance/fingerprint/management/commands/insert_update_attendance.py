from django.core.management.base import BaseCommand
from fingerprint.models import Attendance, ImprAttendanceTable, Contacts


class Command(BaseCommand):
    def handle(self, *args, **options):
        imprt_att_data = ImprAttendanceTable.objects.filter(is_validate=0)
        
        for data in imprt_att_data:
            get_contact_id = Contacts.objects.filter(fingerprint_card_serial_no=data.card_no).first()
            
            if get_contact_id:
                get_attendance = Attendance.objects.filter(
                    punch_date=data.punch_date,
                    contact_id=get_contact_id.id
                )

                if get_attendance:
                    get_attendance.update(out_time=data.in_time)
                    data.is_validate = 1  
                    data.save()
                else:
                    new_attendance = Attendance(
                        contact_id=get_contact_id.id, 
                        card_no=data.card_no,
                        punch_date=data.punch_date,
                        in_time=data.in_time,
                        type='Finger',
                        contact_type='student'
                        )
                    new_attendance.save()
