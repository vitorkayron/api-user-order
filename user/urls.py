from user.views import UserViewSet
from rest_framework.routers import DefaultRouter

app_name = 'user'

router = DefaultRouter(trailing_slash=False)
router.register('', UserViewSet)

urlpatterns = router.urls