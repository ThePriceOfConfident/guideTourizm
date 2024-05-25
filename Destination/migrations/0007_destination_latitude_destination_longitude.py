# Generated by Django 5.0 on 2024-05-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Destination', '0006_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='Latitude',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='destination',
            name='Longitude',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Longitude'),
        ),
    ]
