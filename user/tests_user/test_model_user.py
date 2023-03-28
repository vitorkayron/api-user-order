from django.test import TestCase
from user.models import User

class UserTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            name='John Doe',
            cpf='12345678900',
            email='johndoe@example.com',
            phone_number='(555) 555-5555'
        )

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.name, 'John Doe')
        self.assertEqual(self.user.cpf, '12345678900')
        self.assertEqual(self.user.email, 'johndoe@example.com')
        self.assertEqual(self.user.phone_number, '(555) 555-5555')

    def test_user_update(self):
        self.user.name = 'Jane Doe'
        self.user.save()
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.name, 'Jane Doe')
        self.assertIsNotNone(updated_user.updated_at)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'John Doe')

