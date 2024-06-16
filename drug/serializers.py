from rest_framework import serializers
from drug.models import Drug


class DrugSerializer(serializers.ModelSerializer):
    sideEffect = serializers.CharField(source="side_effect")

    class Meta:
        model = Drug
        fields = [
            "id",
            "name",
            "description",
            "sideEffect",
        ]
