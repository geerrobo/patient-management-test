# Generated by Django 5.0.6 on 2024-06-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField()),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=20
                    ),
                ),
                ("address", models.TextField()),
                ("phone_number", models.CharField(max_length=20)),
                ("insurance_id", models.CharField(max_length=100)),
                ("insurance_provider", models.CharField(max_length=100)),
                ("emergency_contact_name", models.CharField(max_length=50)),
                ("emergency_contact_phone", models.CharField(max_length=20)),
                ("congenital_disease", models.TextField()),
                ("drug_allergy", models.TextField()),
                ("note", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
