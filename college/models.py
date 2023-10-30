from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=256)


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=256)
    group = models.CharField(max_length=256)
    faculty = models.ForeignKey(to=Faculty, on_delete=models.CASCADE, related_name='FOS')
    units = models.IntegerField()
    degree = models.CharField(max_length=256)


class Term(models.Model):
    name = models.CharField(max_length=256)
    students = models.ManyToManyField(to='accounts.Student', related_name='terms')
    professors = models.ManyToManyField(to='accounts.Professor', related_name='terms')
    TermCourses = models.ManyToManyField(to='courses.TermCourse', related_name='terms')
    selection_start_time = jmodels.jDateTimeField()
    selection_end_time = jmodels.jDateTimeField()
    classes_start_time = jmodels.jDateTimeField()
    classes_end_time = jmodels.jDateTimeField()
    update_start_time = jmodels.jDateTimeField()
    update_end_time = jmodels.jDateTimeField()
    emergency_cancellation_end_time = models.DateTimeField()
    exams_start_time = jmodels.jDateField()
    term_end_time = jmodels.jDateField()
