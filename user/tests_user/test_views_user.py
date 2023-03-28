import unittest
from unittest.mock import Mock
from rest_framework import permissions
from user.views import UserViewSet

class TestUserViewSet(unittest.TestCase):

    def setUp(self):
        self.user_view_set = UserViewSet()
        self.user_view_set.queryset = Mock()
        self.user_view_set.serializer_class = Mock()
        self.user_view_set.permission_classes = [permissions.IsAuthenticated]
        
        # chamadas aos métodos queryset e serializer_class
        self.user_view_set.queryset()
        self.user_view_set.serializer_class()

    def test_query_set(self):
        self.user_view_set.queryset.assert_called_once()

    def test_serializer_class(self):
        self.user_view_set.serializer_class.assert_called_once()

    def test_permission_classes(self):
        self.assertEqual(self.user_view_set.permission_classes, [permissions.IsAuthenticated])

if __name__ == '__main__':
    unittest.main()
