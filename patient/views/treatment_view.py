from rest_framework.viewsets import ModelViewSet
from patient.models import Treatment
from patient.serializers import TreatmentSerializer, TreatmentNestedSerializer


class TreatmentViewSet(ModelViewSet):
    serializer_class = TreatmentSerializer
    http_method_names = ["get", "post", "patch"]

    def get_queryset(self):
        return Treatment.objects.select_related("patient").prefetch_related("drugs")


class TreatmentNestedViewSet(ModelViewSet):
    serializer_class = TreatmentNestedSerializer
    http_method_names = ["get", "post", "patch"]

    def get_queryset(self):
        return (
            Treatment.objects.select_related("patient")
            .prefetch_related("drugs")
            .filter(patient_id=self.kwargs["patient_pk"])
        )

    def create(self, request, *args, **kwargs):
        request.data["patient_id"] = self.kwargs["patient_pk"]
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.data["patient_id"] = self.kwargs["patient_pk"]
        return super().update(request, *args, **kwargs)
