from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_id']