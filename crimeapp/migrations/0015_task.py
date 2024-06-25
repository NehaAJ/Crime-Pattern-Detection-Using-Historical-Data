# Generated by Django 4.1.5 on 2023-05-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crimeapp", "0014_duty"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("date", models.DateField()),
                ("task", models.CharField(max_length=200)),
            ],
        ),
    ]
