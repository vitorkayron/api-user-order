import unittest
from unittest.mock import Mock
from rest_framework import permissions
from order.views import OrderViewSet

class TestOrderViewSet(unittest.TestCase):

    def setUp(self):
        self.order_view_set = OrderViewSet()
        self.order_view_set.queryset = Mock()
        self.order_view_set.serializer_class = Mock()
        self.order_view_set.permission_classes = [permissions.IsAuthenticated]
        
        # chamadas aos métodos queryset e serializer_class
        self.order_view_set.queryset()
        self.order_view_set.serializer_class()

    def test_query_set(self):
        self.order_view_set.queryset.assert_called_once()

    def test_serializer_class(self):
        self.order_view_set.serializer_class.assert_called_once()

    def test_permission_classes(self):
        self.assertEqual(self.order_view_set.permission_classes, [permissions.IsAuthenticated])

if __name__ == '__main__':
    unittest.main()
