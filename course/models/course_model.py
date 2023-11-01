from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Course(models.Model):
     name = models.CharField(max_length=50)
     faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE , related_name='faculty_course')
     prerequisite = models.ManyToManyField('self', blank=True)
     corequisite = models.ManyToManyField('self', blank=True)
     credits = models.IntegerField()
     course_type = models.CharField(max_length=50, choices=[
         ('core', 'عمومی'),
         ('specialized', 'تخصصی'),
         ('foundation', 'پایه'),
         ('elective', 'اختیاری'),
     ])


     def __str__(self):
         return self.name