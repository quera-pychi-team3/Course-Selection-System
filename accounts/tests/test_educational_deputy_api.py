
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.reverse import reverse
from accounts.models import EducationalDeputy, User
from college.models import Faculty


class EducationalDeputyViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.base_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.token = str(AccessToken.for_user(self.base_user))
        self.faculty = Faculty.objects.create(name='فنی حرفه ای 1 تبریز')
        self.faculty2 = Faculty.objects.create(name='فنی حرفه ای 2 تبریز')
        from college.models import FieldOfStudy
        self.fos = FieldOfStudy.objects.create(name='نرم افزار', group='کامپیوتر', faculty=self.faculty, units=75,
                                               degree='کارشناسی')
        self.educational_deputy = EducationalDeputy.objects.create(user=self.base_user, faculty=self.faculty,
                                                                   field_of_study=self.fos)

    def test_list_educational_deputies_unauthenticated(self):
        response = self.client.get('/accounts/admin/educationaldeputies/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_educational_deputies_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/accounts/admin/educationaldeputies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_educational_deputy_unauthenticated(self):
        response = self.client.post('/accounts/admin/educationaldeputies/', data={
            'user': self.base_user.pk,
            'faculty': self.faculty.pk,
            'field_of_study': self.fos.pk,
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_educational_deputy_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.post('/accounts/admin/educationaldeputies/', data={
            'user': self.base_user.pk,
            'faculty': self.faculty.pk,
            'field_of_study': self.fos.pk,
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_educational_deputy_unauthenticated(self):
        response = self.client.get('/accounts/admin/educationaldeputies/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_educational_deputy_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/accounts/admin/educationaldeputies/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_educational_deputy_unauthenticated(self):
        response = self.client.put('/accounts/admin/educationaldeputies/1/', data={
            'user': self.base_user.pk,
            'faculty': self.faculty2.pk,
            'field_of_study': self.fos.pk,
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_educational_deputy_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put('/accounts/admin/educationaldeputies/1/', data={
            'user': self.base_user.pk,
            'faculty': self.faculty2.pk,
            'field_of_study': self.fos.pk,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_educational_deputy_unauthenticated(self):
        response = self.client.delete('/accounts/admin/educationaldeputies/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_educational_deputy_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.delete('/accounts/admin/educationaldeputies/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




