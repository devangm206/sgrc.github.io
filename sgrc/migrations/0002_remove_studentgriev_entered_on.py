# Generated by Django 3.2.7 on 2021-11-09 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sgrc', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgriev',
            name='entered_on',
        ),
    ]
