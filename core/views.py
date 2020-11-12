from datetime import date
from django.shortcuts import render, get_object_or_404

from .models import Klass, Subject, Student, DailyAttendance


def take_attendance(request, klass_id, subject_id):
    klass = get_object_or_404(Klass, id=klass_id)
    subject = get_object_or_404(Subject, id=subject_id)
    students = Student.objects.filter(klass=klass)
    current_date = date.today()

    if request.method == 'POST':
        attendees = request.POST.getlist('attendance_choices')
        attendees = students.filter(id__in=list(map(int, attendees)))
        absence = students.exclude(id__in=attendees)

        for student in attendees:
            DailyAttendance.objects.create(
                date=current_date,
                taken_by=subject.instructor,
                klass=klass,
                student=student,
                subject=subject,
                presence=True
            )
        for student in absence:
            DailyAttendance.objects.create(
                date=current_date,
                taken_by=subject.instructor,
                klass=klass,
                student=student,
                subject=subject,
                presence=False
            )
        # print(attendees, absence, sep=' ATTENDEES|ABSENT ')
    ctx = {
        'klass': klass,
        'subject': subject,
        'students': students,
        'current_date': current_date,
    }
    return render(request, 'core/take_attendances.html', ctx)
