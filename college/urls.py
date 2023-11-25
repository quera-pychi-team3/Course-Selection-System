from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.faculty import FacultyViewSet
from .views.term import TermViewSet

app_name = 'college'

router = DefaultRouter()
router.register(r'faculty', FacultyViewSet)
router.register(r'terms', TermViewSet, basename='term')

urlpatterns = [
    path('terms/', TermViewSet.as_view({'get': 'list'}), name='term-list'),
    path('terms/<int:pk>/', TermViewSet.as_view({'get': 'list'}), name='term-detail'),
    path('admin/', include(router.urls)),  
]
