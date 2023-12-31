from django.db import models
from accounts.models import Student
from course.models.course import Course
from django.utils.translation import gettext_lazy as _
from shared.models import BaseModel


class Registration(BaseModel):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE, related_name='reg_student',
                                verbose_name=_('دانشجوی درخواست دهنده'))
    courses = models.ManyToManyField(to=Course, verbose_name=_('دروس درخواستی'))
    approval_status = models.BooleanField(default=False, verbose_name=_('وضعیت تایید'))
