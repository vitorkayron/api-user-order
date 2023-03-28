import pytest
from django.db import IntegrityError
from user.models import User
from .models import Order

@pytest.fixture
def user():
    return User.objects.create(
        username='testuser',
        email='testuser@example.com',
        password='testpassword'
    )

@pytest.fixture
def order(user):
    return Order.objects.create(
        user_id=user,
        item_description='Test Item',
        item_quantity=2,
        item_price=10.00
    )

def test_order_creation(order):
    assert order.id == 1
    assert order.user_id.username == 'testuser'
    assert order.item_description == 'Test Item'
    assert order.item_quantity == 2
    assert order.item_price == 10.00
    assert order.total_value == 20.00
    assert order.created_at is not None
    assert order.updated_at is not None

def test_order_total_value_calculation(order):
    order.item_quantity = 3
    order.save()
    assert order.total_value == 30.00

def test_order_updated_at_on_save(order):
    old_updated_at = order.updated_at
    order.item_quantity = 3
    order.save()
    assert order.updated_at > old_updated_at

def test_order_blank_total_value():
    with pytest.raises(IntegrityError):
        Order.objects.create(
            user_id=User.objects.create(),
            item_description='Test Item',
            item_quantity=2,
            item_price=10.00,
            total_value=None
        )