from django.contrib import admin

from .models import (Teacher, Department,
                     Klass, Subject)

admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Klass)
admin.site.register(Subject)
