# Generated by Django 4.1.4 on 2023-04-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0009_alter_medicalrecords_date_alter_medicalrecords_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalrecords',
            name='hospital',
            field=models.CharField(max_length=200, null=True),
        ),
    ]