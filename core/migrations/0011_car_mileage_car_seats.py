# Generated by Django 4.1.7 on 2023-03-21 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_price_car_price_per_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='seats',
            field=models.IntegerField(default=0),
        ),
    ]
