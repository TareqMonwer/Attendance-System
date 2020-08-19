from datetime import datetime
from django.shortcuts import render, HttpResponse

from .models import Attendance


def attendance(request):
    attendances = Attendance.objects.filter(user=request.user)
    last_attendance = Attendance.objects.filter(user=request.user).last()
    current_dt = datetime.now()
    valid_dt = datetime.strptime(str(current_dt), '%Y-%m-%d %H:%M:%S.%f')
    
    try:
        status = last_attendance.get_status()
    except:
        status = "out"

    if status == "in":
        status_display = "Check Out"
    elif status == "out":
        status_display = "Check In"

    if request.method == 'POST':
        req_status = request.POST.get('status')

        if req_status == 'in':
            # User is already in office, wants to check out
            last_attendance.check_out = datetime.now()
            last_attendance.save()
            return HttpResponse("attendance updated")
        elif req_status == 'out':
            # User want's to check in.
            attendance = Attendance.objects.create(user=request.user)
            return HttpResponse("attendance created")
    ctx = {'status': status, 'status_display': status_display, 'attendances': attendances}
    return render(request, 'core/attendance.html', ctx)

