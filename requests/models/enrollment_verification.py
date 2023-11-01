from django.db import models
from accounts.models import Student
from course.models import Term


class EnrollmentVerification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollment_verification_req_student')
    enrollment_verification_file = models.FileField()
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='enrollment_verification_req_term')
    issuance_certificate_place = models.CharField(max_length=200)