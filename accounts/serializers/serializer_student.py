from rest_framework import serializers
from accounts.models import Student


class StudentSerializerITAdmin(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'