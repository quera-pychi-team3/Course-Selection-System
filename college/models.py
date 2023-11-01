from django.db import models


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=256)


class FieldOfStudy(models.Model):
    name = models.CharField(max_length=256)
    group = models.CharField(max_length=256)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='FOS')
    units = models.IntegerField()
    degree = models.CharField(max_length=256)



