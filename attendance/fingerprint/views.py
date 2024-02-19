from django.shortcuts import render
from django.http import HttpResponse
from zk import ZK
from django.db import connection
from django.core.management import call_command
from fingerprint.models import ImprAttendanceTable
from datetime import date
from django.shortcuts import redirect
from django.http import JsonResponse


def index(request):
    attendance_list = ImprAttendanceTable.objects.filter(punch_date=date.today())

    context = {
        'attendance_list': attendance_list,
    }
    return render(request, 'frontend/index.html', context)


def attend(request):
    call_command('retrieve')  
    data = {
        'success': True,
        'message': 'Data stored into database successfully'
    }
    response = JsonResponse(data)
    return response