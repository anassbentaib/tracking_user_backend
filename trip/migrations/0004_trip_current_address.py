# Generated by Django 5.1.7 on 2025-03-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_trip_dropoff_address_trip_pickup_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='current_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
