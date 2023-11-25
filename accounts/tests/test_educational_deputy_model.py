from django.test import TestCase
from accounts.models import User, EducationalDeputy
from college.models import Faculty, FieldOfStudy


class CustomUserModelTest(TestCase):

    def setUp(self):
        # Create a test user
        self.base_user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.faculty = Faculty.objects.create(name='فنی حرفه ای 1 تبریز')
        self.faculty2 = Faculty.objects.create(name='فنی حرفه ای 2 تبریز')
        self.fos = FieldOfStudy.objects.create(name='نرم افزار', group='کامپیوتر', faculty=self.faculty, units=75,
                                               degree='کارشناسی')
        self.educational_deputy = EducationalDeputy.objects.create(user=self.base_user, faculty=self.faculty,
                                                                   field_of_study=self.fos)

    def test_educational_deputy_create(self):
        self.educational_deputy.save()
        self.assertEqual(self.educational_deputy.faculty.name, 'فنی حرفه ای 1 تبریز')

    def test_educational_deputy_retrieve(self):
        educational_deputy = EducationalDeputy.objects.get(pk=self.educational_deputy.pk)
        self.assertEqual(educational_deputy.faculty.name, 'فنی حرفه ای 1 تبریز')

    def test_educational_deputy_update(self):
        old = self.educational_deputy.faculty.name
        self.educational_deputy.faculty=self.faculty2
        self.educational_deputy.save()
        educational_deputy = EducationalDeputy.objects.get(pk=self.educational_deputy.pk)
        self.assertNotEqual(educational_deputy.faculty.name, old)

    def test_educational_deputy_delete(self):
        pk = self.educational_deputy.pk
        self.educational_deputy.delete()
        result = EducationalDeputy.objects.filter(pk=pk).exists()
        self.assertEqual(result, False)
