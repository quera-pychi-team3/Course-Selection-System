from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from accounts.models import Professor, Expertise, Degree, EducationalDeputy, ITAdmin, Student
from accounts.models import User

from college.models import Faculty, FieldOfStudy
from course.models import Course
from accounts.models import Professor, Expertise, Degree, EducationalDeputy, ITAdmin


class ProfessorViewSetITAdminTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.base_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.faculty = Faculty.objects.create(name='فنی حرفه ای 1 تبریز')
        self.fos = FieldOfStudy.objects.create(name='نرم افزار', group='کامپیوتر', faculty=self.faculty, units=75,
                                               degree='کارشناسی')
        self.passed_courses = [Course.objects.create(name='تاریخ', faculty=self.faculty,
                                                     credits=3, course_type='core'), ]
        self.taken_courses = [Course.objects.create(name='سیستم عامل', faculty=self.faculty,
                                                    credits=3, course_type='specialized'), ]


        self.expertise = Expertise.objects.create(name='نرم افزار')
        self.degree = Degree.objects.create(name='دکترا')
        self.degree2 = Degree.objects.create(name='لیسانس')
        self.professor = Professor.objects.create(user=self.base_user, faculty=self.faculty, field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        self.professor.past_teaching_courses.add(*self.taken_courses)

        self.token = str(AccessToken.for_user(self.base_user))

    def test_list_professors_authenticated_with_itadmin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        ITAdmin.objects.create(user=self.base_user)
        response = self.client.get('/accounts/admin/professors-itadmin/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_professors_unauthenticated(self):
        response = self.client.get('/accounts/admin/professors-itadmin/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_professor_authenticated_with_itadmin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        ITAdmin.objects.create(user=self.base_user)
        response = self.client.post('/accounts/admin/professors-itadmin/', data={
            'user': self.base_user.pk,
            'faculty': self.faculty.pk,
            'field_of_study': self.fos.pk,
            'expertise': self.expertise.pk,
            'degree': self.degree.pk,
            'past_teaching_courses': [self.taken_courses[0].pk]
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_professor_unauthenticated(self):
        response = self.client.post('/accounts/admin/professors-itadmin/', data={
            'user': self.base_user.pk,
            'faculty': self.faculty.pk,
            'field_of_study': self.fos.pk,
            'expertise': self.expertise.pk,
            'degree': self.degree.pk,
            'past_teaching_courses': [self.taken_courses[0].pk]
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_professor_authenticated_with_itadmin_with_invalid_data(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        ITAdmin.objects.create(user=self.base_user)
        response = self.client.post('/accounts/admin/professors-itadmin/', data={
            'user': self.base_user.pk,
            'faculty': self.faculty.pk,
            'field_of_study': self.fos.pk,
            'expertise': self.expertise.pk,
            'degree': self.degree.pk,
            'past_teaching_courses': [self.taken_courses[0].pk]
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_professor_authenticated_with_itadmin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        ITAdmin.objects.create(user=self.base_user)
        response = self.client.put(f'/accounts/admin/professors-itadmin/{self.professor.pk}/', data={
            'user': self.base_user.pk,
            'faculty': self.faculty.pk,
            'field_of_study': self.fos.pk,
            'expertise': self.expertise.pk,
            'degree': self.degree2.pk,
            'past_teaching_courses': [self.taken_courses[0].pk]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_professor_unauthenticated(self):
        response = self.client.put(f'/accounts/admin/professors-itadmin/{self.professor.pk}/', data={
            'user': self.base_user.pk,
            'faculty': self.faculty.pk,
            'field_of_study': self.fos.pk,
            'expertise': self.expertise.pk,
            'degree': self.degree2.pk,
            'past_teaching_courses': [self.taken_courses[0].pk]
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_professor_unauthenticated(self):
        response = self.client.delete(f'/accounts/admin/professors-itadmin/{self.professor.pk}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_professor_authenticated_with_itadmin(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        ITAdmin.objects.create(user=self.base_user)
        response = self.client.delete(f'/accounts/admin/professors-itadmin/{self.professor.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
