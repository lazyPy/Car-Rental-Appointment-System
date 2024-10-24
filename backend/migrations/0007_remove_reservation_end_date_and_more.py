# Generated by Django 4.2.16 on 2024-10-24 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_car_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='start_date',
        ),
        migrations.AddField(
            model_name='reservation',
            name='end_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]