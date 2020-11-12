from django.urls import path

from . import views


urlpatterns = [
    path('attendance/<int:klass_id>/<int:subject_id>/', views.take_attendance, name='take_attendance'),
]