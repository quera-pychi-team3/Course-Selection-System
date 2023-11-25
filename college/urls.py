from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.faculty import FacultyViewSet
from .views.term import TermViewSet, TermListAPIView, TermDetailAPIView, StudentCoursesAPIView

app_name = 'college'

router = DefaultRouter()
router.register(r'faculty', FacultyViewSet)
router.register(r'terms', TermViewSet, basename='term')

urlpatterns = [
    path('terms/', TermListAPIView.as_view(), name='term-list'),
    path('terms/<int:pk>/', TermDetailAPIView.as_view(), name='term-detail'),
    path('student/<str:pk>/my-courses/', StudentCoursesAPIView.as_view(), name='student-courses'),
    path('admin/', include(router.urls)),  
]

