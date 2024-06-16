from rest_framework import serializers
from patient.models import Treatment
from patient.serializers import PatientSerializer
from drug.serializers import DrugSerializer


class TreatmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)
    patientID = serializers.IntegerField(source="patient_id", write_only=True)
    doctorName = serializers.CharField(source="doctor_name")
    drugs = DrugSerializer(many=True, read_only=True)
    drugIds = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        write_only=True,
    )
    createdAt = serializers.DateTimeField(source="created_at", read_only=True)

    class Meta:
        model = Treatment
        fields = [
            "id",
            "patient",
            "patientID",
            "doctorName",
            "disease",
            "treatment",
            "drugs",
            "drugIds",
            "note",
            "createdAt",
        ]

    def create(self, validated_data):
        drug_ids = validated_data.pop("drugIds")
        treatment = super().create(validated_data)
        treatment.drugs.set(drug_ids)
        return treatment

    def update(self, instance, validated_data):
        drug_ids = validated_data.pop("drugIds")
        treatment = super().update(instance, validated_data)
        treatment.drugs.set(drug_ids)
        return treatment


class TreatmentNestedSerializer(TreatmentSerializer):
    patientID = None

    class Meta:
        model = Treatment
        fields = [
            "id",
            "patient",
            "doctorName",
            "disease",
            "treatment",
            "drugs",
            "drugIds",
            "note",
            "createdAt",
        ]

    def create(self, validated_data):
        validated_data["patient_id"] = self.context["request"].data["patient_id"]
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["patient_id"] = self.context["request"].data["patient_id"]
        return super().update(instance, validated_data)
