from django.db import models
from django_jalali.db import models as jmodels


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(to='college.Faculty', on_delete=models.CASCADE, related_name='faculty_course')
    pre_requisite = models.ManyToManyField('self', blank=True)
    co_requisite = models.ManyToManyField('self', blank=True)
    credits = models.IntegerField()
    course_type = models.CharField(max_length=50, choices=[
        ('core', 'عمومی'),
        ('specialized', 'تخصصی'),
        ('foundation', 'پایه'),
        ('elective', 'اختیاری'),
    ])

    def __str__(self):
        return self.name


class Term(models.Model):
    name = models.CharField(max_length=256)
    students = models.ManyToManyField(to='accounts.Student', related_name='term_student')
    professors = models.ManyToManyField(to='accounts.Professor', related_name='term_professor')
    TermCourses = models.ManyToManyField('TermCourse', related_name="+")
    selection_start_time = models.DateTimeField()
    selection_end_time = models.DateTimeField()
    classes_start_time = models.DateTimeField()
    classes_end_time = models.DateTimeField()
    update_start_time = models.DateTimeField()
    update_end_time = models.DateTimeField()
    emergency_cancellation_end_time = models.DateTimeField()
    exams_start_time = models.DateField()
    term_end_time = models.DateField()


class TermCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='term_course')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='term_course')
    exam_date_time = jmodels.jDateTimeField()
    exam_venue = models.CharField(max_length=50)
    professor = models.ForeignKey(to='accounts.Professor', on_delete=models.CASCADE, related_name='term_course')
    capacity = models.IntegerField()
    time = models.TimeField()
    day = models.IntegerField(
        choices=[(1, 'شنبه'), (2, 'یکشنبه'), (3, 'دوشنبه'), (4, 'سه شنبه'), (5, 'چهارشنبه'), (6, 'پنجشنبه'),
                 (7, 'جمعه')])

    def __str__(self):
        return self.course.name + ' - ' + self.term.name


class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_course')
    course_state = models.CharField(max_length=50, choices=[('passed', 'قبول'), ('failed', 'مردود')])
    grade = models.IntegerField()
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='student_course')

    def __str__(self):
        return self.course.name + ' - ' + self.term.name
