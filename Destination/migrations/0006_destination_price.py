# Generated by Django 5.0 on 2024-05-05 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Destination', '0005_alter_destination_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Price'),
        ),
    ]
