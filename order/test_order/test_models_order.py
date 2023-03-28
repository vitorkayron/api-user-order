from django.test import TestCase
from user.models import User
from order.models import Order

class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        user = User.objects.create(name='testuser', cpf='111.111.111-11', email='test@example.com', phone_number='123456789')
        Order.objects.create(user_id=user, item_description='Test Item', item_quantity=2, item_price=10.00)

    def test_total_value(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.total_value, 20.00)

    def test_updated_at(self):
        order = Order.objects.get(id=1)
        order.item_quantity = 3
        order.save()
        self.assertIsNotNone(order.updated_at)