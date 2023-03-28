from order.views import OrderViewSet
from rest_framework.routers import DefaultRouter

app_name = 'order'

router = DefaultRouter(trailing_slash=False)
router.register('', OrderViewSet)

urlpatterns = router.urls