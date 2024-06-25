# Generated by Django 4.1.5 on 2023-05-21 07:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("crimeapp", "0015_task"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task", old_name="task", new_name="characters",
        ),
        migrations.RenameField(
            model_name="task", old_name="date", new_name="end_date",
        ),
        migrations.AddField(
            model_name="task",
            name="start_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
