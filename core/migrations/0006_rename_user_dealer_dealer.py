# Generated by Django 4.1.7 on 2023-03-18 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_dealer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealer',
            old_name='user',
            new_name='dealer',
        ),
    ]