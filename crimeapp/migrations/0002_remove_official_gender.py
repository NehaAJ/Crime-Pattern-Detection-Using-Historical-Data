# Generated by Django 4.1.4 on 2022-12-19 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='official',
            name='gender',
        ),
    ]
