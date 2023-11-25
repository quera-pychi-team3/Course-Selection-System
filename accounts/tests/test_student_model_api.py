from django.test import TestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken

from accounts.models import Student, User, Professor, Expertise, Degree, EducationalDeputy, ITAdmin
from accounts.serializers import StudentSerializer
from college.models import Faculty, FieldOfStudy
from course.models import Course
from rest_framework.test import APITestCase, APIClient


class StudentViewSetTests(APITestCase):

    def setUp(self):
        # Create a test user
        self.base_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.client = APIClient()
        self.token = str(AccessToken.for_user(self.base_user))

        self.faculty = Faculty.objects.create(name='فنی حرفه ای 1 تبریز')
        self.fos = FieldOfStudy.objects.create(name='نرم افزار', group='کامپیوتر', faculty=self.faculty, units=75,
                                               degree='کارشناسی')
        self.passed_courses = [Course.objects.create(name='تاریخ', faculty=self.faculty,
                                                     credits=3, course_type='core'), ]
        self.taken_courses = [Course.objects.create(name='سیستم عامل', faculty=self.faculty,
                                                    credits=3, course_type='specialized'), ]

        self.expertise = Expertise.objects.create(name='نرم افزار')
        self.degree = Degree.objects.create(name='دکترا')
        self.professor = Professor.objects.create(user=self.base_user, faculty=self.faculty, field_of_study=self.fos,
                                                  expertise=self.expertise, degree=self.degree)
        self.professor.past_teaching_courses.add(*self.taken_courses)
        self.student = Student.objects.create(user=self.base_user, entry_year='1375-10-10', entry_term=1, gpa=18.0,
                                              faculty=self.faculty, field_of_study=self.fos, supervisor=self.professor,
                                              military_service_status='SBJ',
                                              academic_years=2)
        self.student.courses_passed.add(*self.passed_courses)
        self.student.courses_taken.add(*self.taken_courses)

    def test_list_students_authenticated_without_educational_deputy(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get('/accounts/students/')
        self.assertEqual(response.status_code, 403)

    def test_list_students_authenticated_with_educational_deputy(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        EducationalDeputy.objects.create(user=self.base_user, faculty=self.faculty, field_of_study=self.fos)
        response = self.client.get('/accounts/students/')
        self.assertEqual(response.status_code, 200)

    def test_list_students_unauthenticated(self):
        response = self.client.get('/accounts/students/')
        self.assertEqual(response.status_code, 401)

    def test_retrieve_student_authenticated_without_educational_deputy(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(f'/accounts/students/{self.student.pk}/')
        self.assertEqual(response.status_code, 403)

    def test_retrieve_student_authenticated_with_educational_deputy(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        EducationalDeputy.objects.create(user=self.base_user, faculty=self.faculty, field_of_study=self.fos)
        response = self.client.get(f'/accounts/students/{self.student.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_student_unauthenticated(self):
        response = self.client.get(f'/accounts/students/{self.student.pk}/')
        self.assertEqual(response.status_code, 401)

    def test_update_student_unauthenticated(self):
        response = self.client.put(f'/accounts/students/{self.student.pk}/', data={'gpa': 19.0})
        self.assertEqual(response.status_code, 401)

    def test_update_student_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        updated_data = {
            'user_first_name': 'John',
            'user_last_name': 'Doe',
            'user_email': 'john.doe@example.com',
            'user_phone_number': '1234567890',
        }
        response = self.client.put(f'/accounts/students/{self.student.pk}/', data=updated_data)
        self.assertEqual(response.status_code, 200)

    def test_update_student_authenticated_with_educational_deputy(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        updated_data = {
            'user_first_name': 'John',
            'user_last_name': 'Doe',
            'user_email': 'john.doe@example.com',
            'user_phone_number': '1234567890',
        }
        EducationalDeputy.objects.create(user=self.base_user, faculty=self.faculty, field_of_study=self.fos)
        response = self.client.put(f'/accounts/students/{self.student.pk}/', data=updated_data)
        self.assertEqual(response.status_code, 200)


class StudentViewSetITAdminTests(APITestCase):

        def setUp(self):
            # Create a test user
            self.base_user = User.objects.create_user(
                username='testuser',
                password='testpassword'
            )

            self.client = APIClient()
            self.token = str(AccessToken.for_user(self.base_user))

            self.faculty = Faculty.objects.create(name='فنی حرفه ای 1 تبریز')
            self.fos = FieldOfStudy.objects.create(name='نرم افزار', group='کامپیوتر', faculty=self.faculty, units=75,
                                                degree='کارشناسی')
            self.passed_courses = [Course.objects.create(name='تاریخ', faculty=self.faculty,
                                                        credits=3, course_type='core'), ]
            self.taken_courses = [Course.objects.create(name='سیستم عامل', faculty=self.faculty,
                                                        credits=3, course_type='specialized'), ]

            self.expertise = Expertise.objects.create(name='نرم افزار')
            self.degree = Degree.objects.create(name='دکترا')
            self.professor = Professor.objects.create(user=self.base_user, faculty=self.faculty, field_of_study=self.fos,
                                                    expertise=self.expertise, degree=self.degree)
            self.professor.past_teaching_courses.add(*self.taken_courses)
            self.student = Student.objects.create(user=self.base_user, entry_year='1375-10-10', entry_term=1, gpa=18.0,
                                                faculty=self.faculty, field_of_study=self.fos, supervisor=self.professor,
                                                military_service_status='SBJ',
                                                academic_years=2)
            self.student.courses_passed.add(*self.passed_courses)
            self.student.courses_taken.add(*self.taken_courses)

        def test_list_students_authenticated_without_it_admin(self):
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
            response = self.client.get('/accounts/admin/students-itadmin/')
            self.assertEqual(response.status_code, 403)

        def test_list_students_authenticated_with_it_admin(self):
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
            ITAdmin.objects.create(user=self.base_user)
            response = self.client.get('/accounts/admin/students-itadmin/')
            self.assertEqual(response.status_code, 200)

        def test_list_students_unauthenticated(self):
            response = self.client.get('/accounts/admin/students-itadmin/')
            self.assertEqual(response.status_code, 401)

        def test_retrieve_student_authenticated_without_it_admin(self):
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
            response = self.client.get(f'/accounts/admin/students-itadmin/{self.student.pk}/')
            self.assertEqual(response.status_code, 403)

        def test_retrieve_student_authenticated_with_it_admin(self):
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
            ITAdmin.objects.create(user=self.base_user)
            response = self.client.get(f'/accounts/admin/students-itadmin/{self.student.pk}/')
            self.assertEqual(response.status_code, 200)

        def test_retrieve_student_unauthenticated(self):
            response = self.client.get(f'/accounts/admin/students-itadmin/{self.student.pk}/')
            self.assertEqual(response.status_code, 401)

        def test_update_student_unauthenticated(self):
            response = self.client.put(f'/accounts/admin/students-itadmin/{self.student.pk}/', data={'gpa': 19.0})
            self.assertEqual(response.status_code, 401)

        def test_update_student_authenticated(self):
            course1 = Course.objects.create(name='تاریخ', faculty=self.faculty,
                                                        credits=3, course_type='core')
            course2 = Course.objects.create(name='سیستم عامل', faculty=self.faculty,
                                                        credits=3, course_type='specialized')

            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
            updated_data = {
                'user' : self.base_user.pk,
                'user_first_name': 'John',
                'user_last_name': 'Doe',
                'user_email': 'john.doe@example.com',
                'user_phone_number': '1234567890',
                'entry_year': '1375-10-10',
                'entry_term': 1,
                'gpa': 18.0,
                'faculty': self.faculty.pk,
                'field_of_study': self.fos.pk,
                'supervisor': self.professor.pk,
                'military_service_status': 'SBJ',
                'academic_years': 2,
                'courses_taken': [course1.pk, course2.pk],
            }

            ITAdmin.objects.create(user=self.base_user)
            response = self.client.put(f'/accounts/admin/students-itadmin/{self.student.pk}/', data=updated_data)
            self.assertEqual(response.status_code, 200)

        def test_update_student_authenticated_without_it_admin(self):
            course1 = Course.objects.create(name='تاریخ', faculty=self.faculty,
                                                        credits=3, course_type='core')
            course2 = Course.objects.create(name='سیستم عامل', faculty=self.faculty,
                                                        credits=3, course_type='specialized')
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
            updated_data = {
                'user' : self.base_user.pk,
                'user_first_name': 'Johddn',
                'user_last_name': 'Doe',
                'user_email': 'john.doe@example.com',
                'user_phone_number': '1234567890',
                'entry_year': '1375-10-10',
                'entry_term': 1,
                'gpa': 18.0,
                'faculty': self.faculty.pk,
                'field_of_study': self.fos.pk,
                'supervisor': self.professor.pk,
                'military_service_status': 'SBJ',
                'academic_years': 2,
                'courses_taken': [course1.pk, course2.pk],
            }

            response = self.client.put(f'/accounts/admin/students-itadmin/{self.student.pk}/', data=updated_data)
            self.assertEqual(response.status_code, 403)

        def test_delete_student(self):
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
            ITAdmin.objects.create(user=self.base_user)
            response = self.client.delete(f'/accounts/admin/students-itadmin/{self.student.pk}/')
            self.assertEqual(response.status_code, 204)

        def test_delete_student_unauthenticated(self):
            response = self.client.delete(f'/accounts/admin/students-itadmin/{self.student.pk}/')
            self.assertEqual(response.status_code, 401)

        def test_delete_student_authenticated_without_it_admin(self):
            self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
            response = self.client.delete(f'/accounts/admin/students-itadmin/{self.student.pk}/')
            self.assertEqual(response.status_code, 403)


