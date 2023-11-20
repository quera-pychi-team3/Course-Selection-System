from rest_framework import serializers
from course.models import StudentCourse


class StudentCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'
