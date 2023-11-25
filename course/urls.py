from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course.views.student_course import StudentCoursesViewSet
from . import views

app_name = 'course'
router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'term-courses', views.TermCourseViewSet)
router.register(r'student-courses', StudentCoursesViewSet, basename='student-courses')


urlpatterns = [
    path('', include(router.urls)),
    path('student/<str:pk>/my-courses/', include(router.urls)),
]
