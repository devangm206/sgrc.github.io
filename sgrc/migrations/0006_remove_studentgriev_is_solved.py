# Generated by Django 3.2.7 on 2021-11-11 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgrc', '0005_studentgriev_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgriev',
            name='is_solved',
        ),
    ]