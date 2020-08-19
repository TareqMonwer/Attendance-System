from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model



class Attendance(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    check_in = models.DateTimeField(auto_now_add=True)
    check_out = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} in: {self.check_in} out: {self.check_out}"
    
    def working_hours(self):
        if self.check_out:
            hours = self.check_out - self.check_in
            seconds = hours.total_seconds()
            seconds = seconds % (24 * 3600) 
            hour = seconds // 3600
            seconds %= 3600
            minutes = seconds // 60
            seconds %= 60
            return f"{hour} Hours {minutes} Minutes"
        else:
            return
    
    def get_status(self):
        if self.check_in and not self.check_out:
            return "in"
        else:
            return "out"