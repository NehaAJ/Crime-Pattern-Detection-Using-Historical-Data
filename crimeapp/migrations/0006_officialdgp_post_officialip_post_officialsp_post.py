# Generated by Django 4.1.4 on 2023-02-25 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crimeapp', '0005_official_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='officialdgp',
            name='post',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='officialip',
            name='post',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='officialsp',
            name='post',
            field=models.CharField(max_length=200, null=True),
        ),
    ]