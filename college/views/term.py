from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from college.models import Term
from course.models import Course
from college.serializers import TermSerializer
from course.serializers import CourseSerializer
from accounts.models import Student, ITAdmin
from accounts.permissions import IsStudent, IsProfessor, IsITAdmin



@extend_schema(tags=["term"])
class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsStudent | IsProfessor]
        elif self.action == 'create':
            permission_classes = [IsITAdmin, IsAuthenticated]
        else:
            permission_classes = [IsStudent | IsProfessor]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

@extend_schema(tags=["term"])
class StudentCoursesAPIView(generics.ListAPIView):
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
