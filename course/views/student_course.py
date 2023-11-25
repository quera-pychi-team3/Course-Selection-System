from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from accounts.models.student import Student
from accounts.permissions.professor import IsProfessor
from accounts.permissions.student import IsStudent
from course.models.course import Course
from course.serializers.course import CourseSerializer


@extend_schema(tags=["term"])
class StudentCoursesViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = (IsStudent | IsProfessor,)

    def get_queryset(self):
        student_id = self.kwargs['pk']

        if student_id == 'me':
            user = self.request.user

            if hasattr(user, 'student_user'):
                student = user.student
            else:
                return Course.objects.none()
        else:
            try:
                student = Student.objects.get(id=int(student_id))
            except Student.DoesNotExist:
                return Course.objects.none()

        course_token = student.courses_taken.all()
        available_courses = Course.objects.exclude(id__in=course_token, faculty_id=student.faculty_id)

        course_with_pre_requisite = available_courses.filter(pre_requisite__in=course_token)
        course_with_co_requisite = available_courses.filter(co_requisite__in=course_token)
        queryset = course_with_pre_requisite.union(course_with_co_requisite)
        return queryset

    @action(detail=False, methods=['get'], url_path='my-courses')
    def my_courses(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)