# Generated by Django 4.2.16 on 2024-10-25 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_car_unavailable_units'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='quantity',
            new_name='total_units',
        ),
    ]
