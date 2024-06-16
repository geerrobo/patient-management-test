from rest_framework_nested import routers
from .views import PatientViewSet, TreatmentViewSet, TreatmentNestedViewSet

router = routers.DefaultRouter()

router.register("treatments", TreatmentViewSet, basename="treatment")
router.register("", PatientViewSet, basename="patient")
patient_router = routers.NestedDefaultRouter(router, r"", lookup="patient")
patient_router.register(
    "treatment",
    TreatmentNestedViewSet,
    basename="patient-treatment",
)

urlpatterns = router.urls + patient_router.urls
