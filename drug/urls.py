from rest_framework_nested import routers
from .views import DrugViewSet

router = routers.DefaultRouter()
router.register("", DrugViewSet, basename="drug")

urlpatterns = router.urls
