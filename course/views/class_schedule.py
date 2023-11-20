from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from course.models import StudentCourse
from course.serializers.student_course import StudentCourseSerializer
from course.permissions.student import IsStudent

class ClassScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated, IsStudent]
    serializer_class = StudentCourseSerializer

    def get_queryset(self):
        return StudentCourse.objects.filter(student__user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
