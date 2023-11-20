from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from .views import *
from .views.professor import ProfessorViewSet
from .views.student import StudentViewSet
from .views.educational_deputy import EducationalDeputyViewSet

app_name = 'accounts'

student_router = DefaultRouter()
professor_router = DefaultRouter()
educational_deputy_router = DefaultRouter()

student_router.register(r'students', StudentViewSet, basename='student')
professor_router.register(r'professors', ProfessorViewSet, basename='professor')

educational_deputy_router.register(r'admin/educationaldeputies', EducationalDeputyViewSet, basename='educationaldeputy')

urlpatterns = [
    path('login/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password-request/', ChangePasswordRequestView.as_view(), name='change_password_request'),
    path('change-password-action/<uidb64>/<token>/', ChangePasswordActionView.as_view(), name='change_password_action'),
] + student_router.urls + professor_router.urls + educational_deputy_router.urls
