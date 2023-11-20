from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course.views.class_schedule import ClassScheduleViewSet
from course.views.exam_schedule import ExamScheduleViewSet
from . import views

app_name = 'course'
router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'term-courses', views.TermCourseViewSet)

class_schedule_router = DefaultRouter
class_schedule_router.register(r'class-schedule', ClassScheduleViewSet, basename='class-schedule')

exam_schedule_router = DefaultRouter
exam_schedule_router.register(r'exam-schedule', ExamScheduleViewSet, basename='exam-schedule')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(class_schedule_router.urls)),
    path('', include(exam_schedule_router.urls)),
]
