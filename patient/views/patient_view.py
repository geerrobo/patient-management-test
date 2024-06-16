from rest_framework.viewsets import ModelViewSet
from patient.models import Patient
from patient.serializers import PatientSerializer


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    http_method_names = ["get", "post", "patch"]
