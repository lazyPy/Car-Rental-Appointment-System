# Generated by Django 4.2.16 on 2024-10-15 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_carimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='payment_source_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
