from rest_framework.viewsets import ModelViewSet
from drug.models import Drug
from drug.serializers import DrugSerializer


class DrugViewSet(ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    http_method_names = ["get", "post", "patch"]
