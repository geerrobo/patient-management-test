from rest_framework import serializers
from patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    dateOfBirth = serializers.DateField(source="date_of_birth")
    phoneNumber = serializers.CharField(source="phone_number")
    insuranceID = serializers.CharField(
        source="insurance_id", allow_blank=True, allow_null=True
    )
    insuranceProvider = serializers.CharField(
        source="insurance_provider", allow_blank=True, allow_null=True
    )
    emergencyContactName = serializers.CharField(
        source="emergency_contact_name", allow_blank=True, allow_null=True
    )
    emergencyContactPhone = serializers.CharField(
        source="emergency_contact_phone", allow_blank=True, allow_null=True
    )
    congenitalDisease = serializers.CharField(
        source="congenital_disease", allow_blank=True, allow_null=True
    )
    drugAllergy = serializers.CharField(
        source="drug_allergy", allow_blank=True, allow_null=True
    )

    class Meta:
        model = Patient
        fields = [
            "id",
            "firstName",
            "lastName",
            "dateOfBirth",
            "gender",
            "address",
            "phoneNumber",
            "insuranceID",
            "insuranceProvider",
            "emergencyContactName",
            "emergencyContactPhone",
            "congenitalDisease",
            "drugAllergy",
            "note",
        ]
