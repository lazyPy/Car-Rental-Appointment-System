# Generated by Django 4.2.16 on 2024-11-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_alter_reservation_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]