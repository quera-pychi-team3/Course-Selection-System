from rest_framework import permissions
from accounts.models import Student

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            student_obj = Student.objects.get(user=request.user)
            return student_obj is not None
        except Student.DoesNotExist:
            return False
