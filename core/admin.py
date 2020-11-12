from django.contrib import admin

from .models import (Teacher, Department,
                     Klass, Subject,
                     Student, DailyAttendance)

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Klass)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(DailyAttendance)
