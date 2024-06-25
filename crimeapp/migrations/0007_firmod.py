# Generated by Django 4.1.4 on 2023-04-02 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('crimeapp', '0006_officialdgp_post_officialip_post_officialsp_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firmod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, null=True)),
                ('age', models.CharField(max_length=200, null=True)),
                ('occupation', models.CharField(max_length=200, null=True)),
                ('residence', models.CharField(max_length=200, null=True)),
                ('casedes', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=200, null=True)),
                ('time', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('typeofcrime', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]