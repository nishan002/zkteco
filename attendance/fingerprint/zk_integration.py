# zkintegration/zk_integration.py
from zk import ZK
import json
from fingerprint.models import ImprAttendanceTable, BatchImportTable
from django.db import transaction
import datetime

def connect_to_device(device_ip, device_port=4370):
    zk = ZK(device_ip, port=device_port)
    conn = zk.connect()
    return conn

def get_attendance(conn):
    get_data = conn.get_attendance()
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%d-%m-%Y-%H:%M:%S")
    batch = BatchImportTable(name=formatted_datetime, type='attendance')
    batch.save()

    formatted_attendance = []
    for entry in get_data:
        entry = str(entry)
        entry = entry.split(": ")
        card_no =   
        in_time = entry[2].split(" ")[1]
        punch_date = entry[2].split(" ")[0]

        new_data = ImprAttendanceTable(card_no=card_no, in_time=in_time, punch_date=punch_date, batch_id = batch.id, is_validate=0)
        try:
            new_data.save()
            print("Success")
        except Exception as e:
            print("Error:", str(e))
    
    conn.clear_attendance()

     