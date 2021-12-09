# Generated by Django 3.2.7 on 2021-11-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sgrc', '0004_alter_studentgriev_is_solved'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgriev',
            name='status',
            field=models.CharField(choices=[('sl', 'Solved'), ('p', 'Pending'), ('nsl', 'Not Solved')], default='', max_length=100),
        ),
    ]