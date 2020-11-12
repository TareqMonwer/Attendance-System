from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name}"


class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"Dept: {self.name}, head: {self.head.name}"


class Klass(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    semester = models.SmallIntegerField()
    academic_session = models.CharField(max_length=50)
    batch = models.SmallIntegerField()
    section = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.department.name} - SEM: {self.semester} - SECTION: {self.section}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    klass = models.ForeignKey(Klass, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.klass}"
